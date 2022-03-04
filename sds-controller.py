from enum import Enum, unique
from msilib.schema import Error
from Helpers.DatabaseHelper import SDSDatabaseHelper

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

    def __init__(self) -> None:
        self._cap_manager = None
        self._a_manager = None
        self._db_connection = None 
        self._state = SDSStateEnum.INIT_SYSTEM

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
        assert(self._cap_manager)
        assert(self._a_manager)
        assert(self._db_connection)

    ''' The following methods are made by synthesizing a state diagram for the 
    project.'''
    def start_new_workplace(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_SYSTEM:
            # Do work here
            self._state = SDSStateEnum.WORKPLACE_CONSTRUCTION

    def specify_directory(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.WORKPLACE_CONSTRUCTION:
            # Do Work here
            self._state = SDSStateEnum.INIT_WORKPLACE

    def open_workplace(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_SYSTEM:
            # Do work here
            self._state = SDSStateEnum.INIT_WORKPLACE

    def import_project(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_WORKPLACE:
            # Do work here
            self._state = SDSStateEnum.FILE_MANAGER_IMPORT_DIALOGUE

    def add_new_project(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_WORKPLACE:
            # Do work here
            self._state = SDSStateEnum.PROJECT_CONSTRUCTION

    def specify_project_name(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.PROJECT_CONSTRUCTION:
            # Do work here
            # State doesn't change.
            pass

    def specify_num_parrallel_units(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.PROJECT_CONSTRUCTION:
            # Do work here
            # State doesn't change
            pass

    def finish_project_construction(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.PROJECT_CONSTRUCTION:
            # Do work here
            self._state = SDSStateEnum.INIT_PROJECT

    def export_project(self):
        self._ensure_subsystems()
        if self._state is SDSStateEnum.INIT_PROJECT:
            # Do work here
            self._state = SDSStateEnum.FILE_MANAGER_EXPORT_DIALOGUE

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