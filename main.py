# from Helpers import DatabaseHelper as DatabaseHelper

import os
import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem, QFileDialog
from pymongo import MongoClient

from views.createWorkspace import Ui_newWorkspace_window
from views.mainWindow import Ui_MainWindow
from views.newProject import Ui_newProject_window
from views.workspace import Ui_workspace_window

client = MongoClient("mongodb://localhost:27017/")

dbs = client.list_database_names()

SDS_DB = client['SDS_DB']
workspaces_DB = SDS_DB['workspaces']

app = QtWidgets.QApplication(sys.argv)

workspace_Window = QtWidgets.QDialog()
createWorkspace_Window = QtWidgets.QDialog()
mainWindow_Window = QtWidgets.QMainWindow()
newProject_Window = QtWidgets.QDialog()

workspaceUI = Ui_workspace_window()
createWorkspaceUI = Ui_newWorkspace_window()
mainWindowUI = Ui_MainWindow()
newProjectWindowUI = Ui_newProject_window()

workspaceUI.setupWorkspaceUI(workspace_Window)
createWorkspaceUI.setupCreateWorkspace(createWorkspace_Window)
mainWindowUI.setupMainWindowUI(mainWindow_Window)
newProjectWindowUI.setupNewProject(newProject_Window)

workspace_path = ''
workspace_name = ''

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
    global workspace_name, workspace_path
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

    mainWindow_Window.show()
    createWorkspace_Window.close()
    workspace_Window.close()


def createProjectWindow():
    newProject_Window.show()


def createProject():
    global workspace_name, workspace_path
    p = QtWidgets.QTreeWidgetItem([newProjectWindowUI.newProjectNameInput_newProjectWindow.text()])
    value = newProjectWindowUI.newProjectMaxUnitsSpinbox_newProjectWindow.value()
    scenarios = {}

    os.makedirs(os.path.join(workspace_path, newProjectWindowUI.newProjectNameInput_newProjectWindow.text()))

    project_path = os.path.join(workspace_path, newProjectWindowUI.newProjectNameInput_newProjectWindow.text())

    for i in range(0, value):
        scenario = QTreeWidgetItem(['Scenario ' + str(i + 1)])
        scenarios['Scenario ' + str(i + 1)] = ''
        p.addChild(scenario)
        os.makedirs(os.path.join(project_path, 'Scenario ' + str(i + 1)))

    mainWindowUI.projectsList_mainWindow.addTopLevelItem(p)

    project = [newProjectWindowUI.newProjectNameInput_newProjectWindow.text(), scenarios]

    for q in workspaces_DB.find():
        if q['Name'] == workspace_name:
            workspaces_DB.update_one({'Projects': q['Projects']},
                                     {'$push': {'Projects': project}})

    newProject_Window.close()


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


workspaceUI.createWorkspaceButton_workspaceWindow.clicked.connect(createWorkspaceWindow)
workspaceUI.workspacesList_workspaceWindow.itemSelectionChanged.connect(item_workspace_selected)

createWorkspaceUI.createWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace)
createWorkspaceUI.cancelWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace_Window.close)
createWorkspaceUI.browseWorkspaceButton_newWorkspaceWindow.clicked.connect(define_workspace_path)

mainWindowUI.newButton_mainWindow.clicked.connect(createProjectWindow)
mainWindowUI.projectsList_mainWindow.itemSelectionChanged.connect(item_project_selected)

newProjectWindowUI.newProjectCreateButton_newProjectWindow.clicked.connect(createProject)
newProjectWindowUI.newProjectCancelButton_newProjectWindow.clicked.connect(newProject_Window.close)

workspace_Window.show()

sys.exit(app.exec_())

# example of how to insert a document into mongo
# SDSdb = DatabaseHelper.SDSDatabaseHelper()
# tempObjectToInsert = {}
# tempObjectToInsert['name'] = 'Test'
# tempObjectToInsert['type'] = 'test type'
# tempObjectToInsert['_id'] = random.randint(1, 100)
# SDSdb.insertObject(tempObjectToInsert)
