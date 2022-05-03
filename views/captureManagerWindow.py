import json
from logging.config import valid_ident

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QAction, QTreeWidgetItem, QFileDialog, QMainWindow, QDialog, QMessageBox
from Models.modelClasses import Workspace, Project, Scenario, Node

from Controllers.CaptureController import CaptureControllerService

from views.addNodeWindow import Ui_addNode_window
from views.newProjectWindow import Ui_newProject_window
from views.newScenarioUnitWindow import Ui_newScenarioUnit_window
from views.addSetOfNodesWindow import Ui_addSetNodes_window

import Database.DatabaseHelper

class Ui_CaptureManagerWindow(object):
    
    workspace_object : Workspace
    db_helper:Database.DatabaseHelper.SDSDatabaseHelper
    capture_controller: CaptureControllerService

    def __init__(self, db_helper:Database.DatabaseHelper.SDSDatabaseHelper, workspace_object:Workspace, capture_controller:CaptureControllerService):
        self.db_helper = db_helper
        self.workspace_object = workspace_object
        self.capture_controller = capture_controller

    def setupCaptureManager(self, parent_window:QMainWindow, choose_workspace_parent_window:QDialog):
        '''
        Sets up the capture manager UI.
        parent_window: The main window of the application.
        choose_workspace_parent_window: The parent window of the choose workspace dialog. (needed in order to navigate back to the choose workspace dialog)
        '''
        self.ip_counter = 0
        self.id_counter = 10
        self.MAC = 1000000000000

        parent_window.setObjectName("CaptureManagerWindow")
        parent_window.resize(1400, 700)
        parent_window.setMinimumSize(QtCore.QSize(1400, 700))
        parent_window.setWindowTitle(self.workspace_object.name + " - Capture Manager")

        self.CentralLayout_captureManagerWindow = QtWidgets.QWidget(parent_window)
        self.CentralLayout_captureManagerWindow.setObjectName("CentralLayout_captureManagerWindow")
        
        # Label for project functions buttons
        self.q_label_project_functions = QtWidgets.QLabel(self.CentralLayout_captureManagerWindow)
        self.q_label_project_functions.setObjectName("projectButtonsLabel")
        self.q_label_project_functions.setText("Project Functions")

        # Save project button
        self.q_button_save_project = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.q_button_save_project.setObjectName("saveButton_captureManagerWindow")
        self.q_button_save_project.setToolTip("Will save the current state all projects")
        self.q_button_save_project.setText("Save Projects")

        # New Project button
        self.q_button_new_project = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.q_button_new_project.setObjectName("newButton_captureManagerWindow")
        self.q_button_new_project.setToolTip("This will create a new project under the selected workspace")
        self.q_button_new_project.setText("New Project")

        # Import Project button
        self.q_button_import_project = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.q_button_import_project.setObjectName("importButton_captureManagerWindow")
        self.q_button_import_project.setToolTip("Import a project from a json file")
        self.q_button_import_project.setText("Import Project")

        # Export Project button
        self.q_button_export_project = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.q_button_export_project.setObjectName("exportButton_captureManagerWindow")
        self.q_button_export_project.setToolTip("Export a project to a json file")
        self.q_button_export_project.setText("Export Project")

        # Spacer item
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        # Create a row and add the label, buttons, and spacer to it.
        self.q_row_buttons_project_options = QtWidgets.QHBoxLayout()
        self.q_row_buttons_project_options.setObjectName("buttonsLayout_captureManagerWindow")
        self.q_row_buttons_project_options.addWidget(self.q_label_project_functions)
        self.q_row_buttons_project_options.addWidget(self.q_button_save_project)
        self.q_row_buttons_project_options.addWidget(self.q_button_new_project)
        self.q_row_buttons_project_options.addWidget(self.q_button_import_project)
        self.q_row_buttons_project_options.addWidget(self.q_button_export_project)
        self.q_row_buttons_project_options.addItem(spacerItem)


        # Set up a label for scenario iterations
        self.q_label_scenario_iterations = QtWidgets.QLabel(self.CentralLayout_captureManagerWindow)
        self.q_label_scenario_iterations.setObjectName("scenarioIterationsLabel_captureManagerWindow")
        self.q_label_scenario_iterations.setText("Scenario Iterations")

        # Set up a spin box that decides the scenario iterations
        self.q_spin_box_scenario_iterations = QtWidgets.QSpinBox(self.CentralLayout_captureManagerWindow)
        self.q_spin_box_scenario_iterations.setObjectName("scenarioIterationsSpinbox_captureManagerWindow")
        self.q_spin_box_scenario_iterations.setValue(1)

        # Set up a button for start vm
        self.q_button_start_vm = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.q_button_start_vm.setObjectName("startVirtualMachineButton_captureManagerWindow")
        self.q_button_start_vm.setText("Start VM")

        # Button for shutdown vm
        self.q_button_shutdown_vm = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.q_button_shutdown_vm.setObjectName("shutdownVMButton_captureManagerWindow")
        self.q_button_shutdown_vm.setText("Shutdown VM")
        # Disabled by default
        self.q_button_shutdown_vm.setEnabled(False)

        # button for run scenario
        self.q_button_run_scenario = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.q_button_run_scenario.setObjectName("runScenarioButton_captureManagerWindow")
        self.q_button_run_scenario.setText("Run Scenario")

        # Button for stop and restoring
        self.q_button_stop_and_restore_scenario = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.q_button_stop_and_restore_scenario.setObjectName("stopScenarioButton_captureManagerWindow")
        self.q_button_stop_and_restore_scenario.setText("Stop and restore scenario")


        # Button for starting service
        self.q_button_start_services_button = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.q_button_start_services_button.setObjectName("startServicesButton_captureManagerWindow")
        self.q_button_start_services_button.setText("Start Services")


        # Button for clsing the workspace
        # TODO: it is not good ui design to have this button next to the other buttons, perhaps put it somewhere else
        self.q_button_close_workspace_button = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.q_button_close_workspace_button.setObjectName("closeWorkspaceButton_captureManagerWindow")
        self.q_button_close_workspace_button.setText("Close workspace button")
        
        # Spacer item
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)


        # Set up a row and add the label, buttons, and spacer to it.
        self.q_row_scenario_buttons_row = QtWidgets.QHBoxLayout()
        self.q_row_scenario_buttons_row.setObjectName("scenarioRunLayout_captureManagerWindow")
        self.q_row_scenario_buttons_row.addWidget(self.q_label_scenario_iterations)
        self.q_row_scenario_buttons_row.addWidget(self.q_spin_box_scenario_iterations)
        self.q_row_scenario_buttons_row.addWidget(self.q_button_start_vm)
        self.q_row_scenario_buttons_row.addWidget(self.q_button_shutdown_vm)
        self.q_row_scenario_buttons_row.addWidget(self.q_button_run_scenario)
        self.q_row_scenario_buttons_row.addWidget(self.q_button_stop_and_restore_scenario)
        self.q_row_scenario_buttons_row.addWidget(self.q_button_start_services_button)
        self.q_row_scenario_buttons_row.addWidget(self.q_button_close_workspace_button)
        self.q_row_scenario_buttons_row.addItem(spacerItem1)


        # Label for scenario status
        self.q_label_scenario_status_label = QtWidgets.QLabel(self.CentralLayout_captureManagerWindow)
        self.q_label_scenario_status_label.setObjectName("scenarioStatusLabel_captureManagerWindow")
        self.q_label_scenario_status_label.setText("Scenario Status:")

        # Label to hold the value of the scenario status
        self.q_label_scenario_status_value = QtWidgets.QLabel(self.CentralLayout_captureManagerWindow)
        self.q_label_scenario_status_value.setObjectName("scenarioStatus_captureManagerWindow")
        self.q_label_scenario_status_value.setText("This is the text area for holding the value of the scenario status")

        # Spacer item
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        # Add node button
        self.q_button_add_node = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.q_button_add_node.setObjectName("addNodeButton_captureManagerWindow")
        self.q_button_add_node.setText("Add Node")

        # Add set of victim nodes button
        self.q_button_add_set_of_victim_nodes = QtWidgets.QPushButton(self.CentralLayout_captureManagerWindow)
        self.q_button_add_set_of_victim_nodes.setObjectName("addSetNodeButton_captureManagerWindow")
        self.q_button_add_set_of_victim_nodes.setText("Add Set of Victim Nodes")
        

        # Set up a row to hold the label for scenario status and the add node/ set nodes buttons
        self.q_row_buttons_node_buttons = QtWidgets.QHBoxLayout()
        self.q_row_buttons_node_buttons.setObjectName("nodeLayout_captureManagerWindow")
        self.q_row_buttons_node_buttons.addWidget(self.q_label_scenario_status_label)
        self.q_row_buttons_node_buttons.addWidget(self.q_label_scenario_status_value)
        self.q_row_buttons_node_buttons.addItem(spacerItem2)
        self.q_row_buttons_node_buttons.addWidget(self.q_button_add_node)          
        self.q_row_buttons_node_buttons.addWidget(self.q_button_add_set_of_victim_nodes)


        # Q tree widget for holding nodes
        self.q_tree_widget_nodes_list = QtWidgets.QTreeWidget(self.CentralLayout_captureManagerWindow)
        self.q_tree_widget_nodes_list.setObjectName("nodesList_captureManagerWindow")
        self.q_tree_widget_nodes_list.headerItem().setText(0, "Log Net Traffic")
        self.q_tree_widget_nodes_list.headerItem().setText(1, "Type")
        self.q_tree_widget_nodes_list.headerItem().setText(2, "Name")
        self.q_tree_widget_nodes_list.headerItem().setText(3, "MAC")
        self.q_tree_widget_nodes_list.headerItem().setText(4, "IP")
        self.q_tree_widget_nodes_list.headerItem().setText(5, "Scanner/Victim")


        # Create a column and the scenario buttons row, the q tree widget and the row for the nodes buttons
        self.q_col_vm_buttons_nodes_list_and_nodes_buttons = QtWidgets.QVBoxLayout()
        self.q_col_vm_buttons_nodes_list_and_nodes_buttons.setObjectName("scenarioLayout_captureManagerWindow")
        self.q_col_vm_buttons_nodes_list_and_nodes_buttons.addLayout(self.q_row_scenario_buttons_row)
        self.q_col_vm_buttons_nodes_list_and_nodes_buttons.addWidget(self.q_tree_widget_nodes_list)
        self.q_col_vm_buttons_nodes_list_and_nodes_buttons.addLayout(self.q_row_buttons_node_buttons)


        # Set up a q tree widget for the projects lists
        self.q_tree_widget_projects_list = QtWidgets.QTreeWidget(self.CentralLayout_captureManagerWindow)
        self.q_tree_widget_projects_list.setMinimumSize(QtCore.QSize(220, 0))
        self.q_tree_widget_projects_list.setMaximumSize(QtCore.QSize(220, 16777215))
        self.q_tree_widget_projects_list.setObjectName("projectsList_captureManagerWindow")
        self.q_tree_widget_projects_list.headerItem().setText(0, "Projects")


        # Create a row and add the projects list widget to it, then add the column that holds the vm buttons, the nodes list and the nodes buttons
        self.q_row_main_projects_and_nodes_row = QtWidgets.QHBoxLayout()
        self.q_row_main_projects_and_nodes_row.setObjectName("centralSectionLayout_captureManagerWindow")
        self.q_row_main_projects_and_nodes_row.addWidget(self.q_tree_widget_projects_list)
        self.q_row_main_projects_and_nodes_row.addLayout(self.q_col_vm_buttons_nodes_list_and_nodes_buttons)

        
        # Set up a q grid layout and add the project buttons row as well as the row for projects and nodes
        self.q_grid_layout = QtWidgets.QVBoxLayout(self.CentralLayout_captureManagerWindow)
        self.q_grid_layout.setObjectName("gridLayout_2")
        self.q_grid_layout.addLayout(self.q_row_buttons_project_options)
        self.q_grid_layout.addLayout(self.q_row_main_projects_and_nodes_row)


        # Add the central layout to the parent window
        parent_window.setCentralWidget(self.CentralLayout_captureManagerWindow)

        # Now we set up event listeners

        # Add event listeners to project buttons
        self.q_button_save_project.clicked.connect(self.save_everything_button_clicked)
        self.q_button_new_project.clicked.connect(self.create_project_button_clicked)
        self.q_button_export_project.clicked.connect(self.export_project_button_clicked)
        self.q_button_import_project.clicked.connect(lambda: self.import_project_button_clicked(parent_window))


        # Virtual Machine button functions
        self.q_button_start_vm.clicked.connect(self.start_vm_button_clicked)
        self.q_button_shutdown_vm.clicked.connect(self.shut_down_vm_button_clicked)

        # Scenario button functions
        self.q_button_run_scenario.clicked.connect(self.run_scenario_button_clicked)
        self.q_button_stop_and_restore_scenario.clicked.connect(self.stop_and_restore_scenario_button_clicked)

        # Start services button
        self.q_button_start_services_button.clicked.connect(self.start_services_button_clicked)

        # Close workspace button
        self.q_button_close_workspace_button.clicked.connect(
            lambda: 
                self.close_workspace_button_clicked(parent_window, choose_workspace_parent_window
            )
        )

        # Set up context menu for when user right clicks on a project
        self.q_tree_widget_projects_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.q_tree_widget_projects_list.customContextMenuRequested.connect(self.projects_tree_widget_right_clicked)

        # Set up event listener for when user clicks on a project on the projects list
        self.q_tree_widget_projects_list.itemSelectionChanged.connect(self.project_tree_widget_left_clicked)


        # Set up context menu for when user right clicks on a node
        self.q_tree_widget_nodes_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.q_tree_widget_nodes_list.customContextMenuRequested.connect(lambda point_clicked: self.node_right_clicked(point_clicked, parent_window))

        # Node button functions
        self.q_button_add_node.clicked.connect(self.add_node_button_clicked)
        self.q_button_add_set_of_victim_nodes.clicked.connect(self.add_set_node_button_clicked)


        # This doesnt work, idk why
        # What i thought this was for is to show the choose workspace window
        # when the user clicks on the close window button (not the close button defined above)
        # instead it just ends the program lmao
        # parent_window.closeEvent = choose_workspace_parent_window.show()

        # Lastly we populate the projects list
        self.render_projects_in_project_tree()


    def render_projects_in_project_tree(self):
        '''
        This function renders the projects in the project tree widget
        gets the projects attribute from the capture manager window
        and populates with tree widget items
        and their respective scenarios
        '''
        self.q_tree_widget_projects_list.clear()
        for project in self.workspace_object.projects:
            # Make TreeWidgetItem
            project_tree_item = QTreeWidgetItem([project.name])
            for scenario in project.scenarios:
                scenario_tree = QTreeWidgetItem([scenario.name])
                project_tree_item.addChild(scenario_tree)

            self.q_tree_widget_projects_list.addTopLevelItem(project_tree_item)

        # Automatically expand
        self.q_tree_widget_projects_list.expandAll()


    def project_tree_widget_left_clicked(self):
        '''
        Triggered when the user left clicks on a project or a scenario unit
        populates the nodes list with the nodes of the selected project or scenario unit
        '''

        try:
            # Get the selected item
            selected_item = self.q_tree_widget_projects_list.selectedItems()[0]
        except IndexError:
            # If no item is selected, return
            return

        # If the item has a parent, it is a scenario
        if selected_item.parent() is not None:
            self.on_scenario_unit_left_clicked(selected_item)
        else:
            self.on_project_left_clicked(selected_item)
    
    def on_scenario_unit_left_clicked(self, selected_scenario_item:QTreeWidgetItem):
        print("scenario unit left clicked " + selected_scenario_item.text(0))
        
        pass

    def on_project_left_clicked(self, selected_project_item:QTreeWidgetItem):
        print("project item left clicked " + selected_project_item.text(0))
        # print(f'checking if item_project_selected went inside')
        # Clear the window
        self.q_tree_widget_nodes_list.clear()
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


        self.q_tree_widget_nodes_list.header().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)

    # Q tree widget projects list right clicked functions
    def projects_tree_widget_right_clicked(self, point):
        '''
        Triggered when user right clicks on a project
        shows the context menu
        '''
       
        index = self.q_tree_widget_projects_list.indexAt(point)

        if not index.isValid():
            return


        item = self.q_tree_widget_projects_list.itemAt(point)
        # If the item has a parent it is a scenario
        if item.parent() is not None:
            self.on_scenario_unit_right_click(point)
        else:
            self.on_project_right_click(point)

    def on_project_right_click(self, point):
        '''
        Triggered when user right clicks on a project
        show options for addings a scenario, renaming the project
        or deleting the project
        '''
        # TODO: finish load scenario unit
        item = self.q_tree_widget_projects_list.itemAt(point)
        name = item.text(0)

        menu = QtWidgets.QMenu()
        action_add_scenario = QAction("Add Scenario Unit")
        # action_load_scenario = QAction("Load Scenario Unit")
        action_edit_project = QAction("Rename Project")
        action_delete_project = QAction("Delete Project")

        menu.addAction(action_add_scenario)
        # menu.addAction(action_load_scenario)
        menu.addAction(action_edit_project)
        menu.addAction(action_delete_project)

        action_add_scenario.triggered.connect(lambda: self.add_scenario_for_project_clicked(name))
        # action_load_scenario.triggered.connect(self.load_scenario_unit)
        action_edit_project.triggered.connect(lambda: self.edit_project_name_clicked(name))
        action_delete_project.triggered.connect(lambda: self.delete_project_clicked(name))

        menu.exec_(self.q_tree_widget_projects_list.mapToGlobal(point))
        return
    
    def on_scenario_unit_right_click(self, point):
        '''
        Triggerd when user right clicks on a scenario unit
        show options for renaming a scenario, deleting a scenario
        '''
        item = self.q_tree_widget_projects_list.itemAt(point)
        parent_project_name = item.parent().text(0)
        scenario_unit_name = item.text(0)

        menu = QtWidgets.QMenu()
        action_rename_scenario = QAction("Rename Scenario Unit")
        action_delete_scenario = QAction("Delete Scenario Unit")

        menu.addAction(action_rename_scenario)
        menu.addAction(action_delete_scenario)

        action_rename_scenario.triggered.connect(lambda: self.edit_scenario_unit_name_clicked(parent_project_name, scenario_unit_name))
        action_delete_scenario.triggered.connect(lambda: self.delete_scenario_unit_clicked(parent_project_name, scenario_unit_name))

        menu.exec_(self.q_tree_widget_projects_list.mapToGlobal(point))
        return


    # Project button functions
    def save_everything_button_clicked(self):
        '''
        Updates the state of the corresponding workspace
        object in the mongoDB
        with the current state of the workspace_object value
        '''
        self.db_helper.update_workspace(self.workspace_object)
        # Show a pop up that the workspace has been saved
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Workspace Saved")
        msg.setWindowTitle("The current workspace has been saved")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def create_project_button_clicked(self):
        newProject_Window = QtWidgets.QDialog()
        newProjectWindowUI = Ui_newProject_window()
        newProjectWindowUI.setupNewProjectWindowUi(
            newProject_Window,
            self,
            self.create_project
        )
        newProject_Window.show()
    
    def create_project(self, project_to_add:Project):
        '''
        Takes in a Project object and adds it to the
        list of projects in the workspace.
        '''
        self.workspace_object.projects.append(project_to_add)
        self.render_projects_in_project_tree()

    def export_project_button_clicked(self):
        project_name = self.q_tree_widget_projects_list.selectedItems()[0].text(0)
        export_path = QFileDialog().getSaveFileName(caption='Export Project', directory='~/untitled.json')
        print(f'export path is: {export_path}')

    def import_project_button_clicked(self, captureManager_Window):
        dialog = QFileDialog()
        json_path = dialog.getOpenFileName(captureManager_Window, 'Select JSON File', filter='*.json')
        if not json_path[0]:
            return
        with open(json_path[0]) as json_file:
            project = json.load(json_file)


    def load_scenario_unit(self):
        pass

    def edit_project_name_clicked(self, selected_project_name):
        '''
        Triggered when user clicks on the edit project name button
        '''
        # new_name, ok = editBox.getText(self, "Rename Project", "New Project Name:", text=selected_project.name)
        valid_input: bool = False

        while(not valid_input):
            new_q_dialog = QtWidgets.QInputDialog()
            editBox = QtWidgets.QInputDialog()
            new_name, ok = editBox.getText(new_q_dialog, "Rename Project", "New Project Name:", text=selected_project_name)

            if ok:
                # Check if the new project name is not already taken
                for project in self.workspace_object.projects:
                    if project.name == new_name:
                        # Show error message
                        error_message = QtWidgets.QMessageBox()
                        error_message.setText("Project name already taken!")
                        error_message.exec_()
                        valid_input = False
                        new_q_dialog.close()
                        break
                    else:
                        valid_input = True

        for project in self.workspace_object.projects:
            if project.name == selected_project_name:
                project.name = new_name
                self.render_projects_in_project_tree()
                break
        self.render_projects_in_project_tree()


    def delete_project_clicked(self, selected_project_name):
        '''
        Triggered when user clicks on the delete project button
        '''
        # Show confimation dialog
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Are you sure you want to delete this project?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
        ret = msgBox.exec_()

        # If user picked yes, delete project
        if ret == QtWidgets.QMessageBox.Yes:
            for project in self.workspace_object.projects:
                if project.name == selected_project_name:
                    self.workspace_object.projects.remove(project)
                    self.render_projects_in_project_tree()
                    break

    def add_scenario_for_project_clicked(self, project_name):
        '''
        Triggered when user clicks on the add scenario unit button
        Shows dialog box to input name of scenario
        '''
        # Get the project from the workspace object
        selected_project:Project
        for project in self.workspace_object.projects:
            if project.name == project_name:
                # Start the UI dialog
                selected_project = project

        newScenarioUnit_Window = QtWidgets.QDialog()
        newScenarioUnitWindowUI = Ui_newScenarioUnit_window()
        newScenarioUnitWindowUI.setupNewScenarioUnit(newScenarioUnit_Window, selected_project, self.create_new_scenario_for_project)
        newScenarioUnit_Window.show()

    def create_new_scenario_for_project(self, project:Project, scenario_name):
        '''
        Called from the UI dialog when the user clicks the create scenario unit button
        Creates a new scenario unit and adds it to the project
        '''
        project.scenarios.append(Scenario(scenario_name))
        self.render_projects_in_project_tree()

    def edit_scenario_unit_name_clicked(self, parent_project_name:str, selected_scenario_unit_name:str):
        '''
        Triggered when user clicks on the rename scenario unit button
        '''
        # TODO: implement get project using a map in the
        # workspace class definition to have O(1) lookup

        valid_input: bool = False

        while(not valid_input):
            editBox = QtWidgets.QInputDialog()
            new_name, ok = editBox.getText(editBox, "Rename Scenario Unit", "New Scenario Unit Name:", text=selected_scenario_unit_name)

            if ok:
                # Check if the new scenario unit name is not already taken
                for project in self.workspace_object.projects:
                    if project.name == parent_project_name:
                        for scenario in project.scenarios:
                            if scenario.name == new_name:
                                # Show error message
                                error_message = QtWidgets.QMessageBox()
                                error_message.setText("Scenario unit name already taken under the selected project!")
                                error_message.exec_()
                                valid_input = False
                                editBox.close()
                                break
                        # IF this is reached, the scenario unit name is not taken
                        else:
                            valid_input = True

        for project in self.workspace_object.projects:
            if project.name == parent_project_name:
                for scenario in project.scenarios:
                    if scenario.name == selected_scenario_unit_name:
                        scenario.name = new_name
                        self.render_projects_in_project_tree()
                        break
                break

        

    def delete_scenario_unit_clicked (self, parent_project_name:str, selected_scenario_unit_name:str):
        '''
        Triggered when user clicks on the delete scenario unit button
        '''
        # Show confimation dialog
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Are you sure you want to delete this scenario unit?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
        ret = msgBox.exec_()

        # If user picked yes, delete scenario unit
        if ret == QtWidgets.QMessageBox.Yes:
            for project in self.workspace_object.projects:
                if project.name == parent_project_name:
                    for scenario in project.scenarios:
                        if scenario.name == selected_scenario_unit_name:
                            project.scenarios.remove(scenario)
                            self.render_projects_in_project_tree()
                            break
                    break


    def node_right_clicked(self, point, capture_manager_window:QtWidgets.QMainWindow):
        '''
        Triggered when user right clicks on a node
        shows the context menu that has edit node,
        and delete node options
        '''
        index = self.q_tree_widget_nodes_list.indexAt(point)

        if not index.isValid():
            return

        if not index.isValid() or index.parent().isValid():
            item = self.q_tree_widget_nodes_list.itemAt(point)
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

            menu.exec_(self.q_tree_widget_nodes_list.mapToGlobal(point))

            return

    

    # Capture controller functions
    def start_vm_button_clicked(self):
        self.capture_controller.start_vm()
        self.q_button_start_vm.setEnabled(False)
        self.q_button_shutdown_vm.setEnabled(True)

    def shut_down_vm_button_clicked(self):
        print("shutdown virtual machine")
        self.capture_controller.shutdown_vm()
        self.q_button_start_vm.setEnabled(True)
        self.q_button_shutdown_vm.setEnabled(False)

    def stop_and_restore_scenario_button_clicked(self):
        # self.vmSdsServiceInput_captureManagerWindow.setEnabled(True)
        # self.dockerSdsServiceInput_captureManagerWindow.setEnabled(True)
        # self.runScenarioButton_captureManagerWindow.setEnabled(True)
        pass

    def start_services_button_clicked(self):
        pass

    def run_scenario_button_clicked(self):
        # Check if scenario is selected
        try:
            selected_item = self.q_tree_widget_projects_list.selectedItems()[0]

            # If there is no parent object in the tree, then the selected item is a project
            if selected_item.parent() is None:
                raise Exception()
            
            # If there is a parent object in the tree, then the selected item is a scenario
            selected_scenario_project_name = selected_item.parent().text(0)
            selected_scenario_name = selected_item.text(0)

            # Get the scenario object
            for project in self.workspace_object.projects:
                if project.name == selected_scenario_project_name:
                    for scenario in project.scenarios:
                        if scenario.name == selected_scenario_name:
                            selected_scenario:Scenario = scenario
                            break
                    break

        except Exception:
            # Show window that there is no scenario selected
            error_message = QMessageBox()
            error_message.setText("Please select a scenario to add a node to!")
            error_message.setIcon(QMessageBox.Warning)
            error_message.exec_()
            return

        # Valid scenario selected
        print("run scenario with name " + selected_scenario.name)
        # TODO: implement scenario run
        # self.capture_controller.run_scenario(selected_scenario)


    def add_node_button_clicked(self):
        # Check if scenario is selected
        try:
            selected_item = self.q_tree_widget_projects_list.selectedItems()[0]

            # If there is no parent object in the tree, then the selected item is a project
            if selected_item.parent() is None:
                raise Exception()
            
            # If there is a parent object in the tree, then the selected item is a scenario
            selected_scenario_project_name = selected_item.parent().text(0)
            selected_scenario_name = selected_item.text(0)

            # Get the scenario object
            for project in self.workspace_object.projects:
                if project.name == selected_scenario_project_name:
                    for scenario in project.scenarios:
                        if scenario.name == selected_scenario_name:
                            selected_scenario:Scenario = scenario
                            break
                    break

        except Exception:
            # Show window that there is no scenario selected
            error_message = QtWidgets.QMessageBox()
            error_message.setText("Please select a scenario to add a node to!")
            error_message.setIcon(QtWidgets.QMessageBox.Warning)
            error_message.exec_()
            return


        addNode_Window = QtWidgets.QDialog()
        addNodeWindowUI = Ui_addNode_window()
        addNodeWindowUI.setupAddNode(addNode_Window, selected_scenario, self.add_node)
        addNode_Window.show()

    def add_set_node_button_clicked(self):
        # TODO: i dont think well have time but this checking
        # if a scenario is selected is repeated multiple times
        # make it into a function
        # Check if scenario is selected
        try:
            selected_item = self.q_tree_widget_projects_list.selectedItems()[0]

            # If there is no parent object in the tree, then the selected item is a project
            if selected_item.parent() is None:
                raise Exception()
            
            # If there is a parent object in the tree, then the selected item is a scenario
            selected_scenario_project_name = selected_item.parent().text(0)
            selected_scenario_name = selected_item.text(0)

            # Get the scenario object
            for project in self.workspace_object.projects:
                if project.name == selected_scenario_project_name:
                    for scenario in project.scenarios:
                        if scenario.name == selected_scenario_name:
                            selected_scenario:Scenario = scenario
                            break
                    break

        except Exception:
            # Show window that there is no scenario selected
            error_message = QtWidgets.QMessageBox()
            error_message.setText("Please select a scenario to add a node to!")
            error_message.setIcon(QtWidgets.QMessageBox.Warning)
            error_message.exec_()
            return

        
        addSetNodes_Window = QtWidgets.QDialog()
        addSetNodesWindowUI = Ui_addSetNodes_window()
        addSetNodesWindowUI.setupAddSetNodes(addSetNodes_Window, selected_scenario, self.add_set_nodes)
        addSetNodes_Window.show()

    def add_set_nodes(self, selected_scenario:Scenario, node_to_clone:Node, times_node_is_cloned:int):
        print("add set nodes not yet implemented")

    def close_workspace_button_clicked(self, capture_manager_window:QMainWindow, choose_workspace_window:QDialog):
        capture_manager_window.close()
        choose_workspace_window.show()

    def add_node(self, node:Node, selected_scenario):
        if node.type == 'PC':
            selected_scenario.devices.append(node)
        if node.type == 'RJ45':
            selected_scenario.networks.append(node)
        
        self.render_nodes_in_node_tree(selected_scenario)

    def render_nodes_in_node_tree(self, selected_scenario):
        for node in selected_scenario.networks:
            node_item = QTreeWidgetItem([str(node.listening),
                                         node.type, node.name, node.mac, node.ip, 'No'])
            self.q_tree_widget_nodes_list.addTopLevelItem(node_item)

        for node in selected_scenario.devices:
            node_item = QTreeWidgetItem([str(node.listening),
                                         node.type, node.name, node.mac, node.ip, 'No'])
            self.q_tree_widget_nodes_list.addTopLevelItem(node_item)

