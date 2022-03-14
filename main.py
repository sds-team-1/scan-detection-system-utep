import os
import sys
import time
import json

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem, QFileDialog
from pymongo import MongoClient

from views.addNodeWindow import Ui_addNode_window
from views.createWorkspace import Ui_newWorkspace_window
from views.mainWindow import Ui_MainWindow
from views.missingFieldsWindow import Ui_missingFields_window
from views.newProject import Ui_newProject_window
from views.workspace import Ui_workspace_window


class Workspace:
    def __init__(self, name, location, projects):
        self.name = name
        self.location = location
        self.projects = projects


class Project:
    def __init__(self, name, location, scenarios):
        self.name = name
        self.location = location
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


client = MongoClient("mongodb://localhost:27017/")

dbs = client.list_database_names()

SDS_DB = client['SDS_DB']
workspaces_DB = SDS_DB['workspaces']

app = QtWidgets.QApplication(sys.argv)

workspace_Window = QtWidgets.QDialog()
createWorkspace_Window = QtWidgets.QDialog()
mainWindow_Window = QtWidgets.QMainWindow()
newProject_Window = QtWidgets.QDialog()
addNode_Window = QtWidgets.QDialog()
missingFields_Window = QtWidgets.QDialog()

workspaceUI = Ui_workspace_window()
createWorkspaceUI = Ui_newWorkspace_window()
mainWindowUI = Ui_MainWindow()
newProjectWindowUI = Ui_newProject_window()
addNodeWindowUI = Ui_addNode_window()
missingFieldsWindowUI = Ui_missingFields_window()

workspaceUI.setupWorkspaceUI(workspace_Window)
createWorkspaceUI.setupCreateWorkspace(createWorkspace_Window)
mainWindowUI.setupMainWindowUI(mainWindow_Window)
newProjectWindowUI.setupNewProject(newProject_Window)
addNodeWindowUI.setupAddNode(addNode_Window)
missingFieldsWindowUI.setupMissingFields(missingFields_Window)

workspace_path = ''
workspace_name = ''
workspace_object = Workspace('', '', [])

if 'SDS_DB' not in dbs:
    workspace = {'_id': 0, 'Name': '', 'Location': '', 'Projects': []}
    workspaces_DB.insert_one(workspace)

else:
    query = workspaces_DB.find_one()
    if query['Name'] != '':
        for query in workspaces_DB.find():
            l1 = QtWidgets.QTreeWidgetItem([query['Name']])
            l1_child = QTreeWidgetItem([query['Location']])
            l1.addChild(l1_child)
            workspaceUI.workspacesList_workspaceWindow.addTopLevelItem(l1)


def createWorkspaceWindow():
    createWorkspace_Window.show()


def createWorkspace():
    global workspace_name, workspace_path, workspace_object
    first_query = workspaces_DB.find_one()

    if first_query['Name'] == '':
        new_query = {'$set': {'Name': createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text(),
                              'Location': createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.text()}}
        workspaces_DB.update_one(first_query, new_query)

        workspace_name = createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text()

    else:
        current_id = workspaces_DB.find().sort('_id', -1).limit(1)
        for doc in current_id:
            current_id = doc['_id']

        new_query = {'_id': int(current_id + 1),
                     'Name': createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text(),
                     'Location': createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.text(),
                     'Projects': []}

        workspaces_DB.insert_one(new_query)

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


def addNodeWindow():
    addNode_Window.show()


