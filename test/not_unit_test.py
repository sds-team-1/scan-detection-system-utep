import sys

sys.path.insert(0, '../')

from Database import DatabaseHelper

database = DatabaseHelper.SDSDatabaseHelper()

database.create_workspace('test_workspace')

print(database.retrieve_workspaces())

database.create_project('test_workplace', 'test_project')

x = database.retrieve_project('test_project')

print('First project insertion')
print(type(x))
print(x)

new_data = {'_id': 'new_project', 'parallel_units': 2, 'scenario_units': []}
database.save_project('test_project', new_data)

x = database.retrieve_project('new_project')
print(x)