import os
import sys
import time
import json

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTreeWidgetItem, QFileDialog, QAction

from views.addNodeWindow import Ui_addNode_window
from views.createWorkspace import Ui_newWorkspace_window
from views.databaseConfigWindow import Ui_databaseConfig_window
from views.databaseErrorWindow import Ui_databaseError_window
from views.deleteConfirmationWindow import Ui_deleteConfirmation_window
from views.mainWindow import Ui_MainWindow
from views.missingFieldsWindow import Ui_missingFields_window
from views.newProject import Ui_newProject_window
from views.newScenarioUnitWindow import Ui_newScenarioUnit_window
from views.workspace import Ui_workspace_window
from Controllers.SDSController import SDSController
from Controllers.AnalysisManager import SDSAnalysisManager
from captureController import CaptureController
from Database.DatabaseHelper import SDSDatabaseHelper


class Workspace:
    def __init__(self, name: str = '', projects: list = []):
        self.name = name
        self.projects = projects


class Project:
    def __init__(self, name: str, max_units: int, scenarios: list = []):
        self.name = name
        self.max_units = max_units
        self.scenarios = scenarios


class Scenario:
    def __init__(self, id, name, networks: list, devices: list, links: list):
        self.id = id
        self.name = name
        self.networks = networks
        self.devices = devices
        self.links = links


class Node:
    def __init__(self, id: int, listening: bool, node_type: str, name: str,
                 IP: str, port: int, MAC: str, network: int):
        self.id = id
        self.listening = listening
        self.type = node_type
        self.name = name
        self.IP = IP
        self.port = port
        self.MAC = MAC
        self.network = network


class ScannerNode(Node):
    def __init__(self, id: int, listening: bool, node_type: str, name: str, IP: str, \
        port: int, MAC: str, network: int, us_pas, scanner_binary, arguments, \
            iterations, max_parallel_runs, end_condition):
        super().__init__(id, listening, node_type, name, IP, port, MAC, network)
        self.us_pas = us_pas
        self.scanner_binary = scanner_binary
        self.arguments = arguments
        self.iterations = iterations
        self.max_parallel_runs = max_parallel_runs
        self.end_condition = end_condition


app = QtWidgets.QApplication(sys.argv)

workspace_Window = QtWidgets.QDialog()
createWorkspace_Window = QtWidgets.QDialog()
mainWindow_Window = QtWidgets.QMainWindow()
newProject_Window = QtWidgets.QDialog()
addNode_Window = QtWidgets.QDialog()
missingFields_Window = QtWidgets.QDialog()
newScenarioUnit_Window = QtWidgets.QDialog()
deleteConfirmation_Window = QtWidgets.QDialog()
databaseConfig_Window = QtWidgets.QDialog()
databaseError_Window = QtWidgets.QDialog()

workspaceUI = Ui_workspace_window()
createWorkspaceUI = Ui_newWorkspace_window()
mainWindowUI = Ui_MainWindow()
newProjectWindowUI = Ui_newProject_window()
addNodeWindowUI = Ui_addNode_window()
missingFieldsWindowUI = Ui_missingFields_window()
newScenarioUnitWindowUI = Ui_newScenarioUnit_window()
deleteConfirmationWindowUI = Ui_deleteConfirmation_window()
databaseConfigWindowUI = Ui_databaseConfig_window()
databaseErrorWindowUI = Ui_databaseError_window()

workspace_object: Workspace = Workspace()
current_workspace_name = workspace_object.name
current_project_name = ''


def createWorkspaceWindow():
    sds_controller.start_new_workplace()
    createWorkspace_Window.show()


def databaseConfigWindow():
    databaseConfig_Window.show()


# TODO: Implement connecting to the database. IP already obtained when clicked connect.
def connect_database():
    database_ip = databaseConfigWindowUI.databaseConfigIPInput_databaseConfigWindow.text()
    print(database_ip)
    # If success -> close window
    databaseConfig_Window.close()

    # TODO: When error occurs, use this commented line:
    #databaseError_Window.show()



def createWorkspace():
    # Get workspace name
    ws_name = createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text()
    # Check if valid input
    if not ws_name:
        missingFields_Window.show()
    else:
        # Insert into controller of new workspace. 
        sds_controller.specify_workplace_name(ws_name)
        workspace_injection_success: bool = sds_controller.finish_workplace_construction()
        # TODO: Based on the success, insert another window if error
        if not workspace_injection_success:
            pass
        else:
            workspace_object.name = ws_name
            mainWindow_Window.show()
            createWorkspace_Window.close()
            workspace_Window.close()


