from enum import Enum, unique
import json
from msilib.schema import Error
import re
from typing import List
from Database.DatabaseHelper import SDSDatabaseHelper

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
        self._cap_manager = None
        self._a_manager = None
        self._db_connection: SDSDatabaseHelper = None 
        self._state = SDSStateEnum.INIT_SYSTEM
        self._worklace_name: str = ''
        self._project_name: str = ''
        self._project_construction: dict = {}

    def add_capture_manager(self, capture_manager):
        if self._cap_manager == None:
            self._cap_manager = capture_manager

    def add_analysis_manager(self, analysis_manager):
        if self._a_manager == None:
            self._a_manager = analysis_manager
    
    def add_mongo_connection(self, connection):
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
            return self._db_connection.retrieve_projects(workplace_name)

    def list_all_scenario_units(self, workplace_name: str, project_name: str) -> List[str]:
        #Gets all scenario_units of specified instance
        if self._db_connection is None:
            return []
        else:
            #Do work here
            pass

    def list_all_nodes(self, workplace_name: str, project_name: str, 
        scenario_unit_id: str) -> List[str]:
        if self._db_connection is None:
            return []
        else:
            #Do work here
            pass

    def start_new_workplace(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_SYSTEM:
            # Do work here
            self._state = SDSStateEnum.WORKPLACE_CONSTRUCTION

    def specify_workplace_name(self, workspace_name: str):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.WORKPLACE_CONSTRUCTION:
            self._worklace_name = workspace_name

    def finish_workplace_construction(self) -> bool:
        self._ensure_subsystems()
        if self._state is SDSStateEnum.WORKPLACE_CONSTRUCTION:
            try:
                self._db_connection.create_workspace(self._worklace_name)
                self._state = SDSStateEnum.INIT_WORKPLACE
                return True
            except:
                return False

    def open_workplace(self, workplace_name: str) -> bool:
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_SYSTEM:
            # Do work here
            self._state = SDSStateEnum.INIT_WORKPLACE

    def import_project(self, workspace_name: str, project: dict) -> bool:
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_WORKPLACE:
            if self._db_connection.create_project(workspace_name, project):
                self._state = SDSStateEnum.FILE_MANAGER_IMPORT_DIALOGUE
                return True
        return False

    def start_new_project_phase(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_WORKPLACE:
            # Do work here
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

    def finish_project_construction(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.PROJECT_CONSTRUCTION:
            # Do work here
            self._db_connection.create_project(self._worklace_name, self._project_construction)
            self._state = SDSStateEnum.INIT_PROJECT

    def export_project(self, project_name: str, directory: str) -> bool:
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_PROJECT:
            try:
                data = self._db_connection.retrieve_project(project_name)
                _file = open(directory, 'w')
                #Write dictionary to json file
                json.dump(data, _file)
                self._state = SDSStateEnum.FILE_MANAGER_EXPORT_DIALOGUE
                return True
            except:
                print('Could not save')
                return False

    def add_scenario_unit(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_PROJECT:
            # Do work here
            self._state = SDSStateEnum.SCENARIO_UNIT_CONSTRUCTION
    
    def finish_scenario_unit_construction(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.SCENARIO_UNIT_CONSTRUCTION:
            # Do work here
            self._state = SDSStateEnum.INIT_PROJECT

    def set_up_scenario_units(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_PROJECT:
            # Do work here
            try:
                # Do launching with Capture Manager
                pass
            except Error as e:
                # Handle here
                self._state = SDSStateEnum.INIT_PROJECT
            self._state = SDSStateEnum.LAUNCHING_CORE_UNITS

    def notify_gathering_complete(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_CAPTURE_NETWORK:
            #Do work here
            pass

    def run_scenario_units(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_CAPTURE_NETWORK:
            # Do work here
            self._state = SDSStateEnum.NETWORK_RUNNING

    def stop(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.NETWORK_RUNNING:
            # Do work here
            self._state = SDSStateEnum.NETWORK_STOPPED

    def restore(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.NETWORK_STOPPED:
            # Do work here
            self._state = SDSStateEnum.NETWORK_RUNNING

    def scenarios_complete(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.NETWORK_RUNNING:
            # Do work here
            self._state = SDSStateEnum.INIT_CAPTURE_NETWORK

    def gather_data_to_DB(self):
        self._ensure_subsystems()
        pass

    '''The following methods are developed by the protocols by the GUI Lead
    Mauricio.'''