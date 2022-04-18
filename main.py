import sys
from PyQt5 import QtWidgets

from Database.databaseFunctions import connect_subsystems_and_database, set_up_database_connection
from Models.modelClasses import Workspace
from views.databaseConfigWindow import Ui_databaseConfig_window
from views.deleteConfirmationWindow import Ui_deleteConfirmation_window
from views.workspace import Ui_workspace_window
from Controllers.SDSController import SDSController

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


def delete_selection():
    pass


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
