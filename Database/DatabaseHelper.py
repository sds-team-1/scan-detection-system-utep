# DatabaseHelper 
from pprint import pprint
from typing import List
from pymongo import MongoClient
from bson.objectid import ObjectId

class SDSDatabaseHelper:

    MONGO_DB_URL = "mongodb://localhost:27017"
    DATABASE_NAME = "SDS_DB"

    DEFAULT_WORKSPACE_COLLECTION_NAME = 'workspaces'

    client = MongoClient(MONGO_DB_URL)

    def __init__(self):
        '''
        Constructor
        '''
        pass

    # DATABASE FUNCTIONS

    def insert_object_into_collection(self, collection_name, object):
        '''
        Inserts an object into the specified collection
        '''
        if not self.database_exists():
            self.client.create_database(self.DATABASE_NAME)

        if not self.collection_exists(collection_name):
            self.client[self.DATABASE_NAME].create_collection(collection_name)
        
        db = self.client[self.DATABASE_NAME]
        db[collection_name].insert_one(object)

    def get_all_objects_from_collection(self, collection_name):
        '''
        Returns all objects from the specified collection
        '''
        db = self.client[self.DATABASE_NAME]
        return db[collection_name].find()

    def collection_exists(self, collection):
        '''
        Checks if the specified collection exists
        '''
        db = self.client[self.DATABASE_NAME]
        collections = db.list_collection_names()
        return collection in collections

    def database_exists(self):
        '''
        Checks if the database exists
        '''
        return self.client.get_database(self.DATABASE_NAME) != None


    # WORKSPACE FUNCTIONS

    def get_all_workspaces(self):
        '''
        Returns all workspaces
        '''
        return self.get_all_objects_from_collection(self.DEFAULT_WORKSPACE_COLLECTION_NAME)
    
    def insert_workspace(self, workspace_object):
        '''
        Inserts a workspace into the database
        '''
        self.insert_object_into_collection(self.DEFAULT_WORKSPACE_COLLECTION_NAME, workspace_object)

    def update_workspace(self, workspace_name, workspace_object):
        '''
        Updates the workspace with the specified name
        '''
        workspaces = self.get_all_workspaces()

        if workspaces is not None:
            for current_workspace in workspaces:
                if current_workspace['Name'] == workspace_name:
                    current_workspace['Name'] = workspace_object['Name']
                    current_workspace['projects'] = workspace_object['projects']
                    self.insert_object_into_collection(self.DEFAULT_WORKSPACE_COLLECTION_NAME, current_workspace)
                    return
        return


    # PROJECT FUNCTIONS

    def get_all_projects_from_workspace(self, workspace_name):
        '''
        Returns all projects under the given workspace name
        '''
        workspaces = self.get_all_workspaces()

        try:
            if workspaces is not None:
                for current_workspace in workspaces:
                    if current_workspace['Name'] == workspace_name:
                        return current_workspace['projects']
        except:
            return []

    def insert_project_into_workspace(self, workspace_name, project_object):
        '''
        Inserts a project into the specified workspace that matches the name
        '''
        workspaces = self.get_all_workspaces()

        if workspaces is not None:
            for current_workspace in workspaces:
                if current_workspace['Name'] == workspace_name:
                    current_workspace['projects'].append(project_object)
                    self.insert_object_into_collection(self.DEFAULT_WORKSPACE_COLLECTION_NAME, current_workspace)
                    return
        return