def createProjectWindow():
    sds_controller.start_new_project_phase()
    newProject_Window.show()


def newScenarioUnitWindow():
    sds_controller.add_scenario_unit()
    newScenarioUnit_Window.show()


def addNodeWindow():
    addNode_Window.show()


def deleteConfirmationWindow():
    deleteConfirmation_Window.show()


def createProject():
    project_name = newProjectWindowUI.newProjectNameInput_newProjectWindow.text()
    #print(project_name)
    project_parallel = newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.value()

    # If the input is incorrect show the missing fields window
    if not project_name or project_parallel is 0:
        missingFields_Window.show()
    # Otherwise save the project
    else:
        p = QtWidgets.QTreeWidgetItem([project_name])
        #print('creating project')
        #print(project_name)
        # Use the sds controller to save the project
        sds_controller._enfore_state('workplace_construction')
        #print('createproject showing currentworksspacename')
        #print(current_workspace_name)
        sds_controller.specify_workplace_name(current_workspace_name)
        sds_controller._enfore_state('project_construction')
        sds_controller.specify_project_name(project_name)
        sds_controller.specify_num_parrallel_units(project_parallel)
        success = sds_controller.finish_project_construction(project_name)

        #print(success)
        if not success:
            # TODO: Add a warning message
            pass
        else:
            # Adds the TreeWidgetItem to the project list
            mainWindowUI.projectsList_mainWindow.addTopLevelItem(p)

            # Resets the values for the window
            newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.setValue(0)
            newProjectWindowUI.newProjectNameInput_newProjectWindow.clear()
            newProject_Window.close()


def createScenario():
    scenario_name = newScenarioUnitWindowUI.newScenarioUnitNameInput_newScenarioUnitWindow.text()
    if not scenario_name:
        missingFields_Window.show()
    else:
        sds_controller._enfore_state('init_project')
        sds_controller.add_scenario_unit()
        sds_controller.insert_scenario_name(scenario_name)
        # TODO: This causes an error when creating a scenario.
        project_name = mainWindowUI.projectsList_mainWindow.selectedItems()[0].text(0)
        # TODO: INSERT ITERATIONS HERE
        su_iterations = mainWindowUI.scenarioIterationsSpinbox_mainWindow.value()
        success = sds_controller.finish_scenario_unit_construction(project_name, su_iterations)
        if not success:
            # TODO: Display error
            pass
        else:
            # TODO: Test this
            s = QTreeWidgetItem([scenario_name])
            p = mainWindowUI.projectsList_mainWindow.selectedItems()[0]
            p.addChild(s)
            newScenarioUnit_Window.close()


def edit_project(selected_project):
    pass


def delete_project(selected_project):
    pass


def load_scenario_unit():
    pass


def edit_scenario_unit(selected_scenario_unit):
    pass


def delete_scenario_unit(selected_scenario_unit):
    pass


def edit_node(selected_node):
    pass


def delete_node(selected_node):
    pass


def addNode():
    # TODO: Implement this
    addNode_Window.close()


def define_workspace_path():
    global workspace_path
    dialog = QFileDialog()
    workspace_path = dialog.getExistingDirectory(createWorkspace_Window, 'Select Workspace Directory')
    createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.setText(workspace_path)


def item_project_selected():
    if mainWindowUI.projectsList_mainWindow.selectedItems()[0].parent() is None:
        # TODO: Check add node button(I was not able to create a project)
        mainWindowUI.exportButton_mainWindow.setEnabled(True)
        mainWindowUI.addNodeButton_mainWindow.setEnabled(False)
        mainWindowUI.startScenarioButton_mainWindow.setEnabled(False)
        mainWindowUI.stopScenarioButton_mainWindow.setEnabled(False)
        mainWindowUI.restoreScenarioButton_mainWindow.setEnabled(False)
    else:
        mainWindowUI.exportButton_mainWindow.setEnabled(False)
        mainWindowUI.addNodeButton_mainWindow.setEnabled(True)
        mainWindowUI.startScenarioButton_mainWindow.setEnabled(True)
        mainWindowUI.stopScenarioButton_mainWindow.setEnabled(True)
        mainWindowUI.restoreScenarioButton_mainWindow.setEnabled(True)


# TODO: Work on this to work with the controller
def save_workspace():
    for project in workspace_object.projects:
        os.makedirs(os.path.join(workspace_object.location,
                                 project.name))

        for scenario in project.scenarios:
            os.makedirs(os.path.join(project.location,
                                     scenario.name))


