import os
import sys
import time
import json
import uuid

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem, QFileDialog

from Models.modelClasses import Workspace
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
from Controllers.AnalysisManager import SDSAnalysisManager
from Controllers.CaptureController import CaptureController
from Controllers.SDSController import SDSController
from Database.DatabaseHelper import SDSDatabaseHelper

 
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
    with open('conf/db_config.json') as mongo_ip_file:
        database_ip_dict = json.load(mongo_ip_file)
        ip = database_ip_dict['ip']
        databaseConfigWindowUI.databaseConfigIPInput_databaseConfigWindow.setText(ip)
        port = database_ip_dict['port']
        databaseConfigWindowUI.databaseConfigPortInput_databaseConfigWindow.setText(port)
    databaseConfig_Window.show()


def analysisManagerWindow():
    global analysisManager_Window
    analysisManager_Window = QtWidgets.QMainWindow()
    analysisManagerWindowUI.setupAnalysisManager(analysisManager_Window)
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
            captureManager_Window.show()
            createWorkspace_Window.close()
            workspace_Window.close()


def addNodeWindow():
    global addNode_Window
    global MAC
    addNode_Window = QtWidgets.QDialog()
    addNodeWindowUI.setupAddNode(addNode_Window)
    addNodeWindowUI.addNodeButton_addNodeWindow.clicked.connect(addNode)
    addNodeWindowUI.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_Window.close)
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
        arguments = addNodeWindowUI.nodeNMapArgumentsInput_addNodeWindow.text() + "$$$" + addNodeWindowUI.nodeNiktoArgumentsInput_addNodeWindow.text()
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


def delete_selection():
    pass


def closeCaptureManager():
    workspace_Window.show()
    generate_workspaces_list_window()
    captureManager_Window.close()


def setup_ui():
    workspaceUI.setupWorkspaceUI(workspace_Window, sds_controller)
    captureManagerWindowUI.setupCaptureManager(captureManager_Window, sds_controller)
    databaseErrorWindowUI.setupDatabaseError(databaseError_Window)


def initialize_signals():
    workspaceUI.createWorkspaceButton_workspaceWindow.clicked.connect(createWorkspaceWindow)
    workspaceUI.dbConfigButton_workspaceWindow.clicked.connect(databaseConfigWindow)
    workspaceUI.analysisManagerButton_workspaceWindow.clicked.connect(analysisManagerWindow)
    # workspaceUI.analysisManagerButton_workspaceWindow.clicked.connect(analysisManagerWindow)
    # workspaceUI.dbConfigButton_workspaceWindow.clicked.connect(databaseConfigurationWindow)
    workspaceUI.workspacesList_workspaceWindow.doubleClicked.connect(open_workspace)

    # Node button functions
    captureManagerWindowUI.addNodeButton_captureManagerWindow.clicked.connect(addNodeWindow)
    captureManagerWindowUI.addSetNodeButton_captureManagerWindow.clicked.connect(addSetNodesWindow)

    captureManagerWindowUI.closeWorkspaceButton_captureManagerWindow.clicked.connect(closeCaptureManager)

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
