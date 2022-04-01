# Imports
import os
import sys
import time
import json

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTreeWidgetItem, QFileDialog, QAction
from pymongo import MongoClient

import captureController
from views.addNodeWindow import Ui_addNode_window
from views.createWorkspace import Ui_newWorkspace_window
from views.mainWindow import Ui_MainWindow
from views.missingFieldsWindow import Ui_missingFields_window
from views.newProject import Ui_newProject_window
from views.newScenarioUnitWindow import Ui_newScenarioUnit_window
from views.workspace import Ui_workspace_window

from Controllers.SDSController import SDSController
from Database.DatabaseHelper import SDSDatabaseHelper
from Controllers.AnalysisManager import SDSAnalysisManager


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

################ END CONSTANTS ################


# Set up database objects
client = MongoClient("mongodb://localhost:27017/")
SDS_DB = client[SDS_DATABASE_NAME]
workspace_collection = SDS_DB['workspaces']

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

workspace_path = ''
workspace_name = ''
workspace_object = Workspace('', '', [])

def createWorkspace():
    global workspace_name, workspace_path, workspace_object

    if createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text() == '' \
            or createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.text() == '':

        missingFields_Window.show()

    else:
        first_query = workspace_collection.find_one()

        if first_query['Name'] == '':
            new_query = {'$set': {'Name': createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text(),
                                  'Location': createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.text()}}
            workspace_collection.update_one(first_query, new_query)

            workspace_name = createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text()

        else:
            current_id = workspace_collection.find().sort('_id', -1).limit(1)
            for doc in current_id:
                current_id = doc['_id']

            new_query = {'_id': int(current_id + 1),
                         'Name': createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text(),
                         'Location': createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.text(),
                         'Projects': []}

            workspace_collection.insert_one(new_query)

        os.makedirs(os.path.join(workspace_path, createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text()))

        workspace_path = os.path.join(workspace_path, createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text())

        workspace_object.name = createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text()
        workspace_object.location = workspace_path
        workspace_object.projects = []

        mainWindow_Window.show()
        createWorkspace_Window.close()
        workspace_Window.close()


def createProjectWindow():
    newProject_Window.show()


def newScenarioUnitWindow():
    newScenarioUnit_Window.show()


def addNodeWindow():
    addNode_Window.show()



def createProjectWindow():
    newProject_Window.show()

def newScenarioUnitWindow():
    newScenarioUnit_Window.show()

def addNodeWindow():
    addNode_Window.show()

def createProject():
    global workspace_name, workspace_path

    if newProjectWindowUI.newProjectNameInput_newProjectWindow.text() == '' \
            or newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.value() == 0:
        missingFields_Window.show()

    else:
        p = QtWidgets.QTreeWidgetItem([newProjectWindowUI.newProjectNameInput_newProjectWindow.text()])
        value = newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.value()
        #scenarios = {}

        project_object = Project('', '', 0, [])

        project_object.name = newProjectWindowUI.newProjectNameInput_newProjectWindow.text()

        project_path = os.path.join(workspace_path, newProjectWindowUI.newProjectNameInput_newProjectWindow.text())

        project_object.location = project_path

        project_object.max_units = value

        #for i in range(0, value):
         #   scenario = QTreeWidgetItem(['Scenario ' + str(i + 1)])
          #  scenarios['Scenario ' + str(i + 1)] = ''
           # p.addChild(scenario)
            #scenario_object = Scenario('', '', '')
            #scenario_object.name = 'Scenario ' + str(i + 1)
            #scenario_object.location = os.path.join(project_object.location, 'Scenario ' + str(i + 1))
            #scenario_object.nodes = ''
            #project_object.scenarios.append(scenario_object)

        mainWindowUI.projectsList_mainWindow.addTopLevelItem(p)

       # project = [newProjectWindowUI.newProjectNameInput_newProjectWindow.text(), scenarios]

        workspace_object.projects.append(project_object)

        #for q in workspaces_DB.find():
          #  if q['Name'] == workspace_name:
         #       workspaces_DB.update_one({'Projects': q['Projects']},
           #                              {'$push': {'Projects': project}})

        newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.setValue(0)
        newProjectWindowUI.newProjectNameInput_newProjectWindow.clear()

        newProject_Window.close()