# TODO: Fix this to work with controller.
def export_project():
    scenarios = {}
    project_name = mainWindowUI.projectsList_mainWindow.selectedItems()[0].text(0)
    project_path = ''
    # FIXME: workspace_object reference
    projects = workspace_object.projects
    for project in projects:
        if project.name == project_name:
            project_path = project.location
            for scenario in project.scenarios:
                scenarios[scenario.name] = ''
    json_project = [project_name, scenarios]
    json_string = json.dumps(json_project)
    with open(project_path + '.json', 'w') as outfile:
        outfile.write(json_string)


# TODO: Fix this to work with the controller.
def import_project():
    dialog = QFileDialog()
    json_path = dialog.getOpenFileName(mainWindow_Window, 'Select JSON File')
    with open(json_path[0]) as json_file:
        project = json.load(json_file)
        p = QtWidgets.QTreeWidgetItem([project[0]])
        for x in project[1]:
            s = QTreeWidgetItem([x])
            p.addChild(s)
        mainWindowUI.projectsList_mainWindow.addTopLevelItem(p)


def addNodeCheckboxStateChanged():
    addNodeWindowUI.addNodeButton_addNodeWindow.clicked.connect(addNode)
    addNodeWindowUI.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_Window.close)


def open_workspace(selected_workspace):
    global current_workspace_name
    current_workspace_name = selected_workspace
    time.sleep(1)
    mainWindow_Window.setWindowTitle(selected_workspace + ' - Scan Detection System')
    mainWindow_Window.show()
    workspace_Window.close()
    # Get all project names related to workspace
    project_names = sds_controller.list_all_projects(selected_workspace)
    for project_name in project_names:
        # Make TreeWidgetItem
        project_tree_item = QTreeWidgetItem([project_name])
        # Get all scenarios related to workspace and project
        scenario_names = sds_controller.list_all_scenario_units(selected_workspace, project_name)
        for scenario_name in scenario_names:
            # Make TreeWidgetItem
            scenario_tree = QTreeWidgetItem([scenario_name])
            # Add scenario tree to project tree
            project_tree_item.addChild(scenario_tree)
        mainWindowUI.projectsList_mainWindow.addTopLevelItem(project_tree_item)


# TODO: Implement this
def edit_workspace(selected_workspace):
    pass


# TODO: Implement this
def delete_workspace(selected_workspace):
    pass


# TODO: Check this call chain
def set_up_scenario_unit():
    sds_controller.set_up_scenario_units()


# TODO: Check this call chain
def start_scenario_unit():
    sds_controller.run_scenario_units()


# TODO: Check this call chain
def stop_scenario_unit():
    sds_controller.stop()


# TODO: Check this call chain
def restore_scenario_unit():
    sds_controller.restore()


def context_menu_workspace(point):
    index = workspaceUI.workspacesList_workspaceWindow.indexAt(point)
    if not index.isValid() or index.parent().isValid():
        return
    item = workspaceUI.workspacesList_workspaceWindow.itemAt(point)
    name = item.text(0)
    menu = QtWidgets.QMenu()

    action_open_workspace = QAction("Open Workspace")
    action_edit_workspace = QAction("Edit Workspace")
    action_delete_workspace = QAction("Delete Workspace")

    menu.addAction(action_open_workspace)
    menu.addAction(action_edit_workspace)
    menu.addAction(action_delete_workspace)

    action_open_workspace.triggered.connect(lambda: open_workspace(name))
    action_edit_workspace.triggered.connect(lambda: edit_workspace(name))
    action_delete_workspace.triggered.connect(lambda: delete_workspace(name))

    menu.exec_(workspaceUI.workspacesList_workspaceWindow.mapToGlobal(point))


