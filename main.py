import os
import sys
import time
import json
import uuid

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTreeWidgetItem, QFileDialog, QAction

from views.addNodeWindow import Ui_addNode_window
from views.analysisManagerWindow import Ui_AnalysisManagerWindow
from views.createWorkspace import Ui_newWorkspace_window
from views.databaseConfigWindow import Ui_databaseConfig_window
from views.databaseErrorWindow import Ui_databaseError_window
from views.deleteConfirmationWindow import Ui_deleteConfirmation_window
from views.captureManagerWindow import Ui_CaptureManagerWindow
from views.missingFieldsWindow import Ui_missingFields_window
from views.newProject import Ui_newProject_window
from views.newScenarioUnitWindow import Ui_newScenarioUnit_window
from views.setNodesWindow import Ui_addSetNodes_window
from views.workspace import Ui_workspace_window
from Controllers.SDSController import SDSController
from Controllers.AnalysisManager import SDSAnalysisManager
from Controllers.CaptureController import CaptureController
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
captureManager_Window = QtWidgets.QMainWindow()
analysisManager_Window = QtWidgets.QMainWindow()
newProject_Window = QtWidgets.QDialog()
addNode_Window = QtWidgets.QDialog()
addSetNodes_Window = QtWidgets.QDialog()
missingFields_Window = QtWidgets.QDialog()
newScenarioUnit_Window = QtWidgets.QDialog()
deleteConfirmation_Window = QtWidgets.QDialog()
databaseConfig_Window = QtWidgets.QDialog()
databaseError_Window = QtWidgets.QDialog()

workspaceUI = Ui_workspace_window()
createWorkspaceUI = Ui_newWorkspace_window()
captureManagerWindowUI = Ui_CaptureManagerWindow()
analysisManagerWindowUI = Ui_AnalysisManagerWindow()
newProjectWindowUI = Ui_newProject_window()
addNodeWindowUI = Ui_addNode_window()
addSetNodesWindowUI = Ui_addSetNodes_window()
missingFieldsWindowUI = Ui_missingFields_window()
newScenarioUnitWindowUI = Ui_newScenarioUnit_window()
deleteConfirmationWindowUI = Ui_deleteConfirmation_window()
databaseConfigWindowUI = Ui_databaseConfig_window()
databaseErrorWindowUI = Ui_databaseError_window()

workspace_object: Workspace = Workspace()
current_workspace_name = workspace_object.name
current_project_name = ''

sds_controller = SDSController()
db_config_filename = 'conf/db_config.json'

ip_counter = 0
id_counter = 10
MAC = 1000000000000

def createWorkspaceWindow():
    global createWorkspace_Window
    createWorkspace_Window = QtWidgets.QDialog()
    createWorkspaceUI.setupCreateWorkspace(createWorkspace_Window)
    sds_controller.start_new_workplace()
    createWorkspaceUI.createWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace)
    createWorkspaceUI.cancelWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace_Window.close)
    createWorkspace_Window.show()


def databaseConfigWindow():
    global databaseConfig_Window
    databaseConfig_Window = QtWidgets.QDialog()
    databaseConfigWindowUI.setupDatabaseConfig(databaseConfig_Window)
    databaseConfigWindowUI.databaseConfigIPConnectButton_databaseConfigWindow.clicked.connect(connect_database)
    databaseConfigWindowUI.databaseConfigIPCancelButton_databaseConfigWindow.clicked.connect(databaseConfig_Window.close)
    databaseConfig_Window.show()


def analysisManagerWindow():
    global analysisManager_Window
    analysisManager_Window = QtWidgets.QMainWindow()
    analysisManagerWindowUI.setupAnalysisManager(analysisManager_Window)
    #databaseConfigWindowUI.databaseConfigIPConnectButton_databaseConfigWindow.clicked.connect(connect_database)
    #databaseConfigWindowUI.databaseConfigIPCancelButton_databaseConfigWindow.clicked.connect(
     #   databaseConfig_Window.close)
    workspace_Window.close()
    analysisManager_Window.show()


def connect_database():
    global db_config_filename, mongo_connection
    database_ip = databaseConfigWindowUI.databaseConfigIPInput_databaseConfigWindow.text()
    # Edit config file to insert database ip
    data = None
    with open(db_config_filename, 'r') as config_file:
        data = json.load(config_file)
        data['ip'] = database_ip
    tempfile = os.path.join(os.path.dirname(db_config_filename), str(uuid.uuid4()))
    with open(tempfile, 'w') as config_file:
        json.dump(data, config_file, indent=4)
    os.replace(tempfile, db_config_filename)
    # Try to set up controller w/ database again
    mongo_connection, connection_success = set_up_database_connection()
    if connection_success:
        connect_subsystems_and_database()
        # If success -> close window
        databaseConfig_Window.close()
    else:
        databaseError_Window.show()


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
            captureManager_Window.show()
            createWorkspace_Window.close()
            workspace_Window.close()


def createProjectWindow():
    global newProject_Window
    newProject_Window = QtWidgets.QDialog()
    newProjectWindowUI.setupNewProject(newProject_Window)
    newProjectWindowUI.newProjectCreateButton_newProjectWindow.clicked.connect(createProject)
    newProjectWindowUI.newProjectCancelButton_newProjectWindow.clicked.connect(newProject_Window.close)
    sds_controller.start_new_project_phase()
    newProject_Window.show()


def newScenarioUnitWindow():
    global newScenarioUnit_Window
    newScenarioUnit_Window = QtWidgets.QDialog()
    newScenarioUnitWindowUI.setupNewScenarioUnit(newScenarioUnit_Window)
    newScenarioUnitWindowUI.newScenarioUnitCreateButton_newScenarioUnitWindow.clicked.connect(createScenario)
    newScenarioUnitWindowUI.newScenarioUnitCancelButton_newScenarioUnitWindow.clicked.connect(
        newScenarioUnit_Window.close)
    sds_controller.add_scenario_unit()
    newScenarioUnit_Window.show()


def addNodeWindow():
    global addNode_Window
    global MAC
    addNode_Window = QtWidgets.QDialog()
    addNodeWindowUI.setupAddNode(addNode_Window)
    addNodeWindowUI.addNodeButton_addNodeWindow.clicked.connect(addNode)
    addNodeWindowUI.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_Window.close)
    addNodeWindowUI.nodeScannerNodeCheckBox_addNodeWindow.toggled.connect(addNodeCheckboxStateChanged)
    addNodeWindowUI.nodeIPAddressInput_addNodeWindow.setText(f"1.1.{ip_counter}.2")
    MAC += 1
    node_mac = str(MAC)[1:]
    node_mac = f"{node_mac[0:2]}:{node_mac[2:4]}:{node_mac[4:6]}:{node_mac[6:8]}:{node_mac[8:10]}:{node_mac[10:12]}"
    addNodeWindowUI.nodeMACAddressInput_addNodeWindow.setText(node_mac)
    addNode_Window.show()


def addSetNodesWindow():
    global addSetNodes_Window
    addSetNodes_Window = QtWidgets.QDialog()
    addSetNodesWindowUI.setupAddSetNodes(addSetNodes_Window)
    addSetNodesWindowUI.setNodesCreateButton_addSetNodesWindow.clicked.connect(addSetNodes)
    addSetNodesWindowUI.setNodesCancelButton_addSetNodesWindow.clicked.connect(addSetNodes_Window.close)
    addSetNodesWindowUI.startingIPInput_addSetNodesWindow.setText(f"1.1.{ip_counter}.2")
    addSetNodes_Window.show()


def deleteConfirmationWindow():
    global deleteConfirmation_Window
    deleteConfirmation_Window = QtWidgets.QDialog()
    deleteConfirmationWindowUI.setupDeleteConfirmation(deleteConfirmation_Window)
    deleteConfirmationWindowUI.deleteConfirmationButton_deleteConfirmationWindow.clicked.connect(
        delete_selection)
    deleteConfirmationWindowUI.cancelConfirmationButton_deleteConfirmationWindow.clicked.connect(
        deleteConfirmation_Window.close)
    deleteConfirmation_Window.show()


def createProject():
    project_name = newProjectWindowUI.newProjectNameInput_newProjectWindow.text()
    # print(project_name)
    project_parallel = newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.value()

    # If the input is incorrect show the missing fields window
    if not project_name or project_parallel == 0:
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
    global ip_counter
    subnet = '0'
    log = ''
    if addNodeWindowUI.nodeLogNetNodeCheckBox_addNodeWindow.isChecked():
        log = 'True'
    else:
        log = 'False'
    type = addNodeWindowUI.nodeTypeComboBox_addNodeWindow.currentText()
    if type == 'CORE' or type == 'VM':
        type = 'PC'
    elif type == 'VM' or type == 'Docker':
        type = 'PC'  #temp solution
    name = addNodeWindowUI.nodeNameInput_addNodeWindow.text()
    MAC = addNodeWindowUI.nodeMACAddressInput_addNodeWindow.text()
    IP = addNodeWindowUI.nodeIPAddressInput_addNodeWindow.text()
    IP_parse = IP.split(".")
    ip_counter = int(IP_parse[2])+1
    # subnet = addNodeWindowUI.nodeSeparateSubNetNodeCheckBox_addNodeWindow.isChecked()
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
    global id_counter
    id_counter +=1
    sds_controller.insert_node(scenario_id, id_counter, log, type, name, IP, MAC, \
        subnet, scanning, user_pw, scanner_bin, arguments, int(num_iterations), \
        max_parallel_runs, end_condition)
    nodes_list = sds_controller.get_all_nodes(scenario_name)
    captureManagerWindowUI.nodesList_captureManagerWindow.clear()
    for node in nodes_list:
        node_item = QTreeWidgetItem([ str(node['listening']), \
            node['type'], node['name'], node['mac'], node['ip'], str(node['scanning'])])
        captureManagerWindowUI.nodesList_captureManagerWindow.addTopLevelItem(node_item)
    addNode_Window.close()
    captureManagerWindowUI.nodesList_captureManagerWindow.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)



# TODO: To be implemented
def addSetNodes():
    starting_ip = addSetNodesWindowUI.startingIPInput_addSetNodesWindow.text()
    name = addSetNodesWindowUI.startingNameInput_addSetNodesWindow.text()
    split_starting_ip = starting_ip.split(".")
    num_nodes = addSetNodesWindowUI.numberVictimNodesSpinbox_addSetNodesWindow.value()
    scenario_name = captureManagerWindowUI.projectsList_captureManagerWindow.selectedItems()[0].text(0)
    scenario_id = sds_controller.get_scenario_id(scenario_name)
    nodes_list = sds_controller.get_all_nodes(scenario_name)
    count = 1
    global MAC 
    global id_counter
    
    for i in range(int(split_starting_ip[3]), num_nodes + int(split_starting_ip[3]),1):
        id_counter +=1
        MAC += 1
        node_mac = str(MAC)[1:]
        node_mac = f"{node_mac[0:2]}:{node_mac[2:4]}:{node_mac[4:6]}:{node_mac[6:8]}:{node_mac[8:10]}:{node_mac[10:12]}"
        node_ip = f"{split_starting_ip[0]}.{split_starting_ip[1]}.{split_starting_ip[2]}.{i}"
        node_name = name + str(count)
        sds_controller.insert_node(scenario_id, id_counter, False, "PC", node_name, node_ip, node_mac, \
            True, False, "", "", "", 1, \
            1, "")
        count += 1
    
    nodes_list = sds_controller.get_all_nodes(scenario_name)
    captureManagerWindowUI.nodesList_captureManagerWindow.clear()
    for node in nodes_list:
        node_item = QTreeWidgetItem([ str(node['listening']), \
            node['type'], node['name'], node['mac'], node['ip'], str(node['scanning'])])
        captureManagerWindowUI.nodesList_captureManagerWindow.addTopLevelItem(node_item)
    addSetNodes_Window.close()
    captureManagerWindowUI.nodesList_captureManagerWindow.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        


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
        # captureManagerWindowUI.startVirtualMachineButton_captureManagerWindow.setEnabled(False)
        # captureManagerWindowUI.stopScenarioButton_captureManagerWindow.setEnabled(False)
        # captureManagerWindowUI.restoreScenarioButton_captureManagerWindow.setEnabled(False)
    else:
        #print(f'checking if else checked')
        captureManagerWindowUI.exportButton_captureManagerWindow.setEnabled(False)
        captureManagerWindowUI.addNodeButton_captureManagerWindow.setEnabled(True)
        captureManagerWindowUI.addSetNodeButton_captureManagerWindow.setEnabled(True)
        # captureManagerWindowUI.startVirtualMachineButton_captureManagerWindow.setEnabled(True)
        # captureManagerWindowUI.stopScenarioButton_captureManagerWindow.setEnabled(True)
        # captureManagerWindowUI.restoreScenarioButton_captureManagerWindow.setEnabled(True)
        # Get all the nodes
        scenario_ID = captureManagerWindowUI.projectsList_captureManagerWindow.selectedItems()[0].text(0)
        #print(f'checking scenario id: {scenario_ID}')
        sds_controller._enforce_state('init_project')
        node_list = sds_controller.get_all_nodes(scenario_ID)
        # Insert into vm and docker text saved values
        vm_ip, docker_ip = sds_controller.get_scenario_vm_info(scenario_ID)
#        captureManagerWindowUI.vmSdsServiceInput_captureManagerWindow.setText(vm_ip)
 #       captureManagerWindowUI.dockerSdsServiceInput_captureManagerWindow.setText(docker_ip)
        #print(f'checking if nodes list is anything: {node_list}')
        # Insert all the nodes into the UI
        if node_list:
            #print(f'checking if nodes list is available for ui...{node_list}')
            for node in node_list:
                node_item = QTreeWidgetItem([str(node['listening']), \
                    node['type'], node['name'], node['mac'], node['ip'], str(node['scanning'])])
                captureManagerWindowUI.nodesList_captureManagerWindow.addTopLevelItem(node_item)
                # TODO: Ask mauricio how this works
                # captureManagerWindowUI.nodesList_captureManagerWindow.setItemWidget(node_item, 6, toolButton)

        captureManagerWindowUI.nodesList_captureManagerWindow.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)


def save_workspace():
    # Everything is already saved. So we don't really need it. YW
    pass

def export_project():
    project_name = captureManagerWindowUI.projectsList_captureManagerWindow.selectedItems()[0].text(0)
    export_path = QFileDialog().getSaveFileName(caption='Export Project',directory='~/untitled.json')
    print(f'export path is: {export_path}')
    sds_controller._enforce_state('init_project')
    sds_controller.export_project(project_name, export_path[0]) 


def import_project():
    dialog = QFileDialog()
    json_path = dialog.getOpenFileName(captureManager_Window, 'Select JSON File', filter='*.json')
    with open(json_path[0]) as json_file:
        project = json.load(json_file)
        sds_controller._enforce_state('init_workplace')
        sds_controller.import_project(project)


def addNodeCheckboxStateChanged():
    addNodeWindowUI.addNodeButton_addNodeWindow.clicked.connect(addNode)
    addNodeWindowUI.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_Window.close)


def open_workspace():
    global current_workspace_name
    selected_workspace = workspaceUI.workspacesList_workspaceWindow.selectedItems()[0].text(0)
    current_workspace_name = selected_workspace
    # Change sds_controller workspace context
    # print(f'check if open_workspace is called')
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

    captureManagerWindowUI.projectsList_captureManagerWindow.expandAll()
    #Insert core options if saved
#    captureManagerWindowUI.corePortNumberInput_captureManagerWindow.setText(sds_controller.get_core_port())
 #   captureManagerWindowUI.coreSdsServiceInput_captureManagerWindow.setText(sds_controller.get_core_ip())

# TODO: Implement this
def delete_workspace(selected_workspace):
    ''' Removes the workspace. If projects don't exist in other workspaces then
    they will be deleted. Same rule for the scenarios and nodes.'''
    sds_controller.delete_workspace_contents(selected_workspace)


def set_up_scenario_unit():
    sds_controller._enforce_state('init_capture_network')
    scenario_name = captureManagerWindowUI.projectsList_captureManagerWindow.selectedItems()[0].text(0)
    vm_ip = captureManagerWindowUI.vmSdsServiceInput_captureManagerWindow.text()
    docker_ip = captureManagerWindowUI.dockerSdsServiceInput_captureManagerWindow.text()
    sds_controller.insert_vm_service(scenario_name, vm_ip, docker_ip)
    captureManagerWindowUI.vmSdsServiceInput_captureManagerWindow.setEnabled(False)
    captureManagerWindowUI.dockerSdsServiceInput_captureManagerWindow.setEnabled(False)
    # captureManagerWindowUI.runScenarioButton_captureManagerWindow.setEnabled(False)
    sds_controller.run_scenario_units(scenario_name)

def start_virtual_machine():
    # Get input
    # store input into workspace
    # sds_controller.insert_core_sds_service(ip, port)
    sds_controller.start_virtual_machine()
    # captureManagerWindowUI.runScenarioButton_captureManagerWindow.setEnabled(True)
    # captureManagerWindowUI.startVirtualMachineButton_captureManagerWindow.setEnabled(False)

def shutdown_virtual_machine():
    print("shutdown virtual machine")
    sds_controller.shutdown_virtual_machine()
    # captureManagerWindowUI.startVirtualMachineButton_captureManagerWindow.setEnabled(True)

def stop_scenario_unit():
    #sds_controller.stop()
    captureManagerWindowUI.vmSdsServiceInput_captureManagerWindow.setEnabled(True)
    captureManagerWindowUI.dockerSdsServiceInput_captureManagerWindow.setEnabled(True)
    # captureManagerWindowUI.runScenarioButton_captureManagerWindow.setEnabled(True)

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

    action_edit_workspace = QAction("Edit Workspace Name")
    action_delete_workspace = QAction("Delete Workspace")

    menu.addAction(action_edit_workspace)
    menu.addAction(action_delete_workspace)

    #action_edit_workspace.triggered.connect(lambda: edit_workspace(name))
    action_delete_workspace.triggered.connect(lambda: delete_workspace(name))

    menu.exec_(workspaceUI.workspacesList_workspaceWindow.mapToGlobal(point))


def context_menu_project(point):
    index = captureManagerWindowUI.projectsList_captureManagerWindow.indexAt(point)

    if not index.isValid():
        return

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

    if not index.isValid():
        return

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


def delete_selection():
    pass


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


def closeCaptureManager():
    workspace_Window.show()
    generate_workspaces_list_window()
    captureManager_Window.close()


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
    workspaceUI.workspacesList_workspaceWindow.doubleClicked.connect(open_workspace)

    captureManagerWindowUI.projectsList_captureManagerWindow.itemSelectionChanged.connect(item_project_selected)

    # Project button functions
    captureManagerWindowUI.newButton_captureManagerWindow.clicked.connect(createProjectWindow)
    captureManagerWindowUI.saveButton_captureManagerWindow.clicked.connect(save_workspace)
    captureManagerWindowUI.exportButton_captureManagerWindow.clicked.connect(export_project)
    captureManagerWindowUI.importButton_captureManagerWindow.clicked.connect(import_project)

    # Virtual Machine button functions
    captureManagerWindowUI.startVirtualMachineButton_captureManagerWindow.clicked.connect(start_virtual_machine)
    captureManagerWindowUI.shutdownVMButton_captureManagerWindow.clicked.connect(shutdown_virtual_machine)

    # Scenario button functions
    captureManagerWindowUI.runScenarioButton_captureManagerWindow.clicked.connect(set_up_scenario_unit)
    captureManagerWindowUI.stopScenarioButton_captureManagerWindow.clicked.connect(stop_scenario_unit)
    captureManagerWindowUI.restoreScenarioButton_captureManagerWindow.clicked.connect(restore_scenario_unit)

    # Node button functions
    captureManagerWindowUI.addNodeButton_captureManagerWindow.clicked.connect(addNodeWindow)
    captureManagerWindowUI.addSetNodeButton_captureManagerWindow.clicked.connect(addSetNodesWindow)

    captureManagerWindowUI.projectsList_captureManagerWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    captureManagerWindowUI.projectsList_captureManagerWindow.customContextMenuRequested.connect(context_menu_project)
    captureManagerWindowUI.nodesList_captureManagerWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    captureManagerWindowUI.nodesList_captureManagerWindow.customContextMenuRequested.connect(context_menu_node)
    captureManagerWindowUI.closeWorkspaceButton_captureManagerWindow.clicked.connect(closeCaptureManager)

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
        for workspace_c in workspaces_c:
            l1 = QtWidgets.QTreeWidgetItem([workspace_c])
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
        return db, True
    except:
        return None, False


def assert_database_connection():
    global sds_controller, mongo_connection
    mongo_connection, db_connection_success = set_up_database_connection()

    if db_connection_success:
        connect_subsystems_and_database()
        workspace_Window.show()
    else:
        workspace_Window.show()
        databaseError_Window.show()


def connect_subsystems_and_database():
    sds_controller.add_mongo_connection(mongo_connection)
    sds_controller.add_capture_manager(CaptureController())
    sds_controller.add_analysis_manager(SDSAnalysisManager())
    # sds controller implementation for filling workspaces
    generate_workspaces_list_window()


setup_ui()

initialize_signals()

assert_database_connection()

sys.exit(app.exec_())
