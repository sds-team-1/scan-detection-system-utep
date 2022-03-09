# DatabaseHelper 
from pprint import pprint
from typing import List
from pymongo import MongoClient

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
        query = {'workspace_name': workspace_name}
        update = {'$addToSet': {'projects': project_name}}
        success = collection.update_one(query, update)
        return False if success == 0 else True

    def retrieve_workspaces(self) -> List[str]:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['workspaces']
        return collection.find().distinct('_id')

    def retrieve_projects(self, workspace_name: str) -> List[str]:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['projects']
        return collection.find()

    """Import Project"""
    """Export Project"""
    def retrieve_project(self, project_name: str) -> dict:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['projects']
        data = collection.find_one({'_id': project_name})
        return data if data else {}

    """Save Project"""
    def save_project(self, project_name: str, new_data: dict) -> bool:
        client = MongoClient(self.url)
        db = client.SDS
        collection = db['projects']
        try:
            result = collection.delete_one({'_id': project_name})
            v = True if result.deleted_count is 1 else False
            if v: 
                collection.insert_one(new_data)
        except Exception as e:
            print(e)
            v = False
        return v 
