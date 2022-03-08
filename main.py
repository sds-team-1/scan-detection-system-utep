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

client = MongoClient("mongodb+srv://admin:sp22SEP@sds.p5j7n.mongodb.net/SDS?retryWrites=true&w=majority")

db = client.test

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

if 'SDS_DB' not in dbs:
    workspace = {'_id': 0, 'Name': '', 'Location': '', 'Projects': {}}
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
    first_query = workspaces_DB.find_one()
    if first_query['Name'] == '':
        new_query = {'$set': {'Name': createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text(),
                              'Location': createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.text()}}
        workspaces_DB.update_one(first_query, new_query)
    else:
        current_id = workspaces_DB.find().sort('_id', -1).limit(1)
        for doc in current_id:
            current_id = doc['_id']

        new_query = {'_id': int(current_id + 1),
                     'Name': createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text(),
                     'Location': createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.text(),
                     'Projects': {}}

        workspaces_DB.insert_one(new_query)

    os.makedirs(os.path.join(workspace_path, createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text()))

    mainWindow_Window.show()
    createWorkspace_Window.close()
    workspace_Window.close()


def createProjectWindow():
    newProject_Window.show()


def define_workspace_path():
    global workspace_path
    dialog = QFileDialog()
    workspace_path = dialog.getExistingDirectory(createWorkspace_Window, 'Select Workspace Directory')
    createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.setText(workspace_path)


def item_selected():
    if workspaceUI.workspacesList_workspaceWindow.selectedItems()[0].parent() is None:
        print(workspaceUI.workspacesList_workspaceWindow.selectedItems()[0].text(0))
        time.sleep(1)
        mainWindow_Window.show()
        workspace_Window.close()


workspaceUI.createWorkspaceButton_workspaceWindow.clicked.connect(createWorkspaceWindow)

createWorkspaceUI.createWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace)
createWorkspaceUI.cancelWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace_Window.close)
createWorkspaceUI.browseWorkspaceButton_newWorkspaceWindow.clicked.connect(define_workspace_path)
mainWindowUI.newButton_mainWindow.clicked.connect(createProjectWindow)
workspaceUI.workspacesList_workspaceWindow.itemSelectionChanged.connect(item_selected)

workspace_Window.show()

sys.exit(app.exec_())

# example of how to insert a document into mongo
# SDSdb = DatabaseHelper.SDSDatabaseHelper()
# tempObjectToInsert = {}
# tempObjectToInsert['name'] = 'Test'
# tempObjectToInsert['type'] = 'test type'
# tempObjectToInsert['_id'] = random.randint(1, 100)
# SDSdb.insertObject(tempObjectToInsert)