def createProject():
    global workspace_name, workspace_path
    p = QtWidgets.QTreeWidgetItem([newProjectWindowUI.newProjectNameInput_newProjectWindow.text()])
    value = newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.value()
    scenarios = {}

    project_object = Project('', '', [])

    project_object.name = newProjectWindowUI.newProjectNameInput_newProjectWindow.text()

    project_path = os.path.join(workspace_path, newProjectWindowUI.newProjectNameInput_newProjectWindow.text())

    project_object.location = project_path

    for i in range(0, value):
        scenario = QTreeWidgetItem(['Scenario ' + str(i + 1)])
        scenarios['Scenario ' + str(i + 1)] = ''
        p.addChild(scenario)
        scenario_object = Scenario('', '', '')
        scenario_object.name = 'Scenario ' + str(i + 1)
        scenario_object.location = os.path.join(project_object.location, 'Scenario ' + str(i + 1))
        scenario_object.nodes = ''
        project_object.scenarios.append(scenario_object)

    mainWindowUI.projectsList_mainWindow.addTopLevelItem(p)

    project = [newProjectWindowUI.newProjectNameInput_newProjectWindow.text(), scenarios]

    workspace_object.projects.append(project_object)

    for q in workspaces_DB.find():
        if q['Name'] == workspace_name:
            workspaces_DB.update_one({'Projects': q['Projects']},
                                     {'$push': {'Projects': project}})

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


def item_workspace_selected():
    if workspaceUI.workspacesList_workspaceWindow.selectedItems()[0].parent() is None:
        global workspace_name
        time.sleep(1)
        workspace_name = workspaceUI.workspacesList_workspaceWindow.selectedItems()[0].text(0)
        mainWindow_Window.setWindowTitle(workspaceUI.workspacesList_workspaceWindow.selectedItems()[0].text(0) +
                                         ' - Scan Detection System')
        mainWindow_Window.show()
        workspace_Window.close()

        for q in workspaces_DB.find():
            if q['Name'] == workspace_name:
                for p in q['Projects']:
                    projectName = QtWidgets.QTreeWidgetItem([p[0]])
                    for k, v in p[1].items():
                        scenarioName = QTreeWidgetItem([k])
                        projectName.addChild(scenarioName)
                        mainWindowUI.projectsList_mainWindow.addTopLevelItem(projectName)


def item_project_selected():
    if mainWindowUI.projectsList_mainWindow.selectedItems()[0].parent() is None:
        mainWindowUI.exportButton_mainWindow.setEnabled(True)
    else:
        mainWindowUI.exportButton_mainWindow.setEnabled(False)


def save_workspace():
    for project in workspace_object.projects:
        os.makedirs(os.path.join(workspace_object.location,
                                 project.name))

        for scenario in project.scenarios:
            os.makedirs(os.path.join(project.location,
                                     scenario.name))


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


workspaceUI.createWorkspaceButton_workspaceWindow.clicked.connect(createWorkspaceWindow)
workspaceUI.workspacesList_workspaceWindow.itemSelectionChanged.connect(item_workspace_selected)

createWorkspaceUI.createWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace)
createWorkspaceUI.cancelWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace_Window.close)
createWorkspaceUI.browseWorkspaceButton_newWorkspaceWindow.clicked.connect(define_workspace_path)

mainWindowUI.newButton_mainWindow.clicked.connect(createProjectWindow)
mainWindowUI.projectsList_mainWindow.itemSelectionChanged.connect(item_project_selected)
mainWindowUI.saveButton_mainWindow.clicked.connect(save_workspace)
mainWindowUI.exportButton_mainWindow.clicked.connect(export_project)
mainWindowUI.importButton_mainWindow.clicked.connect(import_project)
mainWindowUI.addNodeButton_mainWindow.clicked.connect(addNodeWindow)

newProjectWindowUI.newProjectCreateButton_newProjectWindow.clicked.connect(createProject)
newProjectWindowUI.newProjectCancelButton_newProjectWindow.clicked.connect(newProject_Window.close)

addNodeWindowUI.addNodeButton_addNodeWindow.clicked.connect(addNode)
addNodeWindowUI.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_Window.close)

missingFieldsWindowUI.missingFieldsCloseButton_missingFieldsWindow.clicked.connect(missingFields_Window.close)

workspace_Window.show()

sys.exit(app.exec_())
