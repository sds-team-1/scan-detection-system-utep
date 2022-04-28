<<<<<<< HEAD
# Imports
import os
=======
>>>>>>> 6d72ead37dacf87e2e6e0a5fffb4f651d42e1ebd
import sys
from PyQt5 import QtWidgets

from Database.databaseFunctions import connect_subsystems_and_database, set_up_database_connection
from Models.modelClasses import Workspace
from views.databaseConfigWindow import Ui_databaseConfig_window
from views.deleteConfirmationWindow import Ui_deleteConfirmation_window
from views.workspace import Ui_workspace_window
from Controllers.SDSController import SDSController
<<<<<<< HEAD
from Controllers.AnalysisManager import SDSAnalysisManager
from Controllers.CaptureController import CaptureController
from Database.DatabaseHelper import SDSDatabaseHelper

from Controllers.SDSController import SDSController
from Database.DatabaseHelper import SDSDatabaseHelper
from Controllers.AnalysisManager import SDSAnalysisManager


################ CLASSES ################
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

################ END CLASSES ################
=======
>>>>>>> 6d72ead37dacf87e2e6e0a5fffb4f651d42e1ebd

app = QtWidgets.QApplication(sys.argv)
workspace_Window = QtWidgets.QDialog()
deleteConfirmation_Window = QtWidgets.QDialog()
databaseConfig_Window = QtWidgets.QDialog()
databaseError_Window = QtWidgets.QDialog()

workspaceUI = Ui_workspace_window()
deleteConfirmationWindowUI = Ui_deleteConfirmation_window()
databaseConfigWindowUI = Ui_databaseConfig_window()

workspace_object: Workspace = Workspace()

sds_controller = SDSController()


def deleteConfirmationWindow():
    global deleteConfirmation_Window
    deleteConfirmation_Window = QtWidgets.QDialog()
    deleteConfirmationWindowUI.setupDeleteConfirmation(deleteConfirmation_Window)
    deleteConfirmationWindowUI.deleteConfirmationButton_deleteConfirmationWindow.clicked.connect(
        delete_selection)
    deleteConfirmationWindowUI.cancelConfirmationButton_deleteConfirmationWindow.clicked.connect(
        deleteConfirmation_Window.close)
    deleteConfirmation_Window.show()


<<<<<<< HEAD
def createProject():
    project_name = newProjectWindowUI.newProjectNameInput_newProjectWindow.text()
    # print(project_name)
    project_parallel = newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.value()

    # If the input is incorrect show the missing fields window
    if not project_name or project_parallel is 0:
        missingFields_Window.show()
    # Otherwise save the project
    else:
        p = QtWidgets.QTreeWidgetItem([project_name])
        # print('creating project')
        # print(project_name)
        # Use the sds controller to save the project
        sds_controller._enforce_state('workplace_construction')
        # print('createproject showing currentworksspacename')
        # print(current_workspace_name)
        sds_controller.specify_workplace_name(current_workspace_name)
        sds_controller._enforce_state('project_construction')
        sds_controller.specify_project_name(project_name)
        sds_controller.specify_num_parrallel_units(project_parallel)
        success = sds_controller.finish_project_construction()

        # print(success)
        if not success:
            # TODO: Add a warning message
            pass
        else:
            # Adds the TreeWidgetItem to the project list
            captureManagerWindowUI.projectsList_captureManagerWindow.addTopLevelItem(p)

            # Resets the values for the window
            newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.setValue(0)
            newProjectWindowUI.newProjectNameInput_newProjectWindow.clear()
            newProject_Window.close()


