import json
import time
from venv import create

import Database.DatabaseHelper
from Controllers.CaptureController import CaptureControllerService
from Models.modelClasses import Workspace
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QAbstractButton, QAction, QDialog, QMessageBox,
                             QTreeWidgetItem)

from views.analysisManagerWindow import Ui_AnalysisManagerWindow
from views.captureManagerWindow import Ui_CaptureManagerWindow
from views.createWorkspaceWindow import Ui_newWorkspace_window


class Ui_choose_workspace_window(object):
    db_helper: Database.DatabaseHelper.SDSDatabaseHelper
    capture_controller_service: CaptureControllerService

    def __init__(self, db_helper: Database.DatabaseHelper.SDSDatabaseHelper, capture_controller_service: CaptureControllerService):
        '''
        Initializes the choose workspace window
        '''
        self.db_helper = db_helper
        self.capture_controller_service = CaptureControllerService()

    def setupWorkspaceUI(self, parent_window: QtWidgets.QDialog):
        # Setup parent window fields
        parent_window.setWindowIcon(QtGui.QIcon('network.png'))
        parent_window.setObjectName("workspace_window")
        parent_window.resize(780, 463)
        parent_window.setMinimumSize(QtCore.QSize(780, 463))
        parent_window.setMaximumSize(QtCore.QSize(780, 463))
        parent_window.setWindowTitle("Scan Detection System")

        # Create a column that will hold the workspaces list as a QTreeWidget
        self.q_col_layout_workspaces_col = QtWidgets.QVBoxLayout()
        self.q_col_layout_workspaces_col.setObjectName(
            "workspacesLayout_workspaceWindow")

        # Create the q tree widget that will hold the workspaces
        self.q_tree_widget_workspaces_list = QtWidgets.QTreeWidget(
            parent_window)
        self.q_tree_widget_workspaces_list.setObjectName(
            "workspacesList_workspaceWindow")
        self.q_tree_widget_workspaces_list.headerItem().setText(0, "Workspaces")

        __sortingEnabled = self.q_tree_widget_workspaces_list.isSortingEnabled()
        self.q_tree_widget_workspaces_list.setSortingEnabled(False)
        self.q_tree_widget_workspaces_list.setSortingEnabled(__sortingEnabled)
        self.q_tree_widget_workspaces_list.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        # This will setup the context menu for the workspaces list, this occurs when right clicking on a list object
        self.q_tree_widget_workspaces_list.customContextMenuRequested.connect(
            self.context_menu_workspace_right_clicked)

        # Add the tree widget to the column
        self.q_col_layout_workspaces_col.addWidget(
            self.q_tree_widget_workspaces_list)

        # create a row to hold the sds logo
        self.q_row_layout_logo = QtWidgets.QHBoxLayout()
        self.q_row_layout_logo.setObjectName("logoLayout_workspaceWindow")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.q_row_layout_logo.addItem(spacerItem)

        # Set up a label to hold the sds logo
        self.logoLabel_workspaceWindow = QtWidgets.QLabel(parent_window)
        self.logoLabel_workspaceWindow.setObjectName(
            "logoLabel_workspaceWindow")
        self.logoLabel_workspaceWindow.setPixmap(QPixmap('img/network.png'))

        # Add the label to the row
        self.q_row_layout_logo.addWidget(self.logoLabel_workspaceWindow)

        # Add spacer to the row
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.q_row_layout_logo.addItem(spacerItem1)

        # Set up label that says "Scan Detection System"
        self.q_label_sds_text_label = QtWidgets.QLabel(parent_window)
        self.q_label_sds_text_label.setObjectName("SDSLabel_workspaceWindow")
        self.q_label_sds_text_label.setText("Scan Detection System")

        # Set up spacer items
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        # Set up row and add spacer, then label, then spacer
        self.q_row_sds_label = QtWidgets.QHBoxLayout()
        self.q_row_sds_label.setObjectName("SDSLayout_workspaceWindow")
        self.q_row_sds_label.addItem(spacerItem2)
        self.q_row_sds_label.addWidget(self.q_label_sds_text_label)
        self.q_row_sds_label.addItem(spacerItem3)

        # Set up a label and spacers to hold the version text label

        self.q_label_version_label_text = QtWidgets.QLabel(parent_window)
        self.q_label_version_label_text.setObjectName(
            "versionLabel_workspaceWindow")
        self.q_label_version_label_text.setText("Version 2022.1.0")

        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        # Create row and add spacer, then label, then spacer
        self.q_row_version_text_label = QtWidgets.QHBoxLayout()
        self.q_row_version_text_label.setObjectName(
            "versionLayout_workspaceWindow")
        self.q_row_version_text_label.addItem(spacerItem4)
        self.q_row_version_text_label.addWidget(
            self.q_label_version_label_text)
        self.q_row_version_text_label.addItem(spacerItem5)

        # Create a column to hold the right part of the window
        self.q_col_right_side = QtWidgets.QVBoxLayout()
        self.q_col_right_side.setObjectName(
            "createWorkspaceLayout_workspaceWindow")

        # Add the rows to the column
        self.q_col_right_side.addLayout(self.q_row_version_text_label)
        self.q_col_right_side.addLayout(self.q_row_layout_logo)
        self.q_col_right_side.addLayout(self.q_row_sds_label)

        # Create a button to create a new workspace
        self.q_button_create_new_workspace = QtWidgets.QPushButton(
            parent_window)
        self.q_button_create_new_workspace.setObjectName(
            "createWorkspaceButton_workspaceWindow")
        self.q_button_create_new_workspace.setText("Create New Workspace")

        # Create a button to open the analysis manager
        self.q_button_open_analysis_manager = QtWidgets.QPushButton(
            parent_window)
        self.q_button_open_analysis_manager.setObjectName(
            "analysisManagerButton_workspaceWindow")
        self.q_button_open_analysis_manager.setText("Open Analysis Manager")

        # Add the buttons to the right side column
        self.q_col_right_side.addWidget(self.q_button_create_new_workspace)
        self.q_col_right_side.addWidget(self.q_button_open_analysis_manager)

        # Set up a row and add the 2 main columns to it
        self.q_row_main_row = QtWidgets.QHBoxLayout()
        self.q_row_main_row.setObjectName("mainLayout_workspaceWindow")
        self.q_row_main_row.addLayout(self.q_col_layout_workspaces_col)
        self.q_row_main_row.addLayout(self.q_col_right_side)

        # Set up a grid layout and add the main row
        self.gridLayout = QtWidgets.QGridLayout(parent_window)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.addLayout(self.q_row_main_row, 0, 0, 1, 1)

        # Add event listeners to the buttons
        self.q_button_open_analysis_manager.clicked.connect(
            lambda: self.open_analysis_manager_button_clicked(parent_window))
        self.q_button_create_new_workspace.clicked.connect(
            lambda: self.create_workspace_button_clicked(parent_window))

        # Event listener for when workspace is double clicked
        self.q_tree_widget_workspaces_list.doubleClicked.connect(
            lambda: self.workspace_list_item_double_clicked(parent_window))

        # Automate workspace generation based on passed workspace object from constructor
        self.generate_workspaces_list_window()

    def generate_workspaces_list_window(self):
        '''
        Generates the list of workspaces in the workspace window
        and updates the self.q_tree_widget_workspaces_list with
        the list of workspaces taken from the self.workspace_list object
        '''
        self.q_tree_widget_workspaces_list.clear()
        workspace_names = self.db_helper.get_all_workspace_names()
        for ws_name in workspace_names:
            list_item = QtWidgets.QTreeWidgetItem([ws_name])
            self.q_tree_widget_workspaces_list.addTopLevelItem(list_item)

    def context_menu_workspace_right_clicked(self, point):
        '''
        Sets up context menu (right click) for the workspace window
        is generated when a workspace is right clicked (or double clicked)
        Show options for delete and rename
        '''

        index = self.q_tree_widget_workspaces_list.indexAt(point)
        if not index.isValid():
            print("Invalid index point")
            return

        # Get the item name
        item = self.q_tree_widget_workspaces_list.itemAt(point)
        selected_workspace_name: str = item.text(0)

        # Set up QAction
        action_delete_workspace = QAction("Delete Workspace")
        action_rename_workspace = QAction("Rename Workspace")

        # set up a menu to hold the q actions
        menu = QtWidgets.QMenu()
        menu.addAction(action_delete_workspace)
        menu.addAction(action_rename_workspace)

        # Add event listeners to the actions
        action_delete_workspace.triggered.connect(
            lambda: self.create_workspace_delete_confirmation_window(selected_workspace_name))

        action_rename_workspace.triggered.connect(
            lambda: self.create_workspace_rename_window(selected_workspace_name))

        menu.exec_(self.q_tree_widget_workspaces_list.mapToGlobal(point))

    def create_workspace_delete_confirmation_window(self, selected_workspace: str):
        '''
        Opens up a confirmation window to delete a workspace
        '''
        # Create a confirmation window
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText(
            "Are you sure you want to delete workspace: " + selected_workspace)
        msg.setWindowTitle("Delete Workspace")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.buttonClicked.connect(
            self.workspace_delete_confirmation_window_option_selected)
        msg.exec_()

    def workspace_delete_confirmation_window_option_selected(self, button: QAbstractButton):
        '''
        Deletes the selected workspace if 
        the user clicked yes, otherwise 
        does nothing
        '''
        button_text: str = button.text()

        # For some reason pyqt sets the button text to "&No" instead of "No", so check for "&No" instead
        if button_text == "&No":
            print("Cancelled deleting a workspace")
            return

        # Get the selected workspace
        selected_workspace: str = self.q_tree_widget_workspaces_list.currentItem().text(0)

        # Delete the workspace
        self.db_helper.delete_workspace(selected_workspace)

        # Update the list of workspaces
        self.generate_workspaces_list_window()

    def create_workspace_rename_window(self, selected_workspace_name: str):
        '''
        Triggered when the user clicks on the rename workspace button
        '''
        # Valid input to keep while loop showing
        valid_input: bool = False

        while(not valid_input):
            # Show a dialog box
            new_q_dialog = QtWidgets.QInputDialog()
            editBox = QtWidgets.QInputDialog()
            new_name, ok = editBox.getText(new_q_dialog, "Rename Workspace", "New Workspace Name:", text=selected_workspace_name)

            if ok:
                # Check if the new workspace name is not already taken
                # if you can find it in the db the it is already taken
                if self.db_helper.get_workspace_by_id(new_name) is not None:
                    # Show error message
                    error_message = QtWidgets.QMessageBox()
                    error_message.setText("Project name already taken!")
                    error_message.exec_()
                    valid_input = False
                    new_q_dialog.destroy()
                if len(new_name) < 1:
                    # Show error message
                    error_message = QtWidgets.QMessageBox()
                    error_message.setText("Project name cannot be empty!")
                    error_message.exec_()
                    valid_input = False
                    new_q_dialog.destroy()
                else:
                    # break from while loop
                    valid_input = True
            else:
                valid_input = True
                return
        
        # Rename workspace
        self.db_helper.rename_workspace(selected_workspace_name, new_name)
        self.generate_workspaces_list_window()
        

    def workspace_list_item_double_clicked(self, choose_workspace_parent_window: QDialog):
        '''
        Triggered when a workspace is double clicked, looks for the workspace in the db that matches the name
        and opens the capture manager window for that workspace
        '''
        selected_workspace_name = self.q_tree_widget_workspaces_list.selectedItems()[
            0].text(0)
        selected_workspace_object = self.db_helper.get_workspace_by_id(
            selected_workspace_name)

        capture_manager_parent_window = QtWidgets.QMainWindow()
        captureManagerWindowUI = Ui_CaptureManagerWindow(
            self.db_helper, selected_workspace_object,
            self.capture_controller_service
        )
        captureManagerWindowUI.setupCaptureManager(
            capture_manager_parent_window, choose_workspace_parent_window)
        # captureManagerWindowUI.projectsList_captureManagerWindow.expandAll()

        capture_manager_parent_window.show()
        choose_workspace_parent_window.close()

    def create_workspace_button_clicked(self, parent_window: QDialog):
        '''
        Triggered when the user clicks on the create workspace button
        Shows the create workspace window, sends a created parent window as parameter
        as well as a function to call when the user clicks on the create workspace button
        '''
        createWorkspace_Window = QtWidgets.QDialog()
        createWorkspaceUI = Ui_newWorkspace_window(self.db_helper)
        createWorkspaceUI.setupCreateWorkspace(
            createWorkspace_Window,
            self.on_create_workspace_button_clicked_from_dialog_function
        )
        createWorkspace_Window.show()

    def on_create_workspace_button_clicked_from_dialog_function(self, workspace_name:str):
        '''
        Triggered when the user clicks on the create workspace button from the create workspace window
        adds a blank workspace with the provided workspace name
        '''
        self.db_helper.create_new_workspace(workspace_name)
        self.generate_workspaces_list_window()

    def open_analysis_manager_button_clicked(self, workspace_Window):
        '''
        Triggered when the user clicks on the open analysis manager button
        Shows the analysis manager window
        '''
        self.analysisManager_Window = QtWidgets.QMainWindow()
        self.analysisManagerWindowUI = Ui_AnalysisManagerWindow()
        self.analysisManagerWindowUI.setupAnalysisManager(
            self.analysisManager_Window, workspace_Window)
        self.analysisManager_Window.show()
        workspace_Window.close()
