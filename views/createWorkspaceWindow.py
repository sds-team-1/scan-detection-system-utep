import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import Database

from Database.databaseFunctions import generate_workspaces_list_window
from views.captureManagerWindow import Ui_CaptureManagerWindow

from Database.databaseFunctions import generate_workspaces_list_window


class Ui_newWorkspace_window(object):
    db_helper: Database.DatabaseHelper.SDSDatabaseHelper

    def __init__(self, db_helper: Database.DatabaseHelper.SDSDatabaseHelper):
        self.db_helper = db_helper

    def setupCreateWorkspace(
        self,
        parent_window: QtWidgets.QDialog,
        on_create_workspace_button_clicked_function
    ):
        '''
        Sets up the create workspace window,
        takes in the parent window and the function to call when the create workspace button is clicked
        '''
        parent_window.setObjectName("newWorkspace_window")
        parent_window.setEnabled(True)
        parent_window.resize(487, 120)
        parent_window.setMinimumSize(QtCore.QSize(487, 120))
        parent_window.setMaximumSize(QtCore.QSize(487, 120))
        parent_window.setWindowTitle("New Workspace")

        # Create label and input line
        self.q_label_workspace_name = QtWidgets.QLabel(parent_window)
        self.q_label_workspace_name.setObjectName(
            "workspaceNameLabel_newWorkspaceWindow")
        self.q_label_workspace_name.setText("Workspace Name")

        self.q_line_edit_input_workspace_name_text = QtWidgets.QLineEdit(
            parent_window)
        self.q_line_edit_input_workspace_name_text.setObjectName(
            "workspaceNameInput_newWorkspaceWindow")
        self.q_line_edit_input_workspace_name_text.setFocus()

        # Create a row and add the label and input line to it
        self.q_row_layout_workspace_dialog_and_button = QtWidgets.QHBoxLayout()
        self.q_row_layout_workspace_dialog_and_button.setObjectName(
            "newWorkspaceNameLayout_newWorkspaceWindow")
        self.q_row_layout_workspace_dialog_and_button.addWidget(
            self.q_label_workspace_name)
        self.q_row_layout_workspace_dialog_and_button.addWidget(
            self.q_line_edit_input_workspace_name_text)

        # Create the create workspace button
        self.createWorkspaceButton_newWorkspaceWindow = QtWidgets.QPushButton(
            parent_window)
        self.createWorkspaceButton_newWorkspaceWindow.setObjectName(
            "createWorkspaceButton_newWorkspaceWindow")
        self.createWorkspaceButton_newWorkspaceWindow.setText(
            "Create Workspace")

        # Create the cancel button
        self.cancelWorkspaceButton_newWorkspaceWindow = QtWidgets.QPushButton(
            parent_window)
        self.cancelWorkspaceButton_newWorkspaceWindow.setObjectName(
            "cancelWorkspaceButton_newWorkspaceWindow")
        self.cancelWorkspaceButton_newWorkspaceWindow.setText("Cancel")

        # Create the row and add the buttons to the row
        self.q_row_layout_create_cancel_buttons = QtWidgets.QHBoxLayout()
        self.q_row_layout_create_cancel_buttons.setObjectName(
            "newWorkspaceButtonsLayout_newWorkspaceWindow")
        self.q_row_layout_create_cancel_buttons.addWidget(
            self.createWorkspaceButton_newWorkspaceWindow)
        self.q_row_layout_create_cancel_buttons.addWidget(
            self.cancelWorkspaceButton_newWorkspaceWindow)

        # Create a column and add the 2 rows
        self.q_col_layout_main = QtWidgets.QVBoxLayout()
        self.q_col_layout_main.setObjectName("newWorkspaceLayout")
        self.q_col_layout_main.addLayout(
            self.q_row_layout_workspace_dialog_and_button)
        self.q_col_layout_main.addLayout(
            self.q_row_layout_create_cancel_buttons)

        # Create a gridlayout and add the column to it
        self.NewProjectWindowLayout = QtWidgets.QGridLayout(parent_window)
        self.NewProjectWindowLayout.setObjectName("NewProjectWindowLayout")
        self.NewProjectWindowLayout.addLayout(
            self.q_col_layout_main, 0, 0, 1, 1)

        # Add event listeners to the buttons
        self.createWorkspaceButton_newWorkspaceWindow.clicked.connect(
            lambda: self.create_workspace_button_clicked(parent_window, on_create_workspace_button_clicked_function))
        self.cancelWorkspaceButton_newWorkspaceWindow.clicked.connect(
            parent_window.close)

    def create_workspace_button_clicked(self, parent_window: QtWidgets.QDialog, on_create_workspace_button_clicked_function):
        '''
        Runs when create workspace button is clicked,
        validates the input then calls on_create_workspace_button_clicked_function
        if the input is valid
        '''
        # Get workspace name
        workspace_name = self.q_line_edit_input_workspace_name_text.text()
        # If the workspace name is empty
        if not workspace_name:
            # Show error box and return
            error_box = QMessageBox()
            error_box.setText("Workspace name cannot be empty")
            error_box.exec()
            return

        if workspace_name in self.db_helper.get_all_workspace_names():
            msg = QMessageBox()
            msg.setWindowTitle("Workspace Already Exists")
            msg.setText('This workspace name is already taken!')
            msg.exec_()
            return

        # Create the workspace
        parent_window.close()
        on_create_workspace_button_clicked_function(workspace_name)
