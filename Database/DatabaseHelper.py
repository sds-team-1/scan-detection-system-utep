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

    def create_project(self, workspace_name: str, project_name: str) -> bool:
        return self.create_project(workspace_name, project_name, 1, [])

    def create_project(self, workspace_name: str, project_name: str, par_units: int):
        return self.create_project(workspace_name, project_name, par_units, [])

    def create_project(self, workspace_name: str, project_name: str, 
        par_units: int, scenario_units: List) -> bool:
        client = MongoClient(self.url)
        db = client['SDS']
        collection = db['projects']
        collection.insert_one({'_id': project_name, 'parallel_units': par_units,
            'scenario_units': scenario_units})
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
        collection = db['workplaces']
        return collection.find()

    """Import Project"""

    """Save Project"""

    """Export Project"""