def createScenario():
    scenario_name = newScenarioUnitWindowUI.newScenarioUnitNameInput_newScenarioUnitWindow.text()
    if not scenario_name:
        missingFields_Window.show()
    else:
        sds_controller._enforce_state('init_project')
        sds_controller.add_scenario_unit()
        sds_controller.insert_scenario_name(scenario_name)
        # TODO: This causes an error when creating a scenario.
        project_name = captureManagerWindowUI.projectsList_captureManagerWindow.selectedItems()[0].text(0)
        # TODO: INSERT ITERATIONS HERE
        su_iterations = captureManagerWindowUI.scenarioIterationsSpinbox_captureManagerWindow.value()
        success = sds_controller.finish_scenario_unit_construction(project_name, su_iterations)
        if not success:
            # TODO: Display error
            pass
        else:
            # TODO: Test this
            s = QTreeWidgetItem([scenario_name])
            p = captureManagerWindowUI.projectsList_captureManagerWindow.selectedItems()[0]
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
    subnet = '0'
    log = ''
    if addNodeWindowUI.nodeLogNetNodeCheckBox_addNodeWindow.isChecked():
        log = 'True'
    else:
        log = 'False'
    type = addNodeWindowUI.nodeTypeComboBox_addNodeWindow.currentText()
    if type == 'CORE':
        type = 'PC'
    elif type == 'VM' or type == 'Docker':
        type = 'RJ45'
    name = addNodeWindowUI.nodeNameInput_addNodeWindow.text()
    MAC = addNodeWindowUI.nodeMACAddressInput_addNodeWindow.text()
    IP = addNodeWindowUI.nodeIPAddressInput_addNodeWindow.text()
    subnet = addNodeWindowUI.nodeSeparateSubNetNodeCheckBox_addNodeWindow.isChecked()
    user_pw = ''
    scanner_bin = ''
    arguments = ''
    num_iterations = 1
    max_parallel_runs = 1
    end_condition = ''
    scanning = addNodeWindowUI.nodeScannerNodeCheckBox_addNodeWindow.isChecked()
    if scanning:
        user_pw = addNodeWindowUI.nodeUserPassInput_addNodeWindow.text()
        scanner_bin = addNodeWindowUI.nodeScannerBinaryInput_addNodeWindow.text()
        arguments = addNodeWindowUI.nodeArgumentsInput_addNodeWindow.text()
        num_iterations = addNodeWindowUI.nodeNumIterationsSpinBox_addNodeWindow.value()
        max_parallel_runs = addNodeWindowUI.nodeMaxParallelRunsSpinBox_addNodeWindow.value()
        if addNodeWindowUI.nodeEndConditionCombobox_addNodeWindow.currentText() == 'on-scan-complete':
            end_condition = 'on-scan-complete'
        else:
            # TODO: Handle minutes and seconds.
            minutes = str(addNodeWindowUI.minutesSpinbox_addNodeWindow.value())
            seconds = str(addNodeWindowUI.secondsSpinbox_addNodeWindow.value())
            end_condition = f'time-{minutes}:{seconds}'
        toolButton = QtWidgets.QToolButton(captureManagerWindowUI.CentralLayout_captureManagerWindow)
        toolButton.setText('Scanner')
        #node_item = QTreeWidgetItem([subnet, log, type, name, MAC, IP])
        #captureManagerWindowUI.nodesList_captureManagerWindow.addTopLevelItem(node_item)
        #captureManagerWindowUI.nodesList_captureManagerWindow.setItemWidget(node_item, 6, toolButton)
    scenario_name = captureManagerWindowUI.projectsList_captureManagerWindow.selectedItems()[0].text(0)
    scenario_id = sds_controller.get_scenario_id(scenario_name)
    nodes_list = sds_controller.get_all_nodes(scenario_name)
    node_id = len(nodes_list)
    sds_controller.insert_node(scenario_id, node_id, log, type, name, IP, MAC, \
        subnet, scanning, user_pw, scanner_bin, arguments, int(num_iterations), \
        max_parallel_runs, end_condition)
    nodes_list = sds_controller.get_all_nodes(scenario_name)
    captureManagerWindowUI.nodesList_captureManagerWindow.clear()
    for node in nodes_list:
        node_item = QTreeWidgetItem([str(node['subnet']), str(node['listening']), \
            node['type'], node['name'], node['mac'], node['ip'], str(node['scanning'])])
        captureManagerWindowUI.nodesList_captureManagerWindow.addTopLevelItem(node_item)
    addNode_Window.close()