def context_menu_project(point):
    index = mainWindowUI.projectsList_mainWindow.indexAt(point)

    if not index.isValid() or index.parent().isValid():
        item = mainWindowUI.projectsList_mainWindow.itemAt(point)
        name = item.text(0)

        menu = QtWidgets.QMenu()
        action_edit_scenario_unit = QAction("Edit Scenario Unit")
        action_delete_scenario_unit = QAction("Delete Scenario Unit")

        menu.addAction(action_edit_scenario_unit)
        menu.addAction(action_delete_scenario_unit)

        action_edit_scenario_unit.triggered.connect(lambda: edit_scenario_unit(name))
        action_delete_scenario_unit.triggered.connect(lambda: delete_scenario_unit(name))

        menu.exec_(mainWindowUI.projectsList_mainWindow.mapToGlobal(point))

        return

    if not index.isValid() or not index.parent().isValid():
        item = mainWindowUI.projectsList_mainWindow.itemAt(point)
        name = item.text(0)

        menu = QtWidgets.QMenu()
        action_add_scenario = QAction("Add Scenario Unit")
        action_load_scenario = QAction("Load Scenario Unit")
        action_edit_project = QAction("Edit Project")
        action_delete_project = QAction("Delete Project")

        menu.addAction(action_add_scenario)
        menu.addAction(action_load_scenario)
        menu.addAction(action_edit_project)
        menu.addAction(action_delete_project)

        action_add_scenario.triggered.connect(newScenarioUnitWindow)
        action_load_scenario.triggered.connect(load_scenario_unit)
        action_edit_project.triggered.connect(lambda: edit_project(name))
        action_delete_project.triggered.connect(lambda: delete_project(name))

        menu.exec_(mainWindowUI.projectsList_mainWindow.mapToGlobal(point))

        return


def context_menu_node(point):
    index = mainWindowUI.nodesList_mainWindow.indexAt(point)

    if not index.isValid() or index.parent().isValid():
        item = mainWindowUI.nodesList_mainWindow.itemAt(point)
        name = item.text(0)

        menu = QtWidgets.QMenu()
        action_edit_node = QAction("Edit Node")
        action_delete_node = QAction("Delete Node")

        menu.addAction(action_edit_node)
        menu.addAction(action_delete_node)

        action_edit_node.triggered.connect(lambda: edit_node(name))
        action_delete_node.triggered.connect(lambda: delete_node(name))

        menu.exec_(mainWindowUI.nodesList_mainWindow.mapToGlobal(point))

        return


def delete_selection():
    pass


# TODO: Store services in variables or objects.
def store_core_sds_service():
    core_sds_service = mainWindowUI.coreSdsServiceInput_mainWindow.text()
    print(core_sds_service)


def store_core_port_number():
    core_port_number = mainWindowUI.corePortNumberInput_mainWindow.text()
    print(core_port_number)


def store_sds_vm_service():
    sds_vm_service = mainWindowUI.vmSdsServiceInput_mainWindow.text()
    print(sds_vm_service)


def store_sds_docker_service():
    sds_docker_service = mainWindowUI.dockerSdsServiceInput_mainWindow.text()
    #selected_scenario = mainWindowUI.projectsList_mainWindow.selectedItems()[0].text(0)
    #print(selected_scenario)
    print(sds_docker_service)


def setup_ui():
    workspaceUI.setupWorkspaceUI(workspace_Window)
    createWorkspaceUI.setupCreateWorkspace(createWorkspace_Window)
    mainWindowUI.setupMainWindowUI(mainWindow_Window)
    newProjectWindowUI.setupNewProject(newProject_Window)
    addNodeWindowUI.setupAddNode(addNode_Window)
    missingFieldsWindowUI.setupMissingFields(missingFields_Window)
    newScenarioUnitWindowUI.setupNewScenarioUnit(newScenarioUnit_Window)
    deleteConfirmationWindowUI.setupDeleteConfirmation(deleteConfirmation_Window)
    databaseConfigWindowUI.setupDatabaseConfig(databaseConfig_Window)
    databaseErrorWindowUI.setupDatabaseError(databaseError_Window)


def initialize_signals():
    workspaceUI.createWorkspaceButton_workspaceWindow.clicked.connect(createWorkspaceWindow)
    workspaceUI.dbConfigButton_workspaceWindow.clicked.connect(databaseConfigWindow)
    #workspaceUI.analysisManagerButton_workspaceWindow.clicked.connect(analysisManagerWindow)
    #workspaceUI.dbConfigButton_workspaceWindow.clicked.connect(databaseConfigurationWindow)
    workspaceUI.workspacesList_workspaceWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    workspaceUI.workspacesList_workspaceWindow.customContextMenuRequested.connect(context_menu_workspace)

    createWorkspaceUI.createWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace)
    createWorkspaceUI.cancelWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace_Window.close)
    createWorkspaceUI.browseWorkspaceButton_newWorkspaceWindow.clicked.connect(define_workspace_path)

    mainWindowUI.newButton_mainWindow.clicked.connect(createProjectWindow)
    mainWindowUI.projectsList_mainWindow.itemSelectionChanged.connect(item_project_selected)
    mainWindowUI.saveButton_mainWindow.clicked.connect(save_workspace)
    mainWindowUI.exportButton_mainWindow.clicked.connect(export_project)
    mainWindowUI.importButton_mainWindow.clicked.connect(import_project)
    mainWindowUI.addNodeButton_mainWindow.clicked.connect(addNodeWindow)
    mainWindowUI.startScenarioButton_mainWindow.clicked.connect(start_scenario_unit)
    mainWindowUI.stopScenarioButton_mainWindow.clicked.connect(stop_scenario_unit)
    mainWindowUI.restoreScenarioButton_mainWindow.clicked.connect(restore_scenario_unit)
    mainWindowUI.projectsList_mainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    mainWindowUI.projectsList_mainWindow.customContextMenuRequested.connect(context_menu_project)
    mainWindowUI.nodesList_mainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    mainWindowUI.nodesList_mainWindow.customContextMenuRequested.connect(context_menu_node)

    mainWindowUI.coreSdsServiceInput_mainWindow.textChanged[str].connect(store_core_sds_service)
    mainWindowUI.corePortNumberInput_mainWindow.textChanged[str].connect(store_core_port_number)
    mainWindowUI.vmSdsServiceInput_mainWindow.textChanged[str].connect(store_sds_vm_service)
    mainWindowUI.dockerSdsServiceInput_mainWindow.textChanged[str].connect(store_sds_docker_service)

    newProjectWindowUI.newProjectCreateButton_newProjectWindow.clicked.connect(createProject)
    newProjectWindowUI.newProjectCancelButton_newProjectWindow.clicked.connect(newProject_Window.close)

    newScenarioUnitWindowUI.newScenarioUnitCreateButton_newScenarioUnitWindow.clicked.connect(createScenario)
    newScenarioUnitWindowUI.newScenarioUnitCancelButton_newScenarioUnitWindow.clicked.connect(
        newScenarioUnit_Window.close)

    addNodeWindowUI.addNodeButton_addNodeWindow.clicked.connect(addNode)
    addNodeWindowUI.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_Window.close)

    addNodeWindowUI.nodeScannerNodeCheckBox_addNodeWindow.toggled.connect(addNodeCheckboxStateChanged)

    missingFieldsWindowUI.missingFieldsCloseButton_missingFieldsWindow.clicked.connect(missingFields_Window.close)

    deleteConfirmationWindowUI.deleteConfirmationButton_deleteConfirmationWindow.clicked.connect(
        delete_selection)
    deleteConfirmationWindowUI.cancelConfirmationButton_deleteConfirmationWindow.clicked.connect(
        deleteConfirmation_Window.close)

    databaseConfigWindowUI.databaseConfigIPConnectButton_databaseConfigWindow.clicked.connect(connect_database)
    databaseConfigWindowUI.databaseConfigIPCancelButton_databaseConfigWindow.clicked.connect(
        databaseConfig_Window.close)

    databaseErrorWindowUI.databaseErrorCloseButton_databaseErrorWindow.clicked.connect(databaseError_Window.close)

def generate_workspaces_list_window():
    workspaces_c = sds_controller.list_all_workplaces()
    if workspaces_c:
        for workspace_c in workspaces_c:
            l1 = QtWidgets.QTreeWidgetItem([workspace_c])
            workspaceUI.workspacesList_workspaceWindow.addTopLevelItem(l1)

def set_up_database_connection():
    database_ip_dict: dict = {}
    ip_port = ''
    with open('conf/db_config.json') as mongo_ip_file:
        database_ip_dict = json.load(mongo_ip_file)
        ip = database_ip_dict['ip']
        port = database_ip_dict['port']
        ip_port = f'{ip}:{port}'
    # For future context that db doesn't connect
    try:
        db = SDSDatabaseHelper(ip_port)
        return (SDSDatabaseHelper(ip_port), True)
    except:
        return (None, False)

setup_ui()

initialize_signals()

sds_controller = None

#First check the mongodb connection
mongo_connection, db_connection_success = set_up_database_connection()

if db_connection_success:
    sds_controller = SDSController()
    sds_controller.add_mongo_connection(mongo_connection)
    sds_controller.add_capture_manager(CaptureController())
    sds_controller.add_analysis_manager(SDSAnalysisManager())
    # sds controller implementation for filling workspaces
    generate_workspaces_list_window()

else:
    print(f'enters else fail db_connection_success')
    databaseConfigWindow()
    databaseError_Window.show()
    pass

workspace_Window.show()

sys.exit(app.exec_())
