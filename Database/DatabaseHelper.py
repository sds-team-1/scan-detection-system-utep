# DatabaseHelper 
from pprint import pprint
from typing import List
from pymongo import MongoClient
from bson.objectid import ObjectId

class SDSDatabaseHelper:
    url = "mongodb://localhost:27017"
    TIMEOUT_MS = 5000

    def __init__(self, ip_port: str):
        self.url = ip_port
        client = MongoClient(self.url, serverSelectionTimeoutMS = self.TIMEOUT_MS)
        db = client.SDS
        serverStatusResult = db.command("serverStatus")

    """Create Project scenario"""
    def create_workspace(self, workspace_name) -> bool:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['workspaces']
        try:
            collection.insert_one({'_id': workspace_name, 'projects': [], \
                'core_sds_service_ip': '', 'core_sds_port_number': ''})
        except:
            return False
        return True

    def update_workspace_projects(self, workspace_name: str, project_name: str) -> bool:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['workspaces']
        try:
            collection.update_one({'_id': workspace_name}, {'$push': {'projects': project_name}})
            return True
        except:
            return False


    def save_workspace(self, workspace_name: str, data: dict):
        client = MongoClient(self.url)
        db = client.SDS
        collection = db['workspaces']
        try:
            result = collection.update_one({'_id': workspace_name}, {'$set': data})
            return True if result.matched_count else False
        except:
            return False

    def create_project(self, workspace_name: str, project_name: str = '', 
        par_units: int = 1, scenario_units: List = [], project: dict = None) -> bool:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['projects']
        #print('dbhelper showing project...')
        #print(project)
        if not project:
            try:
                collection.insert_one({'_id': project_name, 'parallel_units': par_units,
                'scenario_units': scenario_units})
                update = {'$addToSet': {'projects': project_name}}
            except:
                return False
        else:
            try:
                collection.insert_one(project)
                update = {'$push': {'projects': project['_id']}}
            except:
                return False
        collection = db['workspaces']
        query = {'_id': workspace_name}
        #print('createproject showing update...')
        #print(query)
        #print(update)
        success = collection.update_one(query, update)
        return False if success == 0 else True

    def retrieve_workspaces(self) -> List[str]:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['workspaces']
        return collection.find().distinct('_id')
    
    def get_workspace_context(self, workspace_name: str) -> dict:
        client = MongoClient(self.url)
        db = client.SDS
        collection = db['workspaces']
        workspace_dict = collection.find_one({'_id': workspace_name})
        # Replace all projects with data
        projects_to_remove = [project_name for project_name in workspace_dict['projects']]
        for project_name in projects_to_remove:
            # Get project Data
            project_collection = db['projects']
            project_dict = project_collection.find_one({'_id': project_name})
            if not project_dict:
                continue
            # Replace all scenarios with data
            scenarios_to_remove = [unique_scenario for unique_scenario in project_dict['scenario_units']]
            for unique_scenario in scenarios_to_remove: 
                # Get scenario data
                # Replace ids with dictionary
                scenario_collection = db['scenarios']
                scenario_dict = scenario_collection.find_one({'_id': unique_scenario})
                if not scenario_dict:
                    continue
                # Replace all nodes with data
                nodes_to_remove = [node for node in scenario_dict['nodes']]
                for node in nodes_to_remove:
                    node_collection = db['nodes']
                    node_dict = node_collection.find_one({'_id': node})
                    if not node_dict:
                        continue
                    # Replace node id with dictionary
                    scenario_dict['nodes'].append(node_dict)
                for n in nodes_to_remove:
                    scenario_dict['nodes'].remove(n)
                project_dict['scenario_units'].append(scenario_dict)
            for s in scenarios_to_remove:
                project_dict['scenario_units'].remove(s)
            workspace_dict['projects'].append(project_dict)
            # Replace project name with dictionary
        for p in projects_to_remove:
            workspace_dict['projects'].remove(p)
        return workspace_dict

    def retrieve_projects(self, workspace_name: str) -> List[dict]:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['workspaces']
        workspace_dict = collection.find_one({'_id': workspace_name})
        projects = workspace_dict['projects']
        project_list = []
        for proj in projects:    
            collection = db['projects']
            project_list.append(collection.find_one({'_id': proj}))
        return project_list

    """Import Project"""
    """Export Project"""
    def retrieve_project(self, project_name: str) -> dict:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['projects']
        data = collection.find_one({'_id': project_name})
        if data:
            if type(data['scenario_units']) is ObjectId:
                data['scenario_units'] = [str(data['scenario_units'])]
            else:
                data['scenario_units'] = [str(x) for x in data['scenario_units']]
            return data
        return {}

    """Save Project"""
    def save_project(self, project_name: str, new_data: dict) -> bool:
        client = MongoClient(self.url)
        db = client.SDS
        collection = db['projects']
        try:
            result = collection.update_one({'_id': project_name}, {'$push': new_data})
            return True if result.matched_count else False
        except Exception as e:
            return False

    """Load Scenario Units
    The DBHelper is responsible for translating dictionary data to
    MongoDB relational data. Not the controller.
    """
    def create_scenario_unit(self, project_name: str, data: dict) -> str:
        """
        Check out sample_scenarios.json for dictionary form of scenarios. 
        """
        # Create an empty scenario unit with its keys and insert the data.
        client = MongoClient(self.url)
        db = client.SDS
        collection = db['scenarios']
        scenario_objid: str = ''
        try:
            #Replace subdata w/ arrays for inserting to db
            nodes = data['nodes']
            data['nodes'] = []

            #Saves the scenario and retrieves the id
            scenario_objid = collection.insert_one(data).inserted_id

            #Insert all the keys if there 
            node_keys = nodes.keys()
            for n in node_keys:
                # Create the node
                node_db_insertion_id = self.create_node(scenario_objid, nodes[n])
        except Exception as e:
            print('ERROR:DatabaseHelper -> Duplicate Key. Scenario ID already exists')
            return ''
        # Add key to projects scenarios property
        collection = db['projects']
        query = {'_id': project_name}
        update = {'scenario_units': scenario_objid}
        collection.update_one(query, {'$push': update})
        return str(scenario_objid)

    def retrieve_scenario_unit(self, scenario_id: str) -> dict:
        client = MongoClient(self.url)
        db = client.SDS
        collection = db['scenarios']
        # Convert str into object id
        try:
            o = ObjectId(scenario_id)
        except Exception as e:
            print(e)
            return {}
        data = collection.find_one({'_id': o})
        return data if data else {}

    def save_scenario_unit(self, scenario_id: str, data: dict) -> bool:
        client = MongoClient(self.url)
        db = client.SDS
        collection = db['scenarios']
        try:
            result = collection.update_one({'_id': scenario_id}, {'$set': data})
            return True if result.matched_count else False
        except: 
            return False

    #TODO: Test this
    def create_node(self, scenario_object_id, node_data: dict) -> bool:
        # Insert the node to the database
        client = MongoClient(self.url)
        db = client.SDS
        collection = db['nodes']
        result = False
        try:
            node_obj_id = collection.insert_one(node_data).inserted_id
            query = {'_id': scenario_object_id}
            update = {'nodes': node_obj_id}
            collection = db['scenarios']
            result = collection.update_one(query, {'$push': update})
        except:
            print('Error: Database Helper could not insert the node')
        return True if result.matched_count else False

    #TODO: Implement this
    def retrieve_all_nodes_for_scenario(self, scenario_object_id: str) -> dict:
        client = MongoClient(self.url)
        db = client.SDS
        
        pass