# TODO: To be implemented
def addSetNodes():
    pass


def define_workspace_path():
    global workspace_path
    dialog = QFileDialog()
    workspace_path = dialog.getExistingDirectory(createWorkspace_Window, 'Select Workspace Directory')
    createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.setText(workspace_path)

def item_project_selected():
    # print(f'checking if item_project_selected went inside')
    # Clear the window
    captureManagerWindowUI.nodesList_captureManagerWindow.clear()
    if captureManagerWindowUI.projectsList_captureManagerWindow.selectedItems()[0].parent() is None:
        # This condition is for projects. Works with the project list which...
        # contains projects and scenarios
        # TODO: Check add node button(I was not able to create a project)
        captureManagerWindowUI.exportButton_captureManagerWindow.setEnabled(True)
        captureManagerWindowUI.addNodeButton_captureManagerWindow.setEnabled(False)
        captureManagerWindowUI.addSetNodeButton_captureManagerWindow.setEnabled(False)
        captureManagerWindowUI.startScenarioButton_captureManagerWindow.setEnabled(False)
        captureManagerWindowUI.stopScenarioButton_captureManagerWindow.setEnabled(False)
        captureManagerWindowUI.restoreScenarioButton_captureManagerWindow.setEnabled(False)
    else:
        #print(f'checking if else checked')
        captureManagerWindowUI.exportButton_captureManagerWindow.setEnabled(False)
        captureManagerWindowUI.addNodeButton_captureManagerWindow.setEnabled(True)
        captureManagerWindowUI.addSetNodeButton_captureManagerWindow.setEnabled(True)
        captureManagerWindowUI.startScenarioButton_captureManagerWindow.setEnabled(True)
        captureManagerWindowUI.stopScenarioButton_captureManagerWindow.setEnabled(True)
        captureManagerWindowUI.restoreScenarioButton_captureManagerWindow.setEnabled(True)
        # Get all the nodes
        scenario_ID = captureManagerWindowUI.projectsList_captureManagerWindow.selectedItems()[0].text(0)
        #print(f'checking scenario id: {scenario_ID}')
        sds_controller._enforce_state('init_project')
        node_list = sds_controller.get_all_nodes(scenario_ID)
        # Insert into vm and docker text saved values
        vm_ip, docker_ip = sds_controller.get_scenario_vm_info(scenario_ID)
        captureManagerWindowUI.vmSdsServiceInput_captureManagerWindow.setText(vm_ip)
        captureManagerWindowUI.dockerSdsServiceInput_captureManagerWindow.setText(docker_ip)
        #print(f'checking if nodes list is anything: {node_list}')
        # Insert all the nodes into the UI
        if node_list:
            #print(f'checking if nodes list is available for ui...{node_list}')
            for node in node_list:
                node_item = QTreeWidgetItem([str(node['subnet']), str(node['listening']), \
                    node['type'], node['name'], node['mac'], node['ip'], str(node['scanning'])])
                captureManagerWindowUI.nodesList_captureManagerWindow.addTopLevelItem(node_item)
                # TODO: Ask mauricio how this works
                # captureManagerWindowUI.nodesList_captureManagerWindow.setItemWidget(node_item, 6, toolButton)


# TODO: Work on this to work with the controller
def save_workspace():
    for project in workspace_object.projects:
        # first check if the directory exists, if it does delete it
        if os.path.exists(workspace_object.location + "/" + project.name):
            os.removedirs(workspace_object.location + "/" + project.name)

        os.makedirs(workspace_object.location + "/" + project.name)

        for scenario in project.scenarios:
            os.makedirs(workspace_object.location + "/" + project.name + "/" + scenario.name)

