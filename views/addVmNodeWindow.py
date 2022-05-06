import random

import Database.DatabaseHelper
from Models.modelClasses import Node, Scenario, Workspace
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem
from randmac import RandMac


class Ui_addVmNode_window(object):

    ip_counter = 0
    id_counter = 0
    ID = str(random.randint(11, 998))
    MAC = str(RandMac("00:00:00:00:00:00"))

    def setupAddVMNode(self, parent_window:QtWidgets.QDialog, project_name:str, scenario_name:str, add_vm_node_function):
        # Setup parent window
        self.parent_window = parent_window
        self.parent_window.setWindowTitle("Adding Core Node to scenario -> " + scenario_name)
        parent_window.resize(400, 600)
        parent_window.setMinimumSize(QtCore.QSize(400, 600))
        parent_window.setMaximumSize(QtCore.QSize(400, 600))

        # Label for ID
        self.label_id = QtWidgets.QLabel(parent_window)
        self.label_id.setGeometry(QtCore.QRect(10, 10, 100, 30))
        self.label_id.setText("ID:")

        # Line edit for ID
        self.line_edit_id = QtWidgets.QLineEdit(parent_window)
        self.line_edit_id.setGeometry(QtCore.QRect(110, 10, 100, 30))
        self.line_edit_id.setText(self.ID)

        # Row to hold ID
        self.row_id = QtWidgets.QHBoxLayout()
        self.row_id.addWidget(self.label_id)
        self.row_id.addWidget(self.line_edit_id)

        # Label for Name
        self.label_name = QtWidgets.QLabel(parent_window)
        self.label_name.setGeometry(QtCore.QRect(10, 50, 100, 30))
        self.label_name.setText("Name:")

        # Line edit for Name
        self.line_edit_name = QtWidgets.QLineEdit(parent_window)
        self.line_edit_name.setGeometry(QtCore.QRect(110, 50, 100, 30))
        self.line_edit_name.setText("")

        # Row to hold Name
        self.row_name = QtWidgets.QHBoxLayout()
        self.row_name.addWidget(self.label_name)
        self.row_name.addWidget(self.line_edit_name)

        # Label for MAC
        self.label_mac = QtWidgets.QLabel(parent_window)
        self.label_mac.setGeometry(QtCore.QRect(10, 90, 100, 30))
        self.label_mac.setText("MAC:")

        # Line edit for MAC
        self.line_edit_mac = QtWidgets.QLineEdit(parent_window)
        self.line_edit_mac.setGeometry(QtCore.QRect(110, 90, 100, 30))
        self.line_edit_mac.setText(self.MAC)

        # Row to hold MAC
        self.row_mac = QtWidgets.QHBoxLayout()
        self.row_mac.addWidget(self.label_mac)
        self.row_mac.addWidget(self.line_edit_mac)

        # Label for IP
        self.label_ip = QtWidgets.QLabel(parent_window)
        self.label_ip.setGeometry(QtCore.QRect(10, 130, 100, 30))
        self.label_ip.setText("IP:")

        # Line edit for IP
        self.line_edit_ip = QtWidgets.QLineEdit(parent_window)
        self.line_edit_ip.setGeometry(QtCore.QRect(110, 130, 100, 30))
        self.line_edit_ip.setText("")

        # Row to hold IP
        self.row_ip = QtWidgets.QHBoxLayout()
        self.row_ip.addWidget(self.label_ip)
        self.row_ip.addWidget(self.line_edit_ip)

        # label for username
        self.label_username = QtWidgets.QLabel(parent_window)
        self.label_username.setGeometry(QtCore.QRect(10, 170, 100, 30))
        self.label_username.setText("Username:")

        # Line edit for username
        self.line_edit_username = QtWidgets.QLineEdit(parent_window)
        self.line_edit_username.setGeometry(QtCore.QRect(110, 170, 100, 30))
        self.line_edit_username.setText("")

        # Row to hold username
        self.row_username = QtWidgets.QHBoxLayout()
        self.row_username.addWidget(self.label_username)
        self.row_username.addWidget(self.line_edit_username)

        # Label for password
        self.label_password = QtWidgets.QLabel(parent_window)
        self.label_password.setGeometry(QtCore.QRect(10, 210, 100, 30))
        self.label_password.setText("Password:")

        # Line edit for password
        self.line_edit_password = QtWidgets.QLineEdit(parent_window)
        self.line_edit_password.setGeometry(QtCore.QRect(110, 210, 100, 30))
        self.line_edit_password.setText("")

        # Row to hold password
        self.row_password = QtWidgets.QHBoxLayout()
        self.row_password.addWidget(self.label_password)
        self.row_password.addWidget(self.line_edit_password)

        # Label for bin
        self.label_bin = QtWidgets.QLabel(parent_window)
        self.label_bin.setGeometry(QtCore.QRect(10, 250, 100, 30))
        self.label_bin.setText("Bin:")

        # Line edit for bin
        self.line_edit_bin = QtWidgets.QLineEdit(parent_window)
        self.line_edit_bin.setGeometry(QtCore.QRect(110, 250, 100, 30))
        self.line_edit_bin.setText("")

        # Row to hold bin
        self.row_bin = QtWidgets.QHBoxLayout()
        self.row_bin.addWidget(self.label_bin)
        self.row_bin.addWidget(self.line_edit_bin)

        # Label for args
        self.label_args = QtWidgets.QLabel(parent_window)
        self.label_args.setGeometry(QtCore.QRect(10, 290, 100, 30))
        self.label_args.setText("Args:")

        # Line edit for args
        self.line_edit_args = QtWidgets.QLineEdit(parent_window)
        self.line_edit_args.setGeometry(QtCore.QRect(110, 290, 100, 30))
        self.line_edit_args.setText("")

        # Row to hold args
        self.row_args = QtWidgets.QHBoxLayout()
        self.row_args.addWidget(self.label_args)
        self.row_args.addWidget(self.line_edit_args)

        
        # cancel button
        self.button_cancel = QtWidgets.QPushButton(parent_window)
        self.button_cancel.setGeometry(QtCore.QRect(10, 210, 100, 30))
        self.button_cancel.setText("Cancel")

        # add button
        self.button_add = QtWidgets.QPushButton(parent_window)
        self.button_add.setGeometry(QtCore.QRect(110, 210, 100, 30))
        self.button_add.setText("Add")

        # Row to hold cancel and add buttons
        self.row_buttons = QtWidgets.QHBoxLayout()
        self.row_buttons.addWidget(self.button_cancel)
        self.row_buttons.addWidget(self.button_add)

        # Add all rows to main layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.row_name)
        self.main_layout.addLayout(self.row_mac)
        self.main_layout.addLayout(self.row_ip)
        self.main_layout.addLayout(self.row_username)
        self.main_layout.addLayout(self.row_password)
        self.main_layout.addLayout(self.row_bin)
        self.main_layout.addLayout(self.row_args)
        self.main_layout.addLayout(self.row_buttons)

        # Set main layout as the layout of the window
        parent_window.setLayout(self.main_layout)
        
        # Connect signals
        self.button_cancel.clicked.connect(lambda: parent_window.destroy())
        self.button_add.clicked.connect(lambda: self.add_node_button_clicked(
            parent_window, 
            selected_project_name=project_name,
            selected_scenario_unit_name=scenario_name, 
            add_vm_node_function=add_vm_node_function))


    def add_node_button_clicked(self, parent_window, selected_project_name:str, selected_scenario_unit_name:str, add_vm_node_function):
        '''
        This function is called when the add node button is clicked.
        Sets up a node that takes in the user input
        then calls the add_vm_node_function and passes the
        selected project name, selected scenario unit name,
        the node object, and the number of nodes to add.
        Sets the type to "RJ45"
        '''
        nodes_list = []

        node_to_add = Node(
            self.line_edit_id.text(),
            self.line_edit_name.text(),
            "RJ45",
            self.line_edit_mac.text(),
            self.line_edit_ip.text(),
            "24",
            vm_node_name=self.line_edit_name.text(),
            vm_node_username=self.line_edit_username.text(),
            vm_node_password=self.line_edit_password.text(),
            vm_binary_path=self.line_edit_bin.text(),
            vm_args=self.line_edit_args.text()
        )

        print("selected_project_name:", selected_project_name)
        print("selected_scenario_unit_name:", selected_scenario_unit_name)

        # Add the core node to the scenario
        add_vm_node_function(selected_project_name, selected_scenario_unit_name, node_to_add)

        parent_window.destroy()
