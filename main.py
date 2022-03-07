from random import random
from PyQt5 import QtCore, QtGui, QtWidgets
#from Helpers import DatabaseHelper as DatabaseHelper
import random

from PyQt5 import QtWidgets
import sys

from views.createWorkspace import Ui_newWorkspace_window
from views.mainWindow import Ui_MainWindow
from views.newProject import Ui_newProject_window
from views.workspace import Ui_workspace_window

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


def createWorkspaceWindow():
    createWorkspace_Window.show()


def createWorkspace():
    print(createWorkspaceUI.workspaceNameInput_newWorkspaceWindow.text())
    print(createWorkspaceUI.workspaceLocationInput_newWorkspaceWindow.text())
    mainWindow_Window.show()
    createWorkspace_Window.close()
    workspace_Window.close()


def createProjectWindow():
    newProject_Window.show()


workspaceUI.createWorkspaceButton_workspaceWindow.clicked.connect(createWorkspaceWindow)

createWorkspaceUI.createWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace)
createWorkspaceUI.cancelWorkspaceButton_newWorkspaceWindow.clicked.connect(createWorkspace_Window.close)
mainWindowUI.newButton_mainWindow.clicked.connect(createProjectWindow)

workspace_Window.show()

sys.exit(app.exec_())



    # example of how to insert a document into mongo
    # SDSdb = DatabaseHelper.SDSDatabaseHelper()
    # tempObjectToInsert = {}
    # tempObjectToInsert['name'] = 'Test'
    # tempObjectToInsert['type'] = 'test type'
    # tempObjectToInsert['_id'] = random.randint(1, 100)
    # SDSdb.insertObject(tempObjectToInsert)