# TODO: Fix this to work with controller.
def export_project():
    scenarios = {}
    project_name = captureManagerWindowUI.projectsList_captureManagerWindow.selectedItems()[0].text(0)
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
    json_path = dialog.getOpenFileName(captureManager_Window, 'Select JSON File')
    with open(json_path[0]) as json_file:
        project = json.load(json_file)
        p = QtWidgets.QTreeWidgetItem([project[0]])
        for x in project[1]:
            s = QTreeWidgetItem([x])
            p.addChild(s)
        captureManagerWindowUI.projectsList_captureManagerWindow.addTopLevelItem(p)


def addNodeCheckboxStateChanged():
    addNodeWindowUI.addNodeButton_addNodeWindow.clicked.connect(addNode)
    addNodeWindowUI.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_Window.close)

def open_workspace(selected_workspace):
    global current_workspace_name
    current_workspace_name = selected_workspace
    # Change sds_controller workspace context
    print(f'check if open_workspace is called')
    sds_controller.change_workspace_context(current_workspace_name)
    time.sleep(1)
    captureManager_Window.setWindowTitle(selected_workspace + ' - Scan Detection System')
    captureManager_Window.show()
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
        captureManagerWindowUI.projectsList_captureManagerWindow.addTopLevelItem(project_tree_item)
    #Insert core options if saved
#    captureManagerWindowUI.corePortNumberInput_captureManagerWindow.setText(sds_controller.get_core_port())
 #   captureManagerWindowUI.coreSdsServiceInput_captureManagerWindow.setText(sds_controller.get_core_ip())


# TODO: Implement this
def edit_workspace(selected_workspace):
    pass


# TODO: Implement this
def delete_workspace(selected_workspace):
    pass


def set_up_scenario_unit():
    sds_controller._enforce_state('init_capture_network')
    scenario_name = captureManagerWindowUI.projectsList_captureManagerWindow.selectedItems()[0].text(0)
    vm_ip = captureManagerWindowUI.vmSdsServiceInput_captureManagerWindow.text()
    docker_ip = captureManagerWindowUI.dockerSdsServiceInput_captureManagerWindow.text()
    sds_controller.insert_vm_service(scenario_name, vm_ip, docker_ip)
    captureManagerWindowUI.vmSdsServiceInput_captureManagerWindow.setEnabled(False)
    captureManagerWindowUI.dockerSdsServiceInput_captureManagerWindow.setEnabled(False)
    captureManagerWindowUI.runScenarioButton_captureManagerWindow.setEnabled(False)
    sds_controller.run_scenario_units(scenario_name)

def start_scenario_unit():
    # Get input
    ip = captureManagerWindowUI.coreSdsServiceInput_captureManagerWindow.text()
    port = captureManagerWindowUI.corePortNumberInput_captureManagerWindow.text()
    # store input into workspace
    sds_controller.insert_core_sds_service(ip, port)
    captureManagerWindowUI.corePortNumberInput_captureManagerWindow.setEnabled(False)
    captureManagerWindowUI.coreSdsServiceInput_captureManagerWindow.setEnabled(False)
    sds_controller.start_VM()
    captureManagerWindowUI.runScenarioButton_captureManagerWindow.setEnabled(True)
    captureManagerWindowUI.startScenarioButton_captureManagerWindow.setEnabled(False)

def stop_scenario_unit():
    #sds_controller.stop()
    captureManagerWindowUI.vmSdsServiceInput_captureManagerWindow.setEnabled(True)
    captureManagerWindowUI.dockerSdsServiceInput_captureManagerWindow.setEnabled(True)
    captureManagerWindowUI.runScenarioButton_captureManagerWindow.setEnabled(True)

def restore_scenario_unit():
    #sds_controller.restore()
    pass

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
    index = captureManagerWindowUI.projectsList_captureManagerWindow.indexAt(point)

    if not index.isValid() or index.parent().isValid():
        item = captureManagerWindowUI.projectsList_captureManagerWindow.itemAt(point)
        name = item.text(0)

        menu = QtWidgets.QMenu()
        action_edit_scenario_unit = QAction("Edit Scenario Unit")
        action_delete_scenario_unit = QAction("Delete Scenario Unit")

        menu.addAction(action_edit_scenario_unit)
        menu.addAction(action_delete_scenario_unit)

        action_edit_scenario_unit.triggered.connect(lambda: edit_scenario_unit(name))
        action_delete_scenario_unit.triggered.connect(lambda: delete_scenario_unit(name))

        menu.exec_(captureManagerWindowUI.projectsList_captureManagerWindow.mapToGlobal(point))

        return

    if not index.isValid() or not index.parent().isValid():
        item = captureManagerWindowUI.projectsList_captureManagerWindow.itemAt(point)
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

        menu.exec_(captureManagerWindowUI.projectsList_captureManagerWindow.mapToGlobal(point))

        return


def context_menu_node(point):
    index = captureManagerWindowUI.nodesList_captureManagerWindow.indexAt(point)

    if not index.isValid() or index.parent().isValid():
        item = captureManagerWindowUI.nodesList_captureManagerWindow.itemAt(point)
        name = item.text(0)

        menu = QtWidgets.QMenu()
        action_edit_node = QAction("Edit Node")
        action_delete_node = QAction("Delete Node")

        menu.addAction(action_edit_node)
        menu.addAction(action_delete_node)

        action_edit_node.triggered.connect(lambda: edit_node(name))
        action_delete_node.triggered.connect(lambda: delete_node(name))

        menu.exec_(captureManagerWindowUI.nodesList_captureManagerWindow.mapToGlobal(point))

        return


=======
>>>>>>> 6d72ead37dacf87e2e6e0a5fffb4f651d42e1ebd
def delete_selection():
    pass


<<<<<<< HEAD
# TODO: Store services in variables or objects.
def store_core_sds_service():
    core_sds_service = captureManagerWindowUI.coreSdsServiceInput_captureManagerWindow.text()
    print(core_sds_service)


def store_core_port_number():
    core_port_number = captureManagerWindowUI.corePortNumberInput_captureManagerWindow.text()
    print(core_port_number)


def store_sds_vm_service():
    sds_vm_service = captureManagerWindowUI.vmSdsServiceInput_captureManagerWindow.text()
    print(sds_vm_service)


def store_sds_docker_service():
    sds_docker_service = captureManagerWindowUI.dockerSdsServiceInput_captureManagerWindow.text()
    # selected_scenario = captureManagerWindowUI.projectsList_captureManagerWindow.selectedItems()[0].text(0)
    # print(selected_scenario)
    print(sds_docker_service)


def setup_ui():
    workspaceUI.setupWorkspaceUI(workspace_Window)
    captureManagerWindowUI.setupCaptureManager(captureManager_Window)
    missingFieldsWindowUI.setupMissingFields(missingFields_Window)
    databaseErrorWindowUI.setupDatabaseError(databaseError_Window)


def initialize_signals():
    workspaceUI.createWorkspaceButton_workspaceWindow.clicked.connect(createWorkspaceWindow)
    workspaceUI.dbConfigButton_workspaceWindow.clicked.connect(databaseConfigWindow)
    workspaceUI.analysisManagerButton_workspaceWindow.clicked.connect(analysisManagerWindow)
    # workspaceUI.analysisManagerButton_workspaceWindow.clicked.connect(analysisManagerWindow)
    # workspaceUI.dbConfigButton_workspaceWindow.clicked.connect(databaseConfigurationWindow)
    workspaceUI.workspacesList_workspaceWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    workspaceUI.workspacesList_workspaceWindow.customContextMenuRequested.connect(context_menu_workspace)

    captureManagerWindowUI.newButton_captureManagerWindow.clicked.connect(createProjectWindow)
    captureManagerWindowUI.projectsList_captureManagerWindow.itemSelectionChanged.connect(item_project_selected)
    captureManagerWindowUI.saveButton_captureManagerWindow.clicked.connect(save_workspace)
    captureManagerWindowUI.exportButton_captureManagerWindow.clicked.connect(export_project)
    captureManagerWindowUI.importButton_captureManagerWindow.clicked.connect(import_project)
    captureManagerWindowUI.addNodeButton_captureManagerWindow.clicked.connect(addNodeWindow)
    captureManagerWindowUI.startScenarioButton_captureManagerWindow.clicked.connect(start_scenario_unit)
    captureManagerWindowUI.runScenarioButton_captureManagerWindow.clicked.connect(set_up_scenario_unit)
    captureManagerWindowUI.stopScenarioButton_captureManagerWindow.clicked.connect(stop_scenario_unit)
    captureManagerWindowUI.restoreScenarioButton_captureManagerWindow.clicked.connect(restore_scenario_unit)
    captureManagerWindowUI.projectsList_captureManagerWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    captureManagerWindowUI.projectsList_captureManagerWindow.customContextMenuRequested.connect(context_menu_project)
    captureManagerWindowUI.nodesList_captureManagerWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    captureManagerWindowUI.nodesList_captureManagerWindow.customContextMenuRequested.connect(context_menu_node)
    captureManagerWindowUI.addSetNodeButton_captureManagerWindow.clicked.connect(addSetNodesWindow)

    #captureManagerWindowUI.coreSdsServiceInput_captureManagerWindow.textChanged[str].connect(store_core_sds_service)
    #captureManagerWindowUI.corePortNumberInput_captureManagerWindow.textChanged[str].connect(store_core_port_number)
    #captureManagerWindowUI.vmSdsServiceInput_captureManagerWindow.textChanged[str].connect(store_sds_vm_service)
    #captureManagerWindowUI.dockerSdsServiceInput_captureManagerWindow.textChanged[str].connect(store_sds_docker_service)

    missingFieldsWindowUI.missingFieldsCloseButton_missingFieldsWindow.clicked.connect(missingFields_Window.close)

    databaseErrorWindowUI.databaseErrorCloseButton_databaseErrorWindow.clicked.connect(databaseError_Window.close)


def generate_workspaces_list_window():
    workspaceUI.workspacesList_workspaceWindow.clear()
    workspaces_c = sds_controller.list_all_workplaces()
    if workspaces_c:
        for workspace_ in workspaces_c:
            l1 = QtWidgets.QTreeWidgetItem([workspace_])
            workspaceUI.workspacesList_workspaceWindow.addTopLevelItem(l1)


def set_up_database_connection():
    database_ip_dict: dict = {}
    ip_port = ''
    with open('conf/db_config.json') as mongo_ip_file:
        database_ip_dict = json.load(mongo_ip_file)
        protocol = database_ip_dict['protocol']
        ip = database_ip_dict['ip']
        port = database_ip_dict['port']
        ip_port = f'{protocol}{ip}:{port}'
    try:
        db = SDSDatabaseHelper(ip_port)
        print(f'connection worked {db}')
        return db, True
    except:
        return None, False


=======
>>>>>>> 6d72ead37dacf87e2e6e0a5fffb4f651d42e1ebd
def assert_database_connection():
    global sds_controller, mongo_connection
    mongo_connection, db_connection_success = set_up_database_connection()

    if db_connection_success:
        connect_subsystems_and_database(workspaceUI.workspacesList_workspaceWindow, sds_controller, mongo_connection)
        workspace_Window.show()
    else:
        workspace_Window.show()
        databaseError_Window.show()


workspaceUI.setupWorkspaceUI(workspace_Window, sds_controller)

assert_database_connection()

sys.exit(app.exec_())
