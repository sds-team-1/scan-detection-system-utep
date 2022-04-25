import sys
sys.path.append('../')
from Controllers.SDSController import SDSController
from Database.DatabaseHelper import SDSDatabaseHelper
from dubs.DubAnalysisManager import DubAnalysisManager
from dubs.DubCaptureController import DubCaptureController

sds_controller: SDSController = SDSController()
sds_controller.add_analysis_manager(DubAnalysisManager())
sds_controller.add_capture_manager(DubCaptureController())
sds_controller.add_mongo_connection(SDSDatabaseHelper('mongodb://localhost:27017'))

"""The purpose of this is to run in interactive mode. Run this as
    python3 -i inter_test_sdscontroller.py
    
    It will run with a prompt"""
print('sds_controller ready to test with working database')

print('Creating a testing context dictionary...')

sds_controller._enforce_state('workplace_construction')
sds_controller.specify_workplace_name('wsA')
sds_controller.finish_workplace_construction()
sds_controller.start_new_project_phase()
sds_controller.specify_project_name('pA')
sds_controller.specify_num_parrallel_units(1)
sds_controller.finish_project_construction()
sds_controller.add_scenario_unit()
sds_controller.insert_scenario_name('sA')
sds_controller.finish_scenario_unit_construction('pA', 1)
scenario_id = sds_controller.get_scenario_id('sA')
sds_controller.insert_node(scenario_id, 'test_delete_id', False, 'PC', 'nT', \
    '10.0.0.2', '00:00:00:00:01', False, False, '', '', '', 1, 1, 'time 00:01')
#sds_controller.delete_workspace_contents('wsA')
print(f'Finished creating simple workspace, project, scenario, and node labeled:\
     wsA, pA, {scenario_id}, test_delete_id')