import json
import time

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QAction, QTreeWidgetItem

from views.analysisManagerWindow import Ui_AnalysisManagerWindow
from views.captureManagerWindow import Ui_CaptureManagerWindow
from views.createWorkspace import Ui_newWorkspace_window
from views.databaseConfigWindow import Ui_databaseConfig_window


# IMPLEMENT THIS. Doesn't show analysis manager window
def analysisManagerWindow(workspace_Window):
    analysisManager_Window = QtWidgets.QMainWindow()
    analysisManagerWindowUI = Ui_AnalysisManagerWindow()
    analysisManagerWindowUI.setupAnalysisManager(analysisManager_Window)
    analysisManager_Window.show()
    workspace_Window.close()


def databaseConfigWindow():
    databaseConfig_Window = QtWidgets.QDialog()
    databaseConfigWindowUI = Ui_databaseConfig_window()
    databaseConfigWindowUI.setupDatabaseConfig(databaseConfig_Window)
    with open('conf/db_config.json') as mongo_ip_file:
        database_ip_dict = json.load(mongo_ip_file)
        ip = database_ip_dict['ip']
        databaseConfigWindowUI.databaseConfigIPInput_databaseConfigWindow.setText(ip)
        port = database_ip_dict['port']
        databaseConfigWindowUI.databaseConfigPortInput_databaseConfigWindow.setText(port)
    databaseConfig_Window.show()


class Ui_workspace_window(object):
    def setupWorkspaceUI(self, workspace_window, sds_controller):
        self.sds_controller = sds_controller
        workspace_window.setWindowIcon(QtGui.QIcon('network.png'))
        workspace_window.setObjectName("workspace_window")
        workspace_window.resize(780, 463)
        workspace_window.setMinimumSize(QtCore.QSize(780, 463))
        workspace_window.setMaximumSize(QtCore.QSize(780, 463))
        self.gridLayout = QtWidgets.QGridLayout(workspace_window)
        self.gridLayout.setObjectName("gridLayout")
        self.mainLayout_workspaceWindow = QtWidgets.QHBoxLayout()
        self.mainLayout_workspaceWindow.setObjectName("mainLayout_workspaceWindow")
        self.workspacesLayout_workspaceWindow = QtWidgets.QHBoxLayout()
        self.workspacesLayout_workspaceWindow.setObjectName("workspacesLayout_workspaceWindow")
        self.workspacesList_workspaceWindow = QtWidgets.QTreeWidget(workspace_window)
        self.workspacesList_workspaceWindow.setObjectName("workspacesList_workspaceWindow")
        self.workspacesLayout_workspaceWindow.addWidget(self.workspacesList_workspaceWindow)
        self.mainLayout_workspaceWindow.addLayout(self.workspacesLayout_workspaceWindow)
        self.createWorkspaceLayout_workspaceWindow = QtWidgets.QVBoxLayout()
        self.createWorkspaceLayout_workspaceWindow.setObjectName("createWorkspaceLayout_workspaceWindow")
        self.logoLayout_workspaceWindow = QtWidgets.QHBoxLayout()
        self.logoLayout_workspaceWindow.setObjectName("logoLayout_workspaceWindow")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.logoLayout_workspaceWindow.addItem(spacerItem)
        self.logoLabel_workspaceWindow = QtWidgets.QLabel(workspace_window)
        self.logoLabel_workspaceWindow.setObjectName("logoLabel_workspaceWindow")
        self.logoLayout_workspaceWindow.addWidget(self.logoLabel_workspaceWindow)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.logoLayout_workspaceWindow.addItem(spacerItem1)
        self.createWorkspaceLayout_workspaceWindow.addLayout(self.logoLayout_workspaceWindow)
        self.SDSLayout_workspaceWindow = QtWidgets.QHBoxLayout()
        self.SDSLayout_workspaceWindow.setObjectName("SDSLayout_workspaceWindow")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.SDSLayout_workspaceWindow.addItem(spacerItem2)
        self.SDSLabel_workspaceWindow = QtWidgets.QLabel(workspace_window)
        self.SDSLabel_workspaceWindow.setObjectName("SDSLabel_workspaceWindow")
        self.SDSLayout_workspaceWindow.addWidget(self.SDSLabel_workspaceWindow)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.SDSLayout_workspaceWindow.addItem(spacerItem3)
        self.createWorkspaceLayout_workspaceWindow.addLayout(self.SDSLayout_workspaceWindow)
        self.versionLayout_workspaceWindow = QtWidgets.QHBoxLayout()
        self.versionLayout_workspaceWindow.setObjectName("versionLayout_workspaceWindow")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.versionLayout_workspaceWindow.addItem(spacerItem4)
        self.versionLabel_workspaceWindow = QtWidgets.QLabel(workspace_window)
        self.versionLabel_workspaceWindow.setObjectName("versionLabel_workspaceWindow")
        self.versionLayout_workspaceWindow.addWidget(self.versionLabel_workspaceWindow)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.versionLayout_workspaceWindow.addItem(spacerItem5)
        self.createWorkspaceLayout_workspaceWindow.addLayout(self.versionLayout_workspaceWindow)
        self.createWorkspaceButton_workspaceWindow = QtWidgets.QPushButton(workspace_window)
        self.createWorkspaceButton_workspaceWindow.setObjectName("createWorkspaceButton_workspaceWindow")
        self.createWorkspaceLayout_workspaceWindow.addWidget(self.createWorkspaceButton_workspaceWindow)

        self.analysisManagerButton_workspaceWindow = QtWidgets.QPushButton(workspace_window)
        self.analysisManagerButton_workspaceWindow.setObjectName("analysisManagerButton_workspaceWindow")
        self.createWorkspaceLayout_workspaceWindow.addWidget(self.analysisManagerButton_workspaceWindow)

        self.dbConfigButton_workspaceWindow = QtWidgets.QPushButton(workspace_window)
        self.dbConfigButton_workspaceWindow.setObjectName("dbConfigButton_workspaceWindow")
        self.createWorkspaceLayout_workspaceWindow.addWidget(self.dbConfigButton_workspaceWindow)

        self.mainLayout_workspaceWindow.addLayout(self.createWorkspaceLayout_workspaceWindow)
        self.gridLayout.addLayout(self.mainLayout_workspaceWindow, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(workspace_window)

        _translate = QtCore.QCoreApplication.translate
        workspace_window.setWindowTitle(_translate("workspace_window", "Scan Detection System"))
        self.workspacesList_workspaceWindow.headerItem().setText(0, _translate("workspace_window", "Workspaces"))
        __sortingEnabled = self.workspacesList_workspaceWindow.isSortingEnabled()
        self.workspacesList_workspaceWindow.setSortingEnabled(False)
        self.workspacesList_workspaceWindow.setSortingEnabled(__sortingEnabled)

        self.logoLabel_workspaceWindow.setPixmap(QPixmap('img/network.png'))
        self.SDSLabel_workspaceWindow.setText(_translate("workspace_window", "Scan Detection System"))
        self.versionLabel_workspaceWindow.setText(_translate("workspace_window", "Version 2022.1.0"))
        self.createWorkspaceButton_workspaceWindow.setText(_translate("workspace_window", "Create New Workspace"))
        self.analysisManagerButton_workspaceWindow.setText(_translate("workspace_window", "Analysis Manager"))
        self.dbConfigButton_workspaceWindow.setText(_translate("workspace_window", "Database Configuration"))

        self.workspacesList_workspaceWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.workspacesList_workspaceWindow.customContextMenuRequested.connect(self.context_menu_workspace)

        self.analysisManagerButton_workspaceWindow.clicked.connect(lambda: analysisManagerWindow(workspace_window))
        self.workspacesList_workspaceWindow.doubleClicked.connect(lambda: self.open_workspace(workspace_window))

        self.createWorkspaceButton_workspaceWindow.clicked.connect(lambda: self.createWorkspaceWindow(workspace_window))
        self.dbConfigButton_workspaceWindow.clicked.connect(databaseConfigWindow)

    def context_menu_workspace(self, point):
        index = self.workspacesList_workspaceWindow.indexAt(point)
        if not index.isValid() or index.parent().isValid():
            return
        item = self.workspacesList_workspaceWindow.itemAt(point)
        name = item.text(0)
        menu = QtWidgets.QMenu()

        action_edit_workspace = QAction("Edit Workspace Name")
        action_delete_workspace = QAction("Delete Workspace")

        menu.addAction(action_edit_workspace)
        menu.addAction(action_delete_workspace)

        # action_edit_workspace.triggered.connect(lambda: edit_workspace(name))
        action_delete_workspace.triggered.connect(lambda: self.delete_workspace(name))

        menu.exec_(self.workspacesList_workspaceWindow.mapToGlobal(point))

    # TODO: Implement this
    def delete_workspace(self, selected_workspace):
        """ Removes the workspace. If projects don't exist in other workspaces then
        they will be deleted. Same rule for the scenarios and nodes."""
        self.sds_controller.delete_workspace_contents(selected_workspace)

    def open_workspace(self, workspace_Window):
        selected_workspace = self.workspacesList_workspaceWindow.selectedItems()[0].text(0)
        current_workspace_name = selected_workspace
        # Change sds_controller workspace context
        # print(f'check if open_workspace is called')
        self.sds_controller.change_workspace_context(current_workspace_name)
        time.sleep(1)
        captureManager_Window = QtWidgets.QMainWindow()
        captureManagerWindowUI = Ui_CaptureManagerWindow()
        captureManagerWindowUI.setupCaptureManager(captureManager_Window, self.sds_controller)
        captureManager_Window.setWindowTitle(selected_workspace + ' - Scan Detection System')
        captureManager_Window.show()
        workspace_Window.close()
        # Get all project names related to workspace
        project_names = self.sds_controller.list_all_projects(selected_workspace)
        for project_name in project_names:
            # Make TreeWidgetItem
            project_tree_item = QTreeWidgetItem([project_name])
            # Get all scenarios related to workspace and project
            scenario_names = self.sds_controller.list_all_scenario_units(selected_workspace, project_name)
            for scenario_name in scenario_names:
                # Make TreeWidgetItem
                scenario_tree = QTreeWidgetItem([scenario_name])
                # Add scenario tree to project tree
                project_tree_item.addChild(scenario_tree)
            captureManagerWindowUI.projectsList_captureManagerWindow.addTopLevelItem(project_tree_item)

        captureManagerWindowUI.projectsList_captureManagerWindow.expandAll()
        # Insert core options if saved
    #    captureManagerWindowUI.corePortNumberInput_captureManagerWindow.setText(sds_controller.get_core_port())
    #   captureManagerWindowUI.coreSdsServiceInput_captureManagerWindow.setText(sds_controller.get_core_ip())

    def createWorkspaceWindow(self, workspace_window):
        createWorkspace_Window = QtWidgets.QDialog()
        createWorkspaceUI = Ui_newWorkspace_window()
        createWorkspaceUI.setupCreateWorkspace(createWorkspace_Window, workspace_window, self.sds_controller)
        self.sds_controller.start_new_workplace()
        createWorkspace_Window.show()

