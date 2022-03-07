import sys

sys.path.insert(0, '../')

from Database import DatabaseHelper

database = DatabaseHelper.SDSDatabaseHelper()

database.create_workspace('test_workspace')

print(database.retrieve_workspaces())

database.create_project('test_workplace', 'test_project')

print(database.retrieve_projects())