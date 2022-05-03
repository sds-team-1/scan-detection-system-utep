import json
import os
import uuid

from PyQt5 import QtCore, QtWidgets
from Controllers.CaptureController import CaptureControllerService

import Database.DatabaseHelper
from views.chooseWorkspace import Ui_choose_workspace_window


class Ui_databaseConfig_window(object):
    parent_window : QtWidgets.QDialog
    DEFAULT_WINDOW_TITLE = "Database Configuration"
    DEFAULT_WINDOW_HEIGHT = 150
    DEFAULT_WINDOW_WIDTH = 513
    DEFAULT_URL_STRING = "mongodb://localhost:27017"

    def __init__(self):
        print("Initializing database config window")

    def setupDatabaseConfig(self, parent_window:QtWidgets.QDialog):
        #self.workspacesList_workspaceWindow = workspacesList_workspaceWindow
        #self.sds_controller = sds_controller
        # db_config_filename = 'conf/db_config.json'
        
        self.parent_window = parent_window

        # setup parent window properties
        parent_window.setObjectName("databaseConfig_window")
        parent_window.setEnabled(True)
        parent_window.resize(self.DEFAULT_WINDOW_WIDTH, self.DEFAULT_WINDOW_HEIGHT)
        parent_window.setMinimumSize(QtCore.QSize(self.DEFAULT_WINDOW_WIDTH, self.DEFAULT_WINDOW_HEIGHT))
        parent_window.setMaximumSize(QtCore.QSize(self.DEFAULT_WINDOW_WIDTH, self.DEFAULT_WINDOW_HEIGHT))
        parent_window.setWindowTitle(self.DEFAULT_WINDOW_TITLE)

        # create a label that says "Mongo Database Url:"
        self.q_label_port = QtWidgets.QLabel(parent_window)
        self.q_label_port.setObjectName("databaseConfigPortLabel_databaseConfigWindow")
        self.q_label_port.setText("Mongo Database Url:")

        # create a line edit that will hold the port number
        self.q_line_edit_url_input = QtWidgets.QLineEdit(parent_window)
        self.q_line_edit_url_input.setObjectName("databaseConfigPortInput_databaseConfigWindow")
        self.q_line_edit_url_input.setText(self.DEFAULT_URL_STRING)
        
        # Add the label and line edit to a row layout
        self.q_row_box_layout_port_label_and_input = QtWidgets.QHBoxLayout()
        self.q_row_box_layout_port_label_and_input.setObjectName("databaseConfigPortLayout_databaseConfigWindow")
        self.q_row_box_layout_port_label_and_input.addWidget(self.q_label_port)
        self.q_row_box_layout_port_label_and_input.addWidget(self.q_line_edit_url_input)

        # Create a label for the error message, set it to empty string (will update when error occurs)
        self.q_label_error_message = QtWidgets.QLabel(parent_window)
        self.q_label_error_message.setObjectName("databaseConfigErrorMessage")
        self.q_label_error_message.setText("")

        # Add the label to a row layout
        self.q_row_box_layout_error = QtWidgets.QHBoxLayout()
        self.q_row_box_layout_error.setObjectName("databaseConfigErrorMessageLayout_databaseConfigWindow")
        self.q_row_box_layout_error.addWidget(self.q_label_error_message)


        # Create a button that will connect to the database
        self.q_push_button_connect = QtWidgets.QPushButton(parent_window)
        self.q_push_button_connect.setObjectName("databaseConfigIPConnectButton_databaseConfigWindow")
        self.q_push_button_connect.setText("Connect")
        
        # Create a cancel button
        self.q_push_button_cancel = QtWidgets.QPushButton(parent_window)
        self.q_push_button_cancel.setObjectName("databaseConfigIPCancelButton_databaseConfigWindow")
        self.q_push_button_cancel.setText("Cancel")

        # Create a row layout to hold the buttons
        self.q_row_box_buttons = QtWidgets.QHBoxLayout()
        self.q_row_box_buttons.setObjectName("databaseConfigIPButtonsLayout_databaseConfigWindow")
        self.q_row_box_buttons.addWidget(self.q_push_button_cancel)
        self.q_row_box_buttons.addWidget(self.q_push_button_connect)

        # Create a column layout to hold the row layouts
        self.q_col_box_layout = QtWidgets.QVBoxLayout()
        self.q_col_box_layout.setObjectName("mainLayout_databaseConfigWindow")
        self.q_col_box_layout.addLayout(self.q_row_box_layout_port_label_and_input)
        self.q_col_box_layout.addLayout(self.q_row_box_layout_error)
        self.q_col_box_layout.addLayout(self.q_row_box_buttons)

        # Initialize main layout a grid layout
        self.q_grid_layout_main = QtWidgets.QGridLayout(parent_window)
        self.q_grid_layout_main.setObjectName("DatabaseConfigWindowLayout")
        self.q_grid_layout_main.addLayout(self.q_col_box_layout, 0, 0, 1, 1)

        # Connect event listeners to buttons
        self.q_push_button_connect.clicked.connect(
            lambda: self.connect_button_clicked(parent_window)
        )

        self.q_push_button_cancel.clicked.connect(
            parent_window.close
        )

    def connect_button_clicked(self, database_config_window):
        '''
        This function is called when the connect button is clicked.
        Uses input from the database config window to connect to the database.
        '''
        try:
            temp_db_helper : Database.DatabaseHelper.SDSDatabaseHelper = Database.DatabaseHelper.SDSDatabaseHelper(
                self.q_line_edit_url_input.text()
            )
            temp_db_helper.test_connection()
        except Exception as e:
            self.q_label_error_message.setText(str(e))
            self.q_label_error_message.repaint()
            return

        # At this point the connection succeeded, create workspace window and the capture controller service
        capture_controller_service = CaptureControllerService()

        choose_workspace_window = QtWidgets.QDialog()
        workspaceWindowUI = Ui_choose_workspace_window(db_helper=temp_db_helper, capture_controller_service=capture_controller_service)
        workspaceWindowUI.setupWorkspaceUI(choose_workspace_window)
        choose_workspace_window.show()   
        database_config_window.close()
