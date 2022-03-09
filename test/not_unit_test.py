import sys

sys.path.insert(0, '../')

from Database import DatabaseHelper

database = DatabaseHelper.SDSDatabaseHelper()

print('Creating test_workspace: ' + \
    str(database.create_workspace('test_workspace')))
print('Creating workspaceA: ' + \
    str(database.create_workspace('worspaceA')))
print('Creating workspaceB: ' + \
    str(database.create_workspace('workspaceB')))

'''workspaces of the same name cannot be created'''

print('Creating workspaceB: ' + \
    str(database.create_workspace('workspaceB'))) #Should fail

print(database.retrieve_workspaces())


database.create_project('test_workplace', 'test_project')

x = database.retrieve_project('test_project')
print('Retrieving project data: ' + str(x))
print(database.retrieve_projects('test_workplace'))

new_data = {'_id': 'new_project', 'parallel_units': 2, 'scenario_units': []}
print('Saving (overwriting) test_project w/ new_project: ' + \
    str(database.save_project('test_project', new_data)))

x = database.retrieve_project('new_project')
print(x)
print(database.retrieve_projects('test_workplace'))

'''Testing exporting'''
from Controllers import SDSController

controller = SDSController.SDSController()
controller.add_mongo_connection(database)

controller._enfore_state('init_project')
controller.export_project('new_project', 
    '/home/jesoto4/Development/scan-detection-system-utep/test/export_new_project.json')
