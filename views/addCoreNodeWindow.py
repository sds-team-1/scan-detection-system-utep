from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem

from Models.modelClasses import Scenario, Workspace, Node
import random
from randmac import RandMac

class Ui_addCoreNodes_window(object):

    ip_counter = 0
    id_counter = 0
    ID = str(random.randint(1000, 1000000))
    MAC = str(RandMac("00:00:00:00:00:00"))

    def setupAddCoreNodes(self, parent_window:QtWidgets.QDialog, project_name:str, scenario_name:str, create_new_nodes_function):
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
        self.label_ip.setText("Starting IP:")

        # Line edit for IP
        self.line_edit_ip = QtWidgets.QLineEdit(parent_window)
        self.line_edit_ip.setGeometry(QtCore.QRect(110, 130, 100, 30))
        self.line_edit_ip.setText("")

        # Row to hold IP
        self.row_ip = QtWidgets.QHBoxLayout()
        self.row_ip.addWidget(self.label_ip)
        self.row_ip.addWidget(self.line_edit_ip)

        # Label for number of nodes to add
        self.label_number_of_nodes = QtWidgets.QLabel(parent_window)
        self.label_number_of_nodes.setGeometry(QtCore.QRect(10, 170, 100, 30))
        self.label_number_of_nodes.setText("Number of nodes:")

        # spin box for number of nodes to add
        self.spin_box_number_of_nodes = QtWidgets.QSpinBox(parent_window)
        self.spin_box_number_of_nodes.setGeometry(QtCore.QRect(110, 170, 100, 30))
        self.spin_box_number_of_nodes.setMinimum(1)
        self.spin_box_number_of_nodes.setMaximum(100)
        self.spin_box_number_of_nodes.setValue(1)

        # Row to hold number of nodes to add
        self.row_number_of_nodes = QtWidgets.QHBoxLayout()
        self.row_number_of_nodes.addWidget(self.label_number_of_nodes)
        self.row_number_of_nodes.addWidget(self.spin_box_number_of_nodes)

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
        self.main_layout.addLayout(self.row_id)
        self.main_layout.addLayout(self.row_name)
        self.main_layout.addLayout(self.row_mac)
        self.main_layout.addLayout(self.row_ip)
        self.main_layout.addLayout(self.row_number_of_nodes)
        self.main_layout.addLayout(self.row_buttons)

        # Set main layout as the layout of the window
        parent_window.setLayout(self.main_layout)
        
        # Connect signals
        self.button_cancel.clicked.connect(lambda: parent_window.destroy())
        self.button_add.clicked.connect(lambda: self.add_node_button_clicked(
            parent_window, 
            selected_project_name=project_name,
            selected_scenario_unit_name=scenario_name, 
            add_nodes_function=create_new_nodes_function))


    def add_node_button_clicked(self, parent_window, selected_project_name:str, selected_scenario_unit_name:str, add_nodes_function):
        nodes_list = []

        node_to_add = Node(
                self.line_edit_id.text() + "_",
                self.line_edit_name.text() + "_",
                "PC",
                mac=self.line_edit_mac.text(),
                ip=self.line_edit_ip.text(),
                core_listening=False
            )

        print("selected_project_name:", selected_project_name)
        print("selected_scenario_unit_name:", selected_scenario_unit_name)

        # Add the core node to the scenario
        add_nodes_function(selected_project_name, selected_scenario_unit_name, node_to_add, self.spin_box_number_of_nodes.value())

        parent_window.destroy()
