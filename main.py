import sys
import json
from PyQt5 import QtWidgets

from Models.modelClasses import Workspace
from views.databaseConfigWindow import Ui_databaseConfig_window
from views.deleteConfirmationWindow import Ui_deleteConfirmation_window
from views.workspace import Ui_workspace_window
from Controllers.AnalysisManager import SDSAnalysisManager
from Controllers.CaptureController import CaptureController
from Controllers.SDSController import SDSController
from Database.DatabaseHelper import SDSDatabaseHelper

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


workspaceUI.setupWorkspaceUI(workspace_Window, sds_controller)

assert_database_connection()

sys.exit(app.exec_())
