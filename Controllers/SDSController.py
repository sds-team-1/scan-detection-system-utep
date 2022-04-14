from enum import Enum, unique
import json
import re
from typing import Dict, List
from Database.DatabaseHelper import SDSDatabaseHelper
from captureController import CaptureController
from Controllers.AnalysisManager import SDSAnalysisManager

@unique
class SDSStateEnum(Enum):
    INIT_SYSTEM = 1
    WORKPLACE_CONSTRUCTION = 2
    INIT_WORKPLACE = 3
    FILE_MANAGER_IMPORT_DIALOGUE = 4
    PROJECT_CONSTRUCTION = 5
    INIT_PROJECT = 6
    LAUNCHING_CORE_UNITS = 7
    SCENARIO_UNIT_CONSTRUCTION = 8
    INIT_CAPTURE_NETWORK = 9
    NETWORK_RUNNING = 10
    NETWORK_STOPPED = 11
    FILE_MANAGER_EXPORT_DIALOGUE = 12

class SDSController:

    directory_regex_pattern = '/^[^\s^\x00-\x1f\\?*:"";<>|\/.][^\x00-\x1f\\?*:"";<>|\/]*[^\s^\x00-\x1f\\?*:"";<>|\/.]+$/g'

    def __init__(self) -> None:
        self._cap_manager: CaptureController = None
        self._a_manager: SDSAnalysisManager = None
        self._db_connection: SDSDatabaseHelper = None 
        self._state = SDSStateEnum.INIT_SYSTEM
        self._workspace_name: str = ''
        self._project_name: str = ''
        self._project_construction: dict = {}
        self._scenario_unit_construction: dict = {}
        self._entire_workspace_context: dict = {}

    def add_capture_manager(self, capture_manager: CaptureController):
        if self._cap_manager == None:
            self._cap_manager = capture_manager

    def add_analysis_manager(self, analysis_manager: SDSAnalysisManager):
        if self._a_manager == None:
            self._a_manager = analysis_manager
    
    def add_mongo_connection(self, connection: SDSDatabaseHelper):
        if self._db_connection == None:
            self._db_connection = connection

    # Make sure that methods can execute. 
    def _ensure_subsystems(self):
        #assert(self._cap_manager)
        #assert(self._a_manager)
        assert(self._db_connection)

    def list_all_workplaces(self) -> List[str]:
        #Gets all the workplaces available from MongoDB
        if self._db_connection is None:
            return [] 
        else:
            #Do work here
            return self._db_connection.retrieve_workspaces()

    def list_all_projects(self, workplace_name: str) -> List[str]:
        #Gets all the projects within the workplace
        if self._db_connection is None:
            return []
        else:
            #Get project dictionaries related to workspace
            projects = self._db_connection.retrieve_projects(workplace_name)
            # Get a list of all the neames retrieved.
            if projects == [None]:
                return []
            project_names = []
            for proj in projects:
                project_names.append(proj['_id'])
            return [project['_id'] for project in projects]

    def list_all_scenario_units(self, workplace_name: str, project_name: str) -> List[str]:
        #Gets all scenario_units of specified instance
        if self._db_connection is None:
            return []
        else:
            # Get the right project context
            scenario_ids = self._db_connection.retrieve_project(project_name)['scenario_units']
            return [self._db_connection.retrieve_scenario_unit(x)['scenario_name'] for x in scenario_ids]

    def list_all_nodes(self, workplace_name: str, project_name: str, 
        scenario_unit_id: str) -> List[str]:
        if self._db_connection is None:
            return []
        else:
            #Do work here
            pass

    ###### Workspace related functions ######
    def start_new_workplace(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_SYSTEM:
            # Do work here
            self._state = SDSStateEnum.WORKPLACE_CONSTRUCTION

    def specify_workplace_name(self, workspace_name: str):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.WORKPLACE_CONSTRUCTION:
            self._workspace_name = workspace_name

    def finish_workplace_construction(self) -> bool:
        self._ensure_subsystems()
        if self._state is SDSStateEnum.WORKPLACE_CONSTRUCTION:
            try:
                self._db_connection.create_workspace(self._workspace_name)
                self.change_workspace_context(self._workspace_name)
                self._state = SDSStateEnum.INIT_WORKPLACE
                return True
            except:
                return False

    def open_workplace(self, workplace_name: str) -> bool:
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_SYSTEM:
            # Do work here
            self._state = SDSStateEnum.INIT_WORKPLACE

    def change_workspace_context(self, workspace_name: str):
        # print('db.change_workspace called')
        self._ensure_subsystems()
        self._workspace_name = workspace_name
        self._entire_workspace_context = self._db_connection.get_workspace_context(self._workspace_name)
        # print(self._entire_workspace_context)

    ###### Project related functions ######
    def import_project(self, workspace_name: str, project: dict) -> bool:
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_WORKPLACE:
            if self._db_connection.create_project(workspace_name, project):
                self.change_workspace_context(workspace_name)
                self._state = SDSStateEnum.FILE_MANAGER_IMPORT_DIALOGUE
                return True
        return False

    def start_new_project_phase(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_WORKPLACE:
            # Do work here
            self._project_construction = {}
            self._state = SDSStateEnum.PROJECT_CONSTRUCTION

    def specify_project_name(self, project_name: str):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.PROJECT_CONSTRUCTION:
            # Do work here
            self._project_name = project_name
            if not self._project_construction:
                self._project_construction = {'_id': self._project_name, 
                    'scenario_units': []}
            else:
                self._project_construction['_id'] = self._project_name
            # State doesn't change.

    def specify_num_parrallel_units(self, n: int):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.PROJECT_CONSTRUCTION:
            # Do work here
            self._project_construction['parallel_units'] = n

    def change_project_context(self, project_name: str):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_PROJECT:
            self._project_name = project_name

    def finish_project_construction(self) -> bool:
        self._ensure_subsystems()
        if self._state is SDSStateEnum.PROJECT_CONSTRUCTION:
            # Do work here
            success = self._db_connection.create_project(self._workspace_name, 
            project=self._project_construction)
            self.change_workspace_context(self._workspace_name)
            self._state = SDSStateEnum.INIT_PROJECT
            return success

    def export_project(self, project_name: str, directory: str) -> bool:
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_PROJECT:
            try:
                data = self._db_connection.retrieve_project(project_name)
                _file = open(directory, 'w')
                #Write dictionary to json file
                print(f'exporting data: {data}')
                json.dump(data, _file)
                _file.close()
                self._state = SDSStateEnum.FILE_MANAGER_EXPORT_DIALOGUE
                return True
            except Exception as e:
                print(e)
                print('Could not save')
                return False

    ###### Enfore state function for overloading (testing) ######
    def _enforce_state(self, state: str):
        #INIT_SYSTEM = 1
        if state == 'init_system':
            self._state = SDSStateEnum.INIT_SYSTEM
        #WORKPLACE_CONSTRUCTION = 2
        if state == 'workplace_construction':
            self._state = SDSStateEnum.WORKPLACE_CONSTRUCTION
        #INIT_WORKPLACE = 3
        if state == 'init_workplace':
            self._state = SDSStateEnum.INIT_WORKPLACE
        #FILE_MANAGER_IMPORT_DIALOGUE = 4
        if state == 'file_manager_import_dialogue':
            self._state = SDSStateEnum.FILE_MANAGER_IMPORT_DIALOGUE
        #PROJECT_CONSTRUCTION = 5
        if state == 'project_construction':
            self._state = SDSStateEnum.PROJECT_CONSTRUCTION
        #INIT_PROJECT = 6
        if state == 'init_project':
            self._state = SDSStateEnum.INIT_PROJECT
        #LAUNCHING_CORE_UNITS = 7
        if state == 'launching_core_units':
            self._state = SDSStateEnum.LAUNCHING_CORE_UNITS
        #SCENARIO_UNIT_CONSTRUCTION = 8
        if state == 'scenario_unit_construction':
            self._state = SDSStateEnum.SCENARIO_UNIT_CONSTRUCTION
        #INIT_CAPTURE_NETWORK = 9
        if state == 'init_capture_network':
            self._state = SDSStateEnum.INIT_CAPTURE_NETWORK
        #NETWORK_RUNNING = 10
        if state == 'network_running':
            self._state = SDSStateEnum.NETWORK_RUNNING
        #NETWORK_STOPPED = 11
        if state == 'network_stopped':
            self._state = SDSStateEnum.NETWORK_STOPPED
        #FILE_MANAGER_EXPORT_DIALOGUE = 12
        if state == 'file_manager_export_dialogue':
            self._state = SDSStateEnum.FILE_MANAGER_EXPORT_DIALOGUE

    ###### Scenario Related Functions ######
    def add_scenario_unit(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_PROJECT:
            self._scenario_unit_construction['scenario_name'] = ''
            self._scenario_unit_construction['nodes'] = {}
            self._scenario_unit_construction['iterations'] = 1
            self._scenario_unit_construction['PCAP'] = []
            self._scenario_unit_construction['sds_vm_service'] = ''
            self._scenario_unit_construction['sds_docker_service'] = ''
            self._state = SDSStateEnum.SCENARIO_UNIT_CONSTRUCTION
        
    def insert_scenario_name(self, name: str):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.SCENARIO_UNIT_CONSTRUCTION:
            self._scenario_unit_construction['scenario_name'] = name
            
    def insert_node(self, scenario_id: str, node_id: str, listening: bool, \
        type: str, name: str, ip: str, mac: str, subnet: bool, scanning: bool, \
        username_pass: str, scanner_binary: str, arguments: str, iterations: int,\
        parallel_runs: int, end_condition: str):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_PROJECT:
            # Continue here
            # Insert scenario node
            node_dict = {}
            node_dict['id'] = node_id
            node_dict['listening'] = listening
            node_dict['type'] = type
            node_dict['name'] = name
            node_dict['ip'] = ip
            node_dict['mac'] = mac
            node_dict['subnet'] = subnet
            node_dict['scanning'] = scanning
            node_dict['username/pass'] = username_pass
            node_dict['scanner_binary'] = scanner_binary
            node_dict['arguments'] = arguments
            node_dict['iterations'] = iterations
            node_dict['parallel_runs'] = parallel_runs
            node_dict['end_condition'] = end_condition
            self._db_connection.create_node(scenario_id, node_dict)
            self.change_workspace_context(self._workspace_name)
            pass
    
    def finish_scenario_unit_construction(self, project_name: str, iterations: int):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.SCENARIO_UNIT_CONSTRUCTION:
            # Do work here
            self._scenario_unit_construction['iterations'] = iterations
            success = self._db_connection.create_scenario_unit(project_name,
            self._scenario_unit_construction)
            self.change_workspace_context(self._workspace_name)
            self._state = SDSStateEnum.INIT_PROJECT
            return success

    ###### CORE Related functinos ######
    def start_VM(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_PROJECT:
            # Do work here
            try:
                # Do launching with Capture Manager
                self._cap_manager.start_vm()
            except Exception as e:
                # Handle here
                self._state = SDSStateEnum.INIT_PROJECT
            self._state = SDSStateEnum.LAUNCHING_CORE_UNITS

    def notify_gathering_complete(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_CAPTURE_NETWORK:
            #Do work here
            pass

    def run_scenario_units(self, scenario_name: str):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_CAPTURE_NETWORK:
            # Do work here
            scenario_dict = self.get_scenario_data(scenario_name)
            self._cap_manager.start_services(scenario_dict)
            self._state = SDSStateEnum.NETWORK_RUNNING

    def stop(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.NETWORK_RUNNING:
            # Do work here
            self._cap_manager.stopVM()
            self._state = SDSStateEnum.NETWORK_STOPPED

    def restore(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.NETWORK_STOPPED:
            # Do work here
            self._cap_manager.restoreScenario()
            self._state = SDSStateEnum.NETWORK_RUNNING

    def scenarios_complete(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.NETWORK_RUNNING:
            # Do work here
            self._state = SDSStateEnum.INIT_CAPTURE_NETWORK

    def gather_data_to_DB(self):
        self._ensure_subsystems()
        pass

    #UI needs all the nodes of a scenario unit
    def get_all_nodes(self, scenario_name: str):
        self._ensure_subsystems()
        projects_list = self._entire_workspace_context['projects']
        for project_dict in projects_list:
            scenario_list = project_dict['scenario_units']
            for scenario_dict in scenario_list:
                if scenario_dict['scenario_name'] == scenario_name:
                    return scenario_dict['nodes']
    
    def get_scenario_id(self, scenario_name: str):
        self._ensure_subsystems()
        projects_list = self._entire_workspace_context['projects']
        for project_dict in projects_list:
            scenario_list = project_dict['scenario_units']
            for scenario_dict in scenario_list:
                if scenario_dict['scenario_name'] == scenario_name:
                    return scenario_dict['_id']

    def get_scenario_project_name(self, scenario_name: str):
        self._ensure_subsystems()
        projects_list = self._entire_workspace_context['projects']
        for project_dict in projects_list:
            scenario_list = project_dict['scenario_units']
            for scenario_dict in scenario_list:
                if scenario_dict['scenario_name'] == scenario_name:
                    return project_dict['_id']

    def get_scenario_vm_info(self, scenario_name: str):
        self._ensure_subsystems()
        projects_list = self._entire_workspace_context['projects']
        for project_dict in projects_list:
            scenario_list = project_dict['scenario_units']
            for scenario_dict in scenario_list:
                if scenario_dict['scenario_name'] == scenario_name:
                    return (scenario_dict['sds_vm_service'], scenario_dict['sds_docker_service'])

    def get_scenario_data(self, scenario_name: str):
        scenario_dict = {}
        scenario_dict['scenario_name'] = scenario_name
        scenario_dict['project_name'] = self.get_scenario_project_name(scenario_name)
        scenario_dict['workspace_name'] = self._entire_workspace_context['_id']
        # Seperate nodes into devices and networks.
        nodes = self.get_all_nodes(scenario_name) 
        scenario_dict['devices'] = []
        scenario_dict['networks'] = []
        for node in nodes:
            _type = node['type']
            if _type == 'PC':
                scenario_dict['devices'].append(node)
            elif _type == 'RJ45':
                scenario_dict['networks'].append(node)
        scenario_dict['core_sds_service_ip'] = self._entire_workspace_context['core_sds_service_ip']
        scenario_dict['core_sds_port_number'] = self._entire_workspace_context['core_sds_port_number']
        vm, docker = self.get_scenario_vm_info(scenario_name)
        scenario_dict['sds_vm_service'] = vm
        scenario_dict['sds_docker_service'] = docker
        return scenario_dict

    def get_core_ip(self):
        return self._entire_workspace_context['core_sds_service_ip']

    def get_core_port(self):
        return self._entire_workspace_context['core_sds_port_number']

    def insert_vm_service(self, scenario_name: str, vm_ip: str, docker_ip: str):
        scenario_id = self.get_scenario_id(scenario_name)
        self._db_connection.save_scenario_unit(scenario_id, {'sds_vm_service': vm_ip, \
            'sds_docker_service': docker_ip})
        self.change_workspace_context(self._workspace_name)

    def insert_core_sds_service(self, ip: str, port: str):
        self._db_connection.save_workspace(self._workspace_name, {'core_sds_service_ip': ip, \
            'core_sds_port_number': port})
        self.change_workspace_context(self._workspace_name)