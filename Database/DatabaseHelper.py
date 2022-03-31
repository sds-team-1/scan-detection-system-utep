# DatabaseHelper 
from pprint import pprint
from typing import List
from pymongo import MongoClient
from bson.objectid import ObjectId

class SDSDatabaseHelper:
    url = "mongodb://localhost:27017"

    def __init__(self):
        client = MongoClient(self.url)
        db = client.SDS
        serverStatusResult = db.command("serverStatus")

    """Create Project scenario"""
    def create_workspace(self, workspace_name) -> bool:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['workspaces']
        try:
            collection.insert_one({'_id': workspace_name, 'projects': []})
        except:
            return False
        return True

    def create_project(self, workspace_name: str, project_name: str = '', 
        par_units: int = 1, scenario_units: List = [], project: dict = None) -> bool:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['projects']
        if not project:
            try:
                collection.insert_one({'_id': project_name, 'parallel_units': par_units,
                'scenario_units': scenario_units})
            except:
                return False
        else:
            try:
                collection.insert_one(project)
                project_name = project['_id']
            except:
                return False
        collection = db['workspaces']
        query = {'_id': workspace_name}
        update = {'$addToSet': {'projects': project_name}}
        success = collection.update_one(query, update)
        return False if success == 0 else True

    def retrieve_workspaces(self) -> List[str]:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['workspaces']
        return collection.find().distinct('_id')

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
            result = collection.update_one({'_id': project_name}, {'$set': new_data})
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
            networks = data['networks']
            data['networks'] = []
            devices = data['devices']
            data['devices'] = []
            links = data['links']
            data['links'] = []

            #Saves the scenario and retrieves the id
            scenario_objid = collection.insert_one(data).inserted_id

            network_keys = networks.keys()
            for k in network_keys:
                self.create_network(scenario_objid, networks[k])
            device_keys = devices.keys()
            for k in device_keys:
                self.create_device(scenario_objid, devices[k])
            link_keys = links.keys()
            for k in link_keys:
                self.create_link(scenario_objid, links[k])
        except:
            print('ERROR:DatabaseHelper -> Duplicate Key. Scenario ID already exists')
            return ''
        # Add key to projects scenarios property
        collection = db['projects']
        query = {'_id': project_name}
        update = {'scenario_units': scenario_objid}
        collection.update_one(query, {'$set': update})
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

    def create_network(self, scenario_id: str, data: dict) -> bool:
        #TODO: Make this
        pass

    def retrieve_network(self, network_id: str, data: dict) -> dict:
        #TODO: Make this
        pass

    def save_network(self, network_id: str, data: dict) -> bool:
        #TODO: Make this
        pass

    def create_device(self, scenario_id: str, data: dict) -> bool:
        #TODO: Make this
        pass

    def retrieve_device(self, device_id: str) -> dict:
        #TODO: make this
        pass

    def save_device(self, device_id: str, new_data: dict) -> dict:
        #TODO: make this
        pass

    def create_link(self, scenario_id: str, data: dict) -> bool:
        #TODO: Make this
        pass

    def retrieve_link(self, device_id: str) -> dict:
        #TODO: make this
        pass

    def save_link(self, device_id: str, new_data: dict) -> dict:
        #TODO: make this
        pass