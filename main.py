# Imports
import os
import string
import sys
import time
import json

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTreeWidgetItem, QFileDialog, QAction
from pymongo import MongoClient

from Database.DatabaseHelper import SDSDatabaseHelper

from views.addNodeWindow import Ui_addNode_window
from views.createWorkspace import Ui_newWorkspace_window
from views.mainWindow import Ui_MainWindow
from views.missingFieldsWindow import Ui_missingFields_window
from views.newProject import Ui_newProject_window
from views.newScenarioUnitWindow import Ui_newScenarioUnit_window
from views.workspace import Ui_workspace_window


################ CLASSES ################
class Workspace:
    def __init__(self, name, location, projects):
        self.name = name
        self.location = location
        self.projects = projects


class Project:
    def __init__(self, name, location, max_units, scenarios):
        self.name = name
        self.location = location
        self.max_units = max_units
        self.scenarios = scenarios


class Scenario:
    def __init__(self, name, location, nodes):
        self.name = name
        self.location = location
        self.nodes = nodes


class Node:
    def __init__(self, listening, node_type, name, IP, port, MAC, scanner):
        self.listening = listening
        self.type = node_type
        self.name = name
        self.IP = IP
        self.port = port
        self.MAC = MAC
        self.scanner = scanner


class ScannerNode:
    def __init__(self, us_pas, scanner_binary, arguments, iterations, max_parallel_runs, end_condition):
        self.us_pas = us_pas
        self.scanner_binary = scanner_binary
        self.arguments = arguments
        self.iterations = iterations
        self.max_parallel_runs = max_parallel_runs
        self.end_condition = end_condition

################ END CLASSES ################

################ CONSTANTS ################
SDS_DATABASE_NAME = 'SDS_DB'
DEFAULT_WORKSPACE_COLLECTION_OBJECT = {'_id': 0, 'Name': '', 'Location': '', 'Projects': []}
SDS_DB_Helper = SDSDatabaseHelper()
################ END CONSTANTS ################

################ GLOBAL VARIABLES ################
global_workspace_path : string = ''
global_workspace_name : string = ''
global_workspace_object = Workspace('', '', [])
################ END GLOBAL VARIABLES ################


def createWorkspace():
    global global_workspace_name, global_workspace_path, global_workspace_object

    # validate inputs
    if createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text() == '' \
            or createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.text() == '':

        missingFields_Window.show()
        return

    print("Inserting new workspace into db")
    new_query = {
                '_id': time.time_ns(),
                'Name': createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text(),
                'Location': createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.text()
                }
    SDS_DB_Helper.insert_workspace(new_query)
    print("Item inserted with id " + str(new_query['_id']))

    # create directory
    directory_to_make_path : string = str(os.path.join(os.getcwd() , createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text()))
    print("Creating directory to with path " + directory_to_make_path)
    os.makedirs(directory_to_make_path)

    # set global workspace_path variable value 
    global_workspace_path = directory_to_make_path

    global_workspace_object.name = createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text()
    global_workspace_object.location = directory_to_make_path
    global_workspace_object.projects = []

    # update views
    mainWindow_Window.show()
    createWorkspace_Window.close()
    workspace_Window.close()

def createProject():
    global global_workspace_name, global_workspace_path

    # validate inputs
    if newProjectWindowUI.newProjectNameInput_newProjectWindow.text() == '' \
            or newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.value() == 0:
        missingFields_Window.show()
        return

    qt_project_column_object = QtWidgets.QTreeWidgetItem([newProjectWindowUI.newProjectNameInput_newProjectWindow.text()])
    max_units_input_value = newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.value()

    project_object = Project(
        newProjectWindowUI.newProjectNameInput_newProjectWindow.text(),
        os.path.join(global_workspace_path, newProjectWindowUI.newProjectNameInput_newProjectWindow.text()),
        max_units_input_value,
        []
    )
    
    # is this needed? if not delete - Erik
    #for i in range(0, value):
        #   scenario = QTreeWidgetItem(['Scenario ' + str(i + 1)])
        #  scenarios['Scenario ' + str(i + 1)] = ''
        # p.addChild(scenario)
        #scenario_object = Scenario('', '', '')
        #scenario_object.name = 'Scenario ' + str(i + 1)
        #scenario_object.location = os.path.join(project_object.location, 'Scenario ' + str(i + 1))
        #scenario_object.nodes = ''
        #project_object.scenarios.append(scenario_object)

    # update view
    mainWindowUI.projectsList_mainWindow.addTopLevelItem(qt_project_column_object)

    # project = [newProjectWindowUI.newProjectNameInput_newProjectWindow.text(), scenarios]

    global_workspace_object.projects.append(project_object)

    # update db
    SDS_DB_Helper.update_workspace(global_workspace_name, global_workspace_object)

    # close window
    newProject_Window.close()

    newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.setValue(0)
    newProjectWindowUI.newProjectNameInput_newProjectWindow.clear()

    newProject_Window.close()

def define_workspace_path():
    global global_workspace_path
    dialog = QFileDialog()
    global_workspace_path = dialog.getExistingDirectory(createWorkspace_Window, 'Select Workspace Directory')
    createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.setText(global_workspace_path)

def item_project_selected():
    if mainWindowUI.projectsList_mainWindow.selectedItems()[0].parent() is None:
        mainWindowUI.exportButton_mainWindow.setEnabled(True)
    else:
        mainWindowUI.exportButton_mainWindow.setEnabled(False)

def save_workspace():
    for project in global_workspace_object.projects:
        # first check if the directory exists, if it does delete it
        if os.path.exists(global_workspace_object.location + "/" + project.name):
            os.removedirs(global_workspace_object.location + "/" + project.name)

        os.makedirs(global_workspace_object.location + "/" + project.name)

        for scenario in project.scenarios:
            os.makedirs(global_workspace_object.location + "/" + project.name + "/" + scenario.name)

def export_project():
    scenarios = {}
    project_name = mainWindowUI.projectsList_mainWindow.selectedItems()[0].text(0)
    project_path = ''
    projects = global_workspace_object.projects
    for project in projects:
        if project.name == project_name:

            project_path = project.location
            for scenario in project.scenarios:
                scenarios[scenario.name] = ''

    json_project = [project_name, scenarios]

    json_string = json.dumps(json_project)

    with open(project_path + '.json', 'w') as outfile:
        outfile.write(json_string)

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
    addNodeWindowUI.addNodeButton_addNodeWindow.clicked.connect(addNode_Window.close)
    addNodeWindowUI.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_Window.close)

def open_workspace(selected_workspace_name):
    global global_workspace_name

    global_workspace_name = selected_workspace_name
    mainWindow_Window.setWindowTitle(selected_workspace_name + ' - Scan Detection System')
    mainWindow_Window.show()
    workspace_Window.close()

    # populate left column with workspace names
    for project_object in SDS_DB_Helper.get_all_projects_from_workspace(selected_workspace_name):
        l1 = QtWidgets.QTreeWidgetItem([project_object.name])
        mainWindowUI.projectsList_mainWindow.addTopLevelItem(l1)

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

        action_add_scenario.triggered.connect(newScenarioUnit_Window.show)

        menu.exec_(mainWindowUI.projectsList_mainWindow.mapToGlobal(point))

        return


##### MAIN #####

# Set up PyQT and views
app = QtWidgets.QApplication(sys.argv)
workspace_Window = QtWidgets.QDialog()
createWorkspace_Window = QtWidgets.QDialog()
mainWindow_Window = QtWidgets.QMainWindow()
newProject_Window = QtWidgets.QDialog()
addNode_Window = QtWidgets.QDialog()
missingFields_Window = QtWidgets.QDialog()
newScenarioUnit_Window = QtWidgets.QDialog()

workspaceUI = Ui_workspace_window()
createWorkspaceUI = Ui_newWorkspace_window()
mainWindowUI = Ui_MainWindow()
newProjectWindowUI = Ui_newProject_window()
addNodeWindowUI = Ui_addNode_window()
missingFieldsWindowUI = Ui_missingFields_window()
newScenarioUnitWindowUI = Ui_newScenarioUnit_window()

workspaceUI.setupWorkspaceUI(workspace_Window)
createWorkspaceUI.setupCreateWorkspace(createWorkspace_Window)
mainWindowUI.setupMainWindowUI(mainWindow_Window)
newProjectWindowUI.setupNewProject(newProject_Window)
addNodeWindowUI.setupAddNode(addNode_Window)
missingFieldsWindowUI.setupMissingFields(missingFields_Window)
newScenarioUnitWindowUI.setupNewScenarioUnit(newScenarioUnit_Window)

# Set up database objects
client = MongoClient("mongodb://localhost:27017/")
SDS_DB = client[SDS_DATABASE_NAME]
workspace_collection = SDS_DB['workspaces']


# list available workspaces
workspaces = SDS_DB_Helper.get_all_workspaces()
if workspaces is not None:
    for current_workspace in workspaces:
        l1 = QtWidgets.QTreeWidgetItem([current_workspace['Name']])
        l1_child = QTreeWidgetItem([current_workspace['Location']])
        l1_child.setFlags(l1_child.flags() & ~QtCore.Qt.ItemIsSelectable)
        l1.addChild(l1_child)
        workspaceUI.workspacesList_workspaceWindow.addTopLevelItem(l1)

workspaceUI.createWorkspaceButton_workspaceWindow.clicked.connect(createWorkspace_Window.show)
workspaceUI.workspacesList_workspaceWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
workspaceUI.workspacesList_workspaceWindow.customContextMenuRequested.connect(context_menu_workspace)

createWorkspaceUI.createWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace)
createWorkspaceUI.cancelWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace_Window.close)
createWorkspaceUI.browseWorkspaceButton_newWorkspaceWindow.clicked.connect(define_workspace_path)

mainWindowUI.newButton_mainWindow.clicked.connect(newProject_Window.show)
mainWindowUI.projectsList_mainWindow.itemSelectionChanged.connect(item_project_selected)
mainWindowUI.saveButton_mainWindow.clicked.connect(save_workspace)
mainWindowUI.exportButton_mainWindow.clicked.connect(export_project)
mainWindowUI.importButton_mainWindow.clicked.connect(import_project)
mainWindowUI.addNodeButton_mainWindow.clicked.connect(addNode_Window.show)
mainWindowUI.projectsList_mainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
mainWindowUI.projectsList_mainWindow.customContextMenuRequested.connect(context_menu_project)

newProjectWindowUI.newProjectCreateButton_newProjectWindow.clicked.connect(createProject)
newProjectWindowUI.newProjectCancelButton_newProjectWindow.clicked.connect(newProject_Window.close)

addNodeWindowUI.addNodeButton_addNodeWindow.clicked.connect(addNode_Window.close)
addNodeWindowUI.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_Window.close)

addNodeWindowUI.nodeScannerNodeCheckBox_addNodeWindow.toggled.connect(addNodeCheckboxStateChanged)

missingFieldsWindowUI.missingFieldsCloseButton_missingFieldsWindow.clicked.connect(missingFields_Window.close)

workspace_Window.show()

sys.exit(app.exec_())

##### END MAIN #####