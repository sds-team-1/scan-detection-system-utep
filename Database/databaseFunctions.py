import json

from Controllers.AnalysisManager import SDSAnalysisManager
from Controllers.CaptureController import CaptureController
from Database.DatabaseHelper import SDSDatabaseHelper

from PyQt5 import QtWidgets


def connect_subsystems_and_database(workspacesList_workspaceWindow, sds_controller, mongo_connection):
    sds_controller.add_mongo_connection(mongo_connection)
    sds_controller.add_capture_manager(CaptureController())
    sds_controller.add_analysis_manager(SDSAnalysisManager())
    # sds controller implementation for filling workspaces
    generate_workspaces_list_window(workspacesList_workspaceWindow, sds_controller)


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


def generate_workspaces_list_window(workspacesList_workspaceWindow, sds_controller):
    workspacesList_workspaceWindow.clear()
    workspaces_c = sds_controller.list_all_workplaces()
    if workspaces_c:
        for workspace_c in workspaces_c:
            l1 = QtWidgets.QTreeWidgetItem([workspace_c])
            workspacesList_workspaceWindow.addTopLevelItem(l1)
