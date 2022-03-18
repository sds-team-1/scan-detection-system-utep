import sys

sys.path.insert(0, '../')

from Database import DatabaseHelper

database = DatabaseHelper.SDSDatabaseHelper()

database.create_project('test_workspace', 'new_project')

sample_scenario_unit = {
    'scenario_name': 'test_scenario', 
    'networks': {},
    'devices': {},
    'links': {}
}

scenario_id = database.create_scenario_unit('new_project', sample_scenario_unit)
print('Scenario ID: ' + scenario_id)

print(database.retrieve_scenario_unit(scenario_id))

'''Testing exporting'''
from Controllers import SDSController

controller = SDSController.SDSController()
controller.add_mongo_connection(database)

controller._enfore_state('init_project')
controller.add_scenario_unit()
controller.insert_scenario_name('test2_scenario')
controller.finish_scenario_unit_construction()
print(controller.list_all_scenario_units('test_workspace', 'new_project'))