def addNode():
    addNode_Window.close()


def define_workspace_path():
    global workspace_path
    dialog = QFileDialog()
    workspace_path = dialog.getExistingDirectory(createWorkspace_Window, 'Select Workspace Directory')
    createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.setText(workspace_path)

def item_project_selected():
    if mainWindowUI.projectsList_mainWindow.selectedItems()[0].parent() is None:
        mainWindowUI.exportButton_mainWindow.setEnabled(True)
    else:
        mainWindowUI.exportButton_mainWindow.setEnabled(False)


def save_workspace():
    for project in workspace_object.projects:
        # first check if the directory exists, if it does delete it
        if os.path.exists(workspace_object.location + "/" + project.name):
            os.removedirs(workspace_object.location + "/" + project.name)

        os.makedirs(workspace_object.location + "/" + project.name)

        for scenario in project.scenarios:
            os.makedirs(workspace_object.location + "/" + project.name + "/" + scenario.name)

def export_project():
    scenarios = {}
    project_name = mainWindowUI.projectsList_mainWindow.selectedItems()[0].text(0)
    project_path = ''
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
    global workspace_name
    time.sleep(1)
    workspace_name = selected_workspace
    mainWindow_Window.setWindowTitle(selected_workspace + ' - Scan Detection System')
    mainWindow_Window.show()
    workspace_Window.close()

    for q in workspace_collection.find():
        if q['Name'] == workspace_name:
            for p in q['Projects']:
                projectName = QtWidgets.QTreeWidgetItem([p[0]])
                for k, v in p[1].items():
                    scenarioName = QTreeWidgetItem([k])
                    projectName.addChild(scenarioName)
                    mainWindowUI.projectsList_mainWindow.addTopLevelItem(projectName)

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

        action_add_scenario.triggered.connect(newScenarioUnitWindow)

        menu.exec_(mainWindowUI.projectsList_mainWindow.mapToGlobal(point))

        return


# Check if database exists, if not insert default item to create database and workspace
databases_list = client.list_database_names()
if 'SDS_DB' not in databases_list:
    workspace = {'_id': 0, 'Name': '', 'Location': '', 'Projects': []}
    workspace_collection.insert_one(workspace)

else:
    query = workspace_collection.find_one()
    if query is None:
        workspace = {'_id': 0, 'Name': '', 'Location': '', 'Projects': []}
        workspace_collection.insert_one(workspace)

    query = workspace_collection.find_one()

    if query['Name'] != '':
        for query in workspace_collection.find():
            l1 = QtWidgets.QTreeWidgetItem([query['Name']])
            l1_child = QTreeWidgetItem([query['Location']])
            l1_child.setFlags(l1_child.flags() & ~QtCore.Qt.ItemIsSelectable)
            l1.addChild(l1_child)
            workspaceUI.workspacesList_workspaceWindow.addTopLevelItem(l1)

workspaceUI.createWorkspaceButton_workspaceWindow.clicked.connect(createWorkspace_Window.show)
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
mainWindowUI.projectsList_mainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
mainWindowUI.projectsList_mainWindow.customContextMenuRequested.connect(context_menu_project)
#mainWindowUI.wiresharkButton_mainWindow.clicked(captureController.open_wireshark("C:\\Users\\Luis\\Downloads\\200722_tcp_anon.pcapng"))
newProjectWindowUI.newProjectCreateButton_newProjectWindow.clicked.connect(createProject)
newProjectWindowUI.newProjectCancelButton_newProjectWindow.clicked.connect(newProject_Window.close)

addNodeWindowUI.addNodeButton_addNodeWindow.clicked.connect(addNode)
addNodeWindowUI.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_Window.close)

addNodeWindowUI.nodeScannerNodeCheckBox_addNodeWindow.toggled.connect(addNodeCheckboxStateChanged)

missingFieldsWindowUI.missingFieldsCloseButton_missingFieldsWindow.clicked.connect(missingFields_Window.close)


##### Top-level Integration w/ all subsystems. #####
sds_controller = SDSController()
import captureController as capture_controller
sds_controller.add_capture_manager(capture_controller)
sds_controller.add_analysis_manager(SDSAnalysisManager())
sds_controller.add_mongo_connection(SDSDatabaseHelper())

workspace_Window.show()

sys.exit(app.exec_())
