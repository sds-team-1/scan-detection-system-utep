import json

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QAction, QTreeWidgetItem, QFileDialog
from Models.modelClasses import Workspace

from views.addNodeWindow import Ui_addNode_window
from views.newProject import Ui_newProject_window
from views.newScenarioUnitWindow import Ui_newScenarioUnit_window
from views.setNodesWindow import Ui_addSetNodes_window

import Database.DatabaseHelper

class Ui_CaptureManagerWindow(object):
    
    workspace_object : Workspace
    db_helper:Database.DatabaseHelper.SDSDatabaseHelper

    def __init__(self, db_helper:Database.DatabaseHelper.SDSDatabaseHelper, workspace_object:Workspace):
        self.db_helper = db_helper
        self.workspace_object = workspace_object

    def setupCaptureManager(self, CaptureManagerWindow, workspace_Window):
        self.InitialWorkspaceWindow = workspace_Window
        self.ip_counter = 0
        self.id_counter = 10
        self.MAC = 1000000000000

        CaptureManagerWindow.setObjectName("CaptureManagerWindow")
        CaptureManagerWindow.resize(1200, 700)
        CaptureManagerWindow.setMinimumSize(QtCore.QSize(1200, 700))
        self.CentralLayout_captureManagerWindow = QtWidgets.QWidget(CaptureManagerWindow)
        self.CentralLayout_captureManagerWindow.setObjectName("CentralLayout_captureManagerWindow")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.CentralLayout_captureManagerWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonsLayout_captureManagerWindow = QtWidgets.QHBoxLayout()
        self.buttonsLayout_captureManagerWindow.setObjectName("buttonsLayout_captureManagerWindow")

        self.projectButtonsLabel = QtWidgets.QLabel(self.CentralLayout_captureManagerWindow)
        self.projectButtonsLabel.setObjectName("projectButtonsLabel")
        self.buttonsLayout_captureManagerWindow.addWidget(self.projectButtonsLabel)
        
        self.newButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.newButton_captureManagerWindow.setObjectName("newButton_captureManagerWindow")
        self.buttonsLayout_captureManagerWindow.addWidget(self.newButton_captureManagerWindow)
        self.saveButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.saveButton_captureManagerWindow.setObjectName("saveButton_captureManagerWindow")
        self.buttonsLayout_captureManagerWindow.addWidget(self.saveButton_captureManagerWindow)
        self.importButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.importButton_captureManagerWindow.setObjectName("importButton_captureManagerWindow")
        self.buttonsLayout_captureManagerWindow.addWidget(self.importButton_captureManagerWindow)
        self.exportButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.exportButton_captureManagerWindow.setObjectName("exportButton_captureManagerWindow")
        self.buttonsLayout_captureManagerWindow.addWidget(self.exportButton_captureManagerWindow)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout_captureManagerWindow.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.buttonsLayout_captureManagerWindow, 0, 0, 1, 1)
        self.centralSectionLayout_captureManagerWindow = QtWidgets.QHBoxLayout()
        self.centralSectionLayout_captureManagerWindow.setObjectName("centralSectionLayout_captureManagerWindow")
        self.projectsList_captureManagerWindow = QtWidgets.QTreeWidget(self.CentralLayout_captureManagerWindow)
        self.projectsList_captureManagerWindow.setMinimumSize(QtCore.QSize(220, 0))
        self.projectsList_captureManagerWindow.setMaximumSize(QtCore.QSize(220, 16777215))
        self.projectsList_captureManagerWindow.setObjectName("projectsList_captureManagerWindow")
        self.centralSectionLayout_captureManagerWindow.addWidget(self.projectsList_captureManagerWindow)
        self.scenarioLayout_captureManagerWindow = QtWidgets.QVBoxLayout()
        self.scenarioLayout_captureManagerWindow.setObjectName("scenarioLayout_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow = QtWidgets.QHBoxLayout()
        self.scenarioRunLayout_captureManagerWindow.setObjectName("scenarioRunLayout_captureManagerWindow")
        self.scenarioIterationsLabel_captureManagerWindow = QtWidgets.QLabel(self.CentralLayout_captureManagerWindow)
        self.scenarioIterationsLabel_captureManagerWindow.setObjectName("scenarioIterationsLabel_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.scenarioIterationsLabel_captureManagerWindow)

        self.scenarioIterationsSpinbox_captureManagerWindow = QtWidgets.QSpinBox(self.CentralLayout_captureManagerWindow)
        self.scenarioIterationsSpinbox_captureManagerWindow.setObjectName("scenarioIterationsSpinbox_captureManagerWindow")
        self.scenarioIterationsSpinbox_captureManagerWindow.setValue(1)
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.scenarioIterationsSpinbox_captureManagerWindow)

        self.startVirtualMachineButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.startVirtualMachineButton_captureManagerWindow.setObjectName("startVirtualMachineButton_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.startVirtualMachineButton_captureManagerWindow)

        self.shutdownVMButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.shutdownVMButton_captureManagerWindow.setObjectName("shutdownVMButton_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.shutdownVMButton_captureManagerWindow)

        self.runScenarioButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.runScenarioButton_captureManagerWindow.setObjectName("runScenarioButton_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.runScenarioButton_captureManagerWindow)

        self.stopRestoreScenarioButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.stopRestoreScenarioButton_captureManagerWindow.setObjectName("stopScenarioButton_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.stopRestoreScenarioButton_captureManagerWindow)

        # self.restoreScenarioButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        # self.restoreScenarioButton_captureManagerWindow.setObjectName("restoreScenarioButton_captureManagerWindow")
        # self.scenarioRunLayout_captureManagerWindow.addWidget(self.restoreScenarioButton_captureManagerWindow)

        self.closeWorkspaceButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.closeWorkspaceButton_captureManagerWindow.setObjectName("closeWorkspaceButton_captureManagerWindow")
        self.scenarioRunLayout_captureManagerWindow.addWidget(self.closeWorkspaceButton_captureManagerWindow)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.scenarioRunLayout_captureManagerWindow.addItem(spacerItem1)
        self.scenarioLayout_captureManagerWindow.addLayout(self.scenarioRunLayout_captureManagerWindow)
        self.nodesList_captureManagerWindow = QtWidgets.QTreeWidget(self.CentralLayout_captureManagerWindow)
        self.nodesList_captureManagerWindow.setObjectName("nodesList_captureManagerWindow")
        self.scenarioLayout_captureManagerWindow.addWidget(self.nodesList_captureManagerWindow)
        self.nodeLayout_captureManagerWindow = QtWidgets.QHBoxLayout()
        self.nodeLayout_captureManagerWindow.setObjectName("nodeLayout_captureManagerWindow")
        self.scenarioStatusLabel_captureManagerWindow = QtWidgets.QLabel(self.CentralLayout_captureManagerWindow)
        self.scenarioStatusLabel_captureManagerWindow.setObjectName("scenarioStatusLabel_captureManagerWindow")
        self.nodeLayout_captureManagerWindow.addWidget(self.scenarioStatusLabel_captureManagerWindow)
        self.scenarioStatus_captureManagerWindow = QtWidgets.QLabel(self.CentralLayout_captureManagerWindow)
        self.scenarioStatus_captureManagerWindow.setObjectName("scenarioStatus_captureManagerWindow")
        self.nodeLayout_captureManagerWindow.addWidget(self.scenarioStatus_captureManagerWindow)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.nodeLayout_captureManagerWindow.addItem(spacerItem2)
        self.addNodeButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.addNodeButton_captureManagerWindow.setObjectName("addNodeButton_captureManagerWindow")
        self.nodeLayout_captureManagerWindow.addWidget(self.addNodeButton_captureManagerWindow)
        self.addSetNodeButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.addSetNodeButton_captureManagerWindow.setObjectName("addSetNodeButton_captureManagerWindow")
        self.nodeLayout_captureManagerWindow.addWidget(self.addSetNodeButton_captureManagerWindow)
        self.scenarioLayout_captureManagerWindow.addLayout(self.nodeLayout_captureManagerWindow)
        self.centralSectionLayout_captureManagerWindow.addLayout(self.scenarioLayout_captureManagerWindow)
        self.gridLayout_2.addLayout(self.centralSectionLayout_captureManagerWindow, 1, 0, 1, 1)
        CaptureManagerWindow.setCentralWidget(self.CentralLayout_captureManagerWindow)
        self.exportButton_captureManagerWindow.setEnabled(False)

        QtCore.QMetaObject.connectSlotsByName(CaptureManagerWindow)

        _translate = QtCore.QCoreApplication.translate
        CaptureManagerWindow.setWindowTitle(_translate("CaptureManagerWindow", "Scan Detection System"))
        self.newButton_captureManagerWindow.setToolTip(_translate("CaptureManagerWindow", "New Project"))
        self.projectButtonsLabel.setText(_translate("CaptureManagerWindow", "  Project Functions  "))
        self.newButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "  New  "))
        self.saveButton_captureManagerWindow.setToolTip(_translate("CaptureManagerWindow", "Save Project"))
        self.saveButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "  Save  "))
        self.importButton_captureManagerWindow.setToolTip(_translate("CaptureManagerWindow", "Import Project"))
        self.importButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Import"))
        self.exportButton_captureManagerWindow.setToolTip(_translate("CaptureManagerWindow", "Export Project"))
        self.exportButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Export"))
        self.projectsList_captureManagerWindow.headerItem().setText(0, _translate("CaptureManagerWindow", "Projects"))
        __sortingEnabled = self.projectsList_captureManagerWindow.isSortingEnabled()
        self.projectsList_captureManagerWindow.setSortingEnabled(False)
        self.projectsList_captureManagerWindow.setSortingEnabled(__sortingEnabled)
        self.scenarioIterationsLabel_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Scenario Iterations:   "))

        self.startVirtualMachineButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Start VM"))
        self.shutdownVMButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Shutdown VM"))

        self.runScenarioButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Run Scenario"))
        self.stopRestoreScenarioButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Stop/Restore Scenario"))
        #self.restoreScenarioButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Restore State"))
        self.closeWorkspaceButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Close Workspace"))
        self.nodesList_captureManagerWindow.headerItem().setText(0, _translate("CaptureManagerWindow", "Log Net Traffic"))
        self.nodesList_captureManagerWindow.headerItem().setText(1, _translate("CaptureManagerWindow", "Type"))
        self.nodesList_captureManagerWindow.headerItem().setText(2, _translate("CaptureManagerWindow", "Name"))
        self.nodesList_captureManagerWindow.headerItem().setText(3, _translate("CaptureManagerWindow", "MAC"))
        self.nodesList_captureManagerWindow.headerItem().setText(4, _translate("CaptureManagerWindow", "IP"))
        #self.nodesList_captureManagerWindow.headerItem().setText(6, _translate("CaptureManagerWindow", "Port"))
        self.nodesList_captureManagerWindow.headerItem().setText(5, _translate("CaptureManagerWindow", "Scanner/Victim"))
        self.scenarioStatusLabel_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Status:"))
        self.scenarioStatus_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Active"))
        self.addNodeButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "    Add Node    "))
        self.addSetNodeButton_captureManagerWindow.setText(_translate("CaptureManagerWindow", "Set of Victim Nodes"))

        # Temporarily having all buttons enabled
        # self.startVirtualMachineButton_captureManagerWindow.setEnabled(False)
        # self.runScenarioButton_captureManagerWindow.setEnabled(False)
        # self.stopScenarioButton_captureManagerWindow.setEnabled(False)
        # self.restoreScenarioButton_captureManagerWindow.setEnabled(False)
        self.addNodeButton_captureManagerWindow.setEnabled(False)
        self.addSetNodeButton_captureManagerWindow.setEnabled(False)

        # Project button functions
        self.newButton_captureManagerWindow.clicked.connect(self.createProjectWindow)
        self.saveButton_captureManagerWindow.clicked.connect(self.save_workspace)
        self.exportButton_captureManagerWindow.clicked.connect(self.export_project)
        self.importButton_captureManagerWindow.clicked.connect(lambda: self.import_project(CaptureManagerWindow))

        # CAUSED AN ERROR!! Method doesn't exist
        # self.startServicesButton_captureManagerWindow.clicked.connect(lambda: start_services())

        # Virtual Machine button functions
        self.startVirtualMachineButton_captureManagerWindow.clicked.connect(self.start_virtual_machine)
        self.shutdownVMButton_captureManagerWindow.clicked.connect(self.shutdown_virtual_machine)

        # Scenario button functions
        self.runScenarioButton_captureManagerWindow.clicked.connect(self.set_up_scenario_unit)
        self.stopRestoreScenarioButton_captureManagerWindow.clicked.connect(
            lambda: self.stop_restore_unit())

        self.projectsList_captureManagerWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.nodesList_captureManagerWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.projectsList_captureManagerWindow.customContextMenuRequested.connect(self.context_menu_project)
        self.nodesList_captureManagerWindow.customContextMenuRequested.connect(self.context_menu_node)
        self.projectsList_captureManagerWindow.itemSelectionChanged.connect(self.item_project_selected)

        self.closeWorkspaceButton_captureManagerWindow.clicked.connect(lambda: self.closeCaptureManager(
            CaptureManagerWindow))

        # Node button functions
        self.addNodeButton_captureManagerWindow.clicked.connect(self.addNodeWindow)
        self.addSetNodeButton_captureManagerWindow.clicked.connect(self.addSetNodesWindow)

        CaptureManagerWindow.closeEvent = self.CloseEvent

        self.generate_projects()


    def generate_projects(self):
        self.projectsList_captureManagerWindow.clear()
        for project in self.workspace_object.projects:
            # Make TreeWidgetItem
            project_tree_item = QTreeWidgetItem([project.name])
            for scenario in project.scenarios:
                scenario_tree = QTreeWidgetItem([scenario.name])
                project_tree_item.addChild(scenario_tree)
            self.projectsList_captureManagerWindow.addTopLevelItem(project_tree_item)
            # Get all scenarios related to workspace and project
          #  scenario_names = self.sds_controller.list_all_scenario_units(selected_workspace, project_name)
         #   for scenario_name in scenario_names:
                # Make TreeWidgetItem
                #scenario_tree = QTreeWidgetItem([scenario_name])
                # Add scenario tree to project tree
               # project_tree_item.addChild(scenario_tree)
           # captureManagerWindowUI.projectsList_captureManagerWindow.addTopLevelItem(project_tree_item)


    def context_menu_project(self, point):
        index = self.projectsList_captureManagerWindow.indexAt(point)

        if not index.isValid():
            return

        if not index.isValid() or index.parent().isValid():
            item = self.projectsList_captureManagerWindow.itemAt(point)
            if not item:
                return
            name = item.text(0)

            menu = QtWidgets.QMenu()
            action_edit_scenario_unit = QAction("Rename Scenario Unit")
            action_delete_scenario_unit = QAction("Delete Scenario Unit")

            menu.addAction(action_edit_scenario_unit)
            menu.addAction(action_delete_scenario_unit)

            action_edit_scenario_unit.triggered.connect(lambda: self.edit_scenario_unit(name))
            action_delete_scenario_unit.triggered.connect(lambda: self.delete_scenario_unit(name))

            menu.exec_(self.projectsList_captureManagerWindow.mapToGlobal(point))

            return

        if not index.isValid() or not index.parent().isValid():
            item = self.projectsList_captureManagerWindow.itemAt(point)
            name = item.text(0)

            menu = QtWidgets.QMenu()
            action_add_scenario = QAction("Add Scenario Unit")
            action_load_scenario = QAction("Load Scenario Unit")
            action_edit_project = QAction("Rename Project")
            action_delete_project = QAction("Delete Project")

            menu.addAction(action_add_scenario)
            menu.addAction(action_load_scenario)
            menu.addAction(action_edit_project)
            menu.addAction(action_delete_project)

            action_add_scenario.triggered.connect(self.newScenarioUnitWindow)
            action_load_scenario.triggered.connect(self.load_scenario_unit)
            action_edit_project.triggered.connect(lambda: self.edit_project(name))
            action_delete_project.triggered.connect(lambda: self.delete_project(name))

            menu.exec_(self.projectsList_captureManagerWindow.mapToGlobal(point))

            return

    def load_scenario_unit(self):
        pass

    #TODO: Start the UI dialog
    def edit_project(self, selected_project):
        '''Starts the UI and edits the project'''
        pass

    def delete_project(self, selected_project):
        pass

    #TODO: Start the UI dialog
    def edit_scenario_unit(self, selected_scenario_unit):
        ''' Starts the UI and edits the scenario unit.'''
        pass

    def delete_scenario_unit(self, selected_scenario_unit):
        pass

    def newScenarioUnitWindow(self):
        newScenarioUnit_Window = QtWidgets.QDialog()
        newScenarioUnitWindowUI = Ui_newScenarioUnit_window()
        newScenarioUnitWindowUI.setupNewScenarioUnit(newScenarioUnit_Window,
                                                     self.projectsList_captureManagerWindow,
                                                     self.scenarioIterationsSpinbox_captureManagerWindow)
        newScenarioUnit_Window.show()

    def context_menu_node(self, point):
        index = self.nodesList_captureManagerWindow.indexAt(point)

        if not index.isValid():
            return

        if not index.isValid() or index.parent().isValid():
            item = self.nodesList_captureManagerWindow.itemAt(point)
            if not item:
                return
            name = item.text(2)

            menu = QtWidgets.QMenu()
            action_edit_node = QAction("Edit Node")
            action_delete_node = QAction("Delete Node")

            menu.addAction(action_edit_node)
            menu.addAction(action_delete_node)

            action_edit_node.triggered.connect(lambda: self.edit_node(name))
            action_delete_node.triggered.connect(lambda: self.delete_node(name))

            menu.exec_(self.nodesList_captureManagerWindow.mapToGlobal(point))

            return

    #TODO: Add the UI and functionality.
    def edit_node(self, selected_node):
        '''Starts the UI window for editing a node then changes it for the db.'''
        pass

    def delete_node(self, selected_node):
        pass
    def item_project_selected(self):
        # print(f'checking if item_project_selected went inside')
        # Clear the window
        self.nodesList_captureManagerWindow.clear()
        # if self.projectsList_captureManagerWindow.selectedItems()[0].parent() is None:
        #     # This condition is for projects. Works with the project list which...
        #     # contains projects and scenarios
        #     # TODO: Check add node button(I was not able to create a project)
        #     self.exportButton_captureManagerWindow.setEnabled(True)
        #     self.addNodeButton_captureManagerWindow.setEnabled(False)
        #     self.addSetNodeButton_captureManagerWindow.setEnabled(False)
        #     # self.startVirtualMachineButton_captureManagerWindow.setEnabled(False)
        #     # self.stopScenarioButton_captureManagerWindow.setEnabled(False)
        #     # self.restoreScenarioButton_captureManagerWindow.setEnabled(False)
        # else:
        #     # print(f'checking if else checked')
        #     self.exportButton_captureManagerWindow.setEnabled(False)
        #     self.addNodeButton_captureManagerWindow.setEnabled(True)
        #     self.addSetNodeButton_captureManagerWindow.setEnabled(True)
        #     # self.startVirtualMachineButton_captureManagerWindow.setEnabled(True)
        #     # self.stopScenarioButton_captureManagerWindow.setEnabled(True)
        #     # self.restoreScenarioButton_captureManagerWindow.setEnabled(True)
        #     # Get all the nodes


        # scenario_ID = self.projectsList_captureManagerWindow.selectedItems()[0].text(0)
        # print(f'checking scenario id: {scenario_ID}')
    
        #        captureManagerWindowUI.vmSdsServiceInput_captureManagerWindow.setText(vm_ip)
        #       captureManagerWindowUI.dockerSdsServiceInput_captureManagerWindow.setText(docker_ip)
        # print(f'checking if nodes list is anything: {node_list}')
        # Insert all the nodes into the UI


        self.nodesList_captureManagerWindow.header().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)

    def start_virtual_machine(self):
        pass
        # Get input
        # store input into workspace
       
        # self.runScenarioButton_captureManagerWindow.setEnabled(True)
        # self.startVirtualMachineButton_captureManagerWindow.setEnabled(False)

    def shutdown_virtual_machine(self):
        print("shutdown virtual machine")

        # self.startVirtualMachineButton_captureManagerWindow.setEnabled(True)

    def stop_scenario_unit(self):
        # self.vmSdsServiceInput_captureManagerWindow.setEnabled(True)
        # self.dockerSdsServiceInput_captureManagerWindow.setEnabled(True)
        # self.runScenarioButton_captureManagerWindow.setEnabled(True)
        pass

    def restore_scenario_unit(self):
        pass

    def stop_restore_unit(self):
        pass

    def start_services(self):
        pass

    def set_up_scenario_unit(self):
        scenario_name = self.projectsList_captureManagerWindow.selectedItems()[0].text(0)
        # vm_ip = self.vmSdsServiceInput_captureManagerWindow.text()
        # docker_ip = self.dockerSdsServiceInput_captureManagerWindow.text()
        # self.vmSdsServiceInput_captureManagerWindow.setEnabled(False)
        # self.dockerSdsServiceInput_captureManagerWindow.setEnabled(False)
        # self.runScenarioButton_captureManagerWindow.setEnabled(False)

    def save_workspace(self):
        # Everything is already saved. So we don't really need it. YW
        pass

    def export_project(self):
        project_name = self.projectsList_captureManagerWindow.selectedItems()[0].text(0)
        export_path = QFileDialog().getSaveFileName(caption='Export Project', directory='~/untitled.json')
        print(f'export path is: {export_path}')

    def import_project(self, captureManager_Window):
        dialog = QFileDialog()
        json_path = dialog.getOpenFileName(captureManager_Window, 'Select JSON File', filter='*.json')
        if not json_path[0]:
            return
        with open(json_path[0]) as json_file:
            project = json.load(json_file)
   

    def createProjectWindow(self):
        newProject_Window = QtWidgets.QDialog()
        newProjectWindowUI = Ui_newProject_window()
        newProjectWindowUI.setupNewProject(
            newProject_Window, self)
        newProject_Window.show()

    def addNodeWindow(self):
        addNode_Window = QtWidgets.QDialog()
        addNodeWindowUI = Ui_addNode_window()
        addNodeWindowUI.setupAddNode(addNode_Window,
                                     self.projectsList_captureManagerWindow, self.nodesList_captureManagerWindow,
                                     self.CentralLayout_captureManagerWindow,
                                     self.ip_counter, self.MAC, self.id_counter)
        addNode_Window.show()

    def addSetNodesWindow(self):
        addSetNodes_Window = QtWidgets.QDialog()
        addSetNodesWindowUI = Ui_addSetNodes_window()
        addSetNodesWindowUI.setupAddSetNodes(addSetNodes_Window,
                                             self.projectsList_captureManagerWindow, self.nodesList_captureManagerWindow,
                                             self.ip_counter, self.MAC, self.id_counter)
        addSetNodes_Window.show()


    def closeCaptureManager(self, CaptureManagerWindow):
        CaptureManagerWindow.close()
        self.InitialWorkspaceWindow.show()


    def CloseEvent(self, event):
        self.InitialWorkspaceWindow.show()