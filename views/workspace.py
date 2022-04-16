from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QAction


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
