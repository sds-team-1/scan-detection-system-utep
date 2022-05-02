from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem

from Models.modelClasses import Workspace

import Database.DatabaseHelper

from Controllers.CaptureController import CaptureControllerService

class Ui_addNode_window(object):

    workspace_object : Workspace
    db_helper : Database.DatabaseHelper.SDSDatabaseHelper
    capture_controller: CaptureControllerService

    def __init__(self, db_helper:Database.DatabaseHelper.SDSDatabaseHelper, workspace_object:Workspace, capture_controller:CaptureControllerService):
        self.db_helper = db_helper
        self.workspace_object = workspace_object
        self.capture_controller = capture_controller


    def setupAddNode(self, parent_window:QtWidgets.QDialog, capture_manager_window, add_node_function):
        MAC += 1
        node_mac = str(MAC)[1:]
        node_mac = f"{node_mac[0:2]}:{node_mac[2:4]}:{node_mac[4:6]}:{node_mac[6:8]}:{node_mac[8:10]}:{node_mac[10:12]}"

        # Set up parent window properties
        parent_window.setObjectName("addNode_window")
        parent_window.setEnabled(True)
        parent_window.resize(487, 240)
        parent_window.setMinimumSize(QtCore.QSize(487, 240))
        parent_window.setMaximumSize(QtCore.QSize(487, 240))
        parent_window.setWindowTitle("parent_window", "Add New Node")

        self.q_label_node_name_label = QtWidgets.QLabel(parent_window)
        self.q_label_node_name_label.setObjectName("nodeNameLabel_addNodeWindow")
        self.q_label_node_name_label.setText("Node Name:          ")

        self.q_line_edit_node_name_input = QtWidgets.QLineEdit(parent_window)
        self.q_line_edit_node_name_input.setObjectName("nodeNameInput_addNodeWindow")

        self.q_label_node_type_label = QtWidgets.QLabel(parent_window)
        self.q_label_node_type_label.setObjectName("nodeTypeLabel_addNodeWindow")
        self.q_label_node_type_label.setText("Type:                    ")

        self.q_combobox_node_type = QtWidgets.QComboBox(parent_window)
        self.q_combobox_node_type.setObjectName("nodeTypeComboBox_addNodeWindow")
        self.q_combobox_node_type.addItem('CORE')
        self.q_combobox_node_type.addItem('VM')
        self.q_combobox_node_type.addItem('Docker ')

        self.q_label_node_MAC_Address_label = QtWidgets.QLabel(parent_window)
        self.q_label_node_MAC_Address_label.setObjectName("nodeMACAddressLabel_addNodeWindow")
        self.q_label_node_MAC_Address_label.setText("MAC Address:       ")

        self.q_line_edit_node_MAC_address_input = QtWidgets.QLineEdit(parent_window)
        self.q_line_edit_node_MAC_address_input.setObjectName("nodeMACAddressInput_addNodeWindow")
        self.q_line_edit_node_MAC_address_input.setText(node_mac)

        self.q_label_node_IP_address_label = QtWidgets.QLabel(parent_window)
        self.q_label_node_IP_address_label.setObjectName("nodeIPAddressLabel_addNodeWindow")
        self.q_label_node_IP_address_label.setText("IP Address:            ")

        self.q_line_edit_node_IP_Adress_input = QtWidgets.QLineEdit(parent_window)
        self.q_line_edit_node_IP_Adress_input.setObjectName("nodeIPAddressInput_addNodeWindow")
        self.q_line_edit_node_IP_Adress_input.setText(f"1.1.{ip_counter}.2")

        self.q_checkbox_web_server_node = QtWidgets.QCheckBox(parent_window)
        self.q_checkbox_web_server_node.setObjectName("nodeWebServerNodeCheckBox_addNodeWindow")
        self.q_checkbox_web_server_node.setText("Web Server")
        self.q_checkbox_scanner_node.toggled.connect(lambda: self.scannerNode(
            parent_window, id_counter))

        self.q_checkbox_log_network_node = QtWidgets.QCheckBox(parent_window)
        self.q_checkbox_log_network_node.setObjectName("nodeLogNetNodeCheckBox_addNodeWindow")
        self.q_checkbox_log_network_node.setText("Log Network Traffic")

        self.q_checkbox_scanner_node = QtWidgets.QCheckBox(parent_window)
        self.q_checkbox_scanner_node.setObjectName("nodeScannerNodeCheckBox_addNodeWindow")
        self.q_checkbox_scanner_node.setText("Scanner Node")
        self.q_checkbox_scanner_node.toggled.connect(lambda: self.scannerNode(
            parent_window, id_counter))

        self.q_button_add_node = QtWidgets.QPushButton(parent_window)
        self.q_button_add_node.setObjectName("addNodeButton_addNodeWindow")
        self.q_button_add_node.setText("Add Node")
        self.q_button_add_node.clicked.connect(lambda: self.addNode(
            parent_window, id_counter))

        self.q_button_cancel_button = QtWidgets.QPushButton(parent_window)
        self.q_button_cancel_button.setObjectName("addNodeCancelButton_addNodeWindow")
        self.q_button_cancel_button.setText("Cancel")
        self.q_button_cancel_button.clicked.connect(parent_window.close)

        self.q_node_type_layout = QtWidgets.QHBoxLayout()
        self.q_node_type_layout.setObjectName("nodeTypeLayout_addNodeWindow")
        self.q_node_type_layout.addWidget(self.q_label_node_type_label)
        self.q_node_type_layout.addWidget(self.q_combobox_node_type)
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.q_node_type_layout.addItem(self.spacerItem)

        self.q_layout_node_name = QtWidgets.QHBoxLayout()
        self.q_layout_node_name.setObjectName("nodeNameLayout_addNodeWindow")
        self.q_layout_node_name.addWidget(self.q_label_node_name_label)
        self.q_layout_node_name.addWidget(self.q_line_edit_node_name_input)

        self.q_layout_node_MAC_address = QtWidgets.QHBoxLayout()
        self.q_layout_node_MAC_address.setObjectName("nodeMACAddressLayout_addNodeWindow")
        self.q_layout_node_MAC_address.addWidget(self.q_label_node_MAC_Address_label)
        self.q_layout_node_MAC_address.addWidget(self.q_line_edit_node_MAC_address_input)

        self.q_layout_node_IP_address = QtWidgets.QHBoxLayout()
        self.q_layout_node_IP_address.setObjectName("nodeIPAddressLayout_addNodeWindow")     
        self.q_layout_node_IP_address.addWidget(self.q_label_node_IP_address_label)
        self.q_layout_node_IP_address.addWidget(self.q_line_edit_node_IP_Adress_input)

        self.q_layout_scanner_node = QtWidgets.QHBoxLayout()
        self.q_layout_scanner_node.setObjectName("nodeScannerNodeLayout_addNodeWindow")
        self.spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.q_layout_scanner_node.addItem(self.spacerItem1)
        self.q_layout_scanner_node.addWidget(self.q_checkbox_web_server_node)
        self.q_layout_scanner_node.addWidget(self.q_checkbox_log_network_node)
        self.q_layout_scanner_node.addWidget(self.q_checkbox_scanner_node)

        self.q_layout_addnode_buttons = QtWidgets.QHBoxLayout()
        self.q_layout_addnode_buttons.setObjectName("addNodeButtonsLayout_addNodeWindow")    
        self.q_layout_addnode_buttons.addWidget(self.q_button_add_node)
        self.q_layout_addnode_buttons.addWidget(self.q_button_cancel_button)

        self.q_main_layout = QtWidgets.QVBoxLayout()
        self.q_main_layout.setObjectName("mainLayout_addNodeWindow")
        self.q_main_layout.addLayout(self.q_node_type_layout)
        self.q_main_layout.addLayout(self.q_layout_node_name)    
        self.q_main_layout.addLayout(self.q_layout_node_MAC_address)
        self.q_main_layout.addLayout(self.q_layout_node_IP_address)
        self.q_main_layout.addLayout(self.q_layout_scanner_node)
        self.q_main_layout.addLayout(self.q_layout_addnode_buttons)

        self.q_grid_main_layout = QtWidgets.QGridLayout(parent_window)
        self.q_grid_main_layout.setObjectName("AddNodeWindowLayout")
        self.q_grid_main_layout.addLayout(self.q_main_layout, 0, 0, 1, 1)
        

    def scannerNode(self, parent_window, id_counter):

        if self.q_checkbox_scanner_node.isChecked():

            self.nmapFlag = False
            self.niktoFlag = False

            parent_window.resize(487, 490)
            parent_window.setMinimumSize(QtCore.QSize(487, 490))
            parent_window.setMaximumSize(QtCore.QSize(487, 490))

            self.q_button_add_node.deleteLater()
            self.q_button_cancel_button.deleteLater()
            self.q_main_layout.removeItem(self.q_layout_addnode_buttons)
            
            self.q_label_node_us_pw = QtWidgets.QLabel(parent_window)
            self.q_label_node_us_pw.setObjectName("q_label_node_us_pw")
            self.q_label_node_us_pw.setText("User/Pass:             ")

            self.q_line_edit_node_us_pw_input = QtWidgets.QLineEdit(parent_window)
            self.q_line_edit_node_us_pw_input.setObjectName("q_line_edit_node_us_pw_input")
            
            self.q_label_node_scanner_binary = QtWidgets.QLabel(parent_window)
            self.q_label_node_scanner_binary.setObjectName("q_label_node_scanner_binary")
            self.q_label_node_scanner_binary.setText("Scanner-Binary:    ")
        
            self.q_line_edit_node_scanner_binary_input = QtWidgets.QLineEdit(parent_window)
            self.q_line_edit_node_scanner_binary_input.setObjectName("q_line_edit_node_scanner_binary_input")
    
            self.q_checkbox_nmap_node = QtWidgets.QCheckBox(parent_window)
            self.q_checkbox_nmap_node.setObjectName("q_checkbox_nmap_node")
            self.q_checkbox_nmap_node.setText("NMap")
            self.q_checkbox_nmap_node.toggled.connect(self.nmapSignal)

            self.q_checkbox_nikto_node = QtWidgets.QCheckBox(parent_window)
            self.q_checkbox_nikto_node.setObjectName("q_checkbox_nikto_node")
            self.q_checkbox_nikto_node.setText("Nikto")
            self.q_checkbox_nikto_node.toggled.connect(self.niktoSignal)
            
            self.q_label_nmap_arguments = QtWidgets.QLabel(parent_window)
            self.q_label_nmap_arguments.setObjectName("q_label_nmap_arguments")
            self.q_label_nmap_arguments.setText("NMap Arguments: ")
            self.q_line_edit_nmap_arguments_input = QtWidgets.QLineEdit(parent_window)
            self.q_line_edit_nmap_arguments_input.setObjectName("q_line_edit_nmap_arguments_input")
            self.q_line_edit_nmap_arguments_input.setDisabled(True)

            self.q_label_nikto_arguments = QtWidgets.QLabel(parent_window)
            self.q_label_nikto_arguments.setObjectName("q_label_nikto_arguments")
            self.q_label_nikto_arguments.setText("Nikto Arguments:  ")
            self.q_line_edit_nikto_arguments_input = QtWidgets.QLineEdit(parent_window)
            self.q_line_edit_nikto_arguments_input.setObjectName("q_line_edit_nikto_arguments_input")
            self.q_line_edit_nikto_arguments_input.setDisabled(True)
            
            self.q_label_iterations_number = QtWidgets.QLabel(parent_window)
            self.q_label_iterations_number.setObjectName("q_label_iterations_number")
            self.q_label_iterations_number.setText("Number-Iterations:")
            self.q_spinbox_iterations_number = QtWidgets.QSpinBox(parent_window)
            self.q_spinbox_iterations_number.setObjectName("q_spinbox_iterations_number")
            self.q_spinbox_iterations_number.setValue(1)
                   
            self.q_label_max_parallel_runs = QtWidgets.QLabel(parent_window)
            self.q_label_max_parallel_runs.setObjectName("q_label_max_parallel_runs")
            self.q_label_max_parallel_runs.setText("Max-Parallel-Runs:")
            self.q_spinbox_max_parallel_runs = QtWidgets.QSpinBox(parent_window)
            self.q_spinbox_max_parallel_runs.setObjectName("q_spinbox_max_parallel_runs")
            self.q_spinbox_max_parallel_runs.setValue(1)
        
            self.q_label_end_condition = QtWidgets.QLabel(parent_window)
            self.q_label_end_condition.setObjectName("q_label_end_condition")
            self.q_label_end_condition.setText("End-Condition:       ")

            self.q_combobox_end_condition = QtWidgets.QComboBox(parent_window)
            self.q_combobox_end_condition.setObjectName("q_combobox_end_condition")
            self.q_combobox_end_condition.addItem('on-scan-complete')
            self.q_combobox_end_condition.addItem('Time...')
            self.q_combobox_end_condition.currentIndexChanged.connect(lambda: self.end_condition_changed(
                parent_window, id_counter))
            
            self.q_button_add_node = QtWidgets.QPushButton(parent_window)
            self.q_button_add_node.setObjectName("q_button_add_node")
            self.q_button_add_node.setText("Add Node")
            self.q_button_add_node.clicked.connect(lambda: self.addNode(
                parent_window, id_counter))

            self.q_button_cancel_button = QtWidgets.QPushButton(parent_window)
            self.q_button_cancel_button.setObjectName("q_button_cancel_button")
            self.q_button_cancel_button.setText("Cancel")
            self.q_button_cancel_button.clicked.connect(parent_window.close)

            self.q_layout_node_us_pw = QtWidgets.QHBoxLayout()
            self.q_layout_node_us_pw.setObjectName("q_layout_node_us_pw")
            self.q_layout_node_us_pw.addWidget(self.q_label_node_us_pw)
            self.q_layout_node_us_pw.addWidget(self.q_line_edit_node_us_pw_input)

            self.q_layout_node_scanner_binary = QtWidgets.QHBoxLayout()
            self.q_layout_node_scanner_binary.setObjectName("q_layout_node_scanner_binary")
            self.q_layout_node_scanner_binary.addWidget(self.q_label_node_scanner_binary)
            self.q_layout_node_scanner_binary.addWidget(self.q_line_edit_node_scanner_binary_input)

            self.q_layout_node_scanner_nikto_nmap = QtWidgets.QHBoxLayout()
            self.q_layout_node_scanner_nikto_nmap.setObjectName("q_layout_node_scanner_nikto_nmap")
            self.spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.q_layout_node_scanner_nikto_nmap.addItem(self.spacerItem1)
            self.q_layout_node_scanner_nikto_nmap.addWidget(self.q_checkbox_nmap_node)
            self.q_layout_node_scanner_nikto_nmap.addWidget(self.q_checkbox_nikto_node)

            self.q_layout_nmap_arguments = QtWidgets.QHBoxLayout()
            self.q_layout_nmap_arguments.setObjectName("q_layout_nmap_arguments")
            self.q_layout_nmap_arguments.addWidget(self.q_label_nmap_arguments)
            self.q_layout_nmap_arguments.addWidget(self.q_line_edit_nmap_arguments_input)

            self.q_layout_nikto_arguments = QtWidgets.QHBoxLayout()
            self.q_layout_nikto_arguments.setObjectName("q_layout_nikto_arguments")
            self.q_layout_nikto_arguments.addWidget(self.q_label_nikto_arguments)
            self.q_layout_nikto_arguments.addWidget(self.q_line_edit_nikto_arguments_input)

            self.q_layout_iterations_number = QtWidgets.QHBoxLayout()
            self.q_layout_iterations_number.setObjectName("q_layout_iterations_number")
            self.q_layout_iterations_number.addWidget(self.q_label_iterations_number)
            self.q_layout_iterations_number.addWidget(self.q_spinbox_iterations_number)
            self.spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
            self.q_layout_iterations_number.addItem(self.spacerItem2)

            self.q_layout_max_parallel_runs = QtWidgets.QHBoxLayout()
            self.q_layout_max_parallel_runs.setObjectName("q_layout_max_parallel_runs")
            self.q_layout_max_parallel_runs.addWidget(self.q_label_max_parallel_runs)
            self.q_layout_max_parallel_runs.addWidget(self.q_spinbox_max_parallel_runs)
            self.spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
            self.q_layout_max_parallel_runs.addItem(self.spacerItem3)

            self.q_layout_end_condition = QtWidgets.QHBoxLayout()
            self.q_layout_end_condition.setObjectName("q_layout_end_condition")
            self.q_layout_end_condition.addWidget(self.q_label_end_condition)
            self.q_layout_end_condition.addWidget(self.q_combobox_end_condition)
            self.spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
            self.q_layout_end_condition.addItem(self.spacerItem4)

            self.q_layout_addnode_buttons = QtWidgets.QHBoxLayout()
            self.q_layout_addnode_buttons.setObjectName("q_layout_addnode_buttons")
            self.q_layout_addnode_buttons.addWidget(self.q_button_add_node)
            self.q_layout_addnode_buttons.addWidget(self.q_button_cancel_button)

            self.q_main_layout.addLayout(self.q_layout_node_us_pw)
            self.q_main_layout.addLayout(self.q_layout_node_scanner_binary)
            self.q_main_layout.addLayout(self.q_layout_node_scanner_nikto_nmap)
            self.q_main_layout.addLayout(self.q_layout_nmap_arguments)
            self.q_main_layout.addLayout(self.q_layout_nikto_arguments)
            self.q_main_layout.addLayout(self.q_layout_iterations_number)
            self.q_main_layout.addLayout(self.q_layout_max_parallel_runs)
            self.q_main_layout.addLayout(self.q_layout_end_condition)
            self.q_main_layout.addLayout(self.q_layout_addnode_buttons)  

        else:

            parent_window.resize(487, 240)
            parent_window.setMinimumSize(QtCore.QSize(487, 240))
            parent_window.setMaximumSize(QtCore.QSize(487, 240))

            self.q_label_node_us_pw.deleteLater()
            self.q_line_edit_node_us_pw_input.deleteLater()
            self.q_label_node_scanner_binary.deleteLater()
            self.q_line_edit_node_scanner_binary_input.deleteLater()

            self.q_label_nmap_arguments.deleteLater()
            self.q_line_edit_nmap_arguments_input.deleteLater()

            self.q_label_nikto_arguments.deleteLater()
            self.q_line_edit_nikto_arguments_input.deleteLater()

            self.q_checkbox_nmap_node.deleteLater()
            self.q_checkbox_nikto_node.deleteLater()

            self.q_label_iterations_number.deleteLater()
            self.q_spinbox_iterations_number.deleteLater()
            self.q_label_max_parallel_runs.deleteLater()
            self.q_spinbox_max_parallel_runs.deleteLater()
            self.q_label_end_condition.deleteLater()

            if self.q_combobox_end_condition.currentText() == 'Time...':

                self.q_spinbox_end_condition_minutes.deleteLater()
                self.q_label_end_condition_minutes.deleteLater()
                self.q_spinbox_end_condition_seconds.deleteLater()
                self.q_label_end_condition_seconds.deleteLater()
                self.q_main_layout.removeItem(self.q_layout_end_condition_time)

            self.q_combobox_end_condition.deleteLater()

            self.q_main_layout.removeItem(self.q_layout_node_us_pw)
            self.q_main_layout.removeItem(self.q_layout_node_scanner_binary)

            self.q_main_layout.removeItem(self.q_layout_nmap_arguments)
            self.q_main_layout.removeItem(self.q_layout_nikto_arguments)
            self.q_main_layout.removeItem(self.q_layout_node_scanner_nikto_nmap)

            self.q_main_layout.removeItem(self.q_layout_iterations_number)
            self.q_main_layout.removeItem(self.q_layout_max_parallel_runs)
            self.q_main_layout.removeItem(self.q_layout_end_condition)
            self.q_main_layout.removeItem(self.q_layout_addnode_buttons)

            self.q_button_add_node.deleteLater()
            self.q_button_cancel_button.deleteLater()
            self.q_main_layout.removeItem(self.q_layout_addnode_buttons)

            
            self.q_button_add_node = QtWidgets.QPushButton(parent_window)
            self.q_button_add_node.setObjectName("q_button_add_node")
            self.q_button_add_node.setText("Add Node")
            self.q_button_add_node.clicked.connect(lambda: self.addNode(
                parent_window, id_counter))

            self.q_button_cancel_button = QtWidgets.QPushButton(parent_window)
            self.q_button_cancel_button.setObjectName("q_button_cancel_button")
            self.q_button_cancel_button.setText("Cancel")
            self.q_button_cancel_button.clicked.connect(parent_window.close)

            self.q_layout_addnode_buttons = QtWidgets.QHBoxLayout()
            self.q_layout_addnode_buttons.setObjectName("q_layout_addnode_buttons")
            self.q_layout_addnode_buttons.addWidget(self.q_button_add_node)
            self.q_layout_addnode_buttons.addWidget(self.q_button_cancel_button)

            self.q_main_layout.addLayout(self.q_layout_addnode_buttons)

    def end_condition_changed(self, parent_window, _translate, projectsList_captureManagerWindow,
                              nodesList_captureManagerWindow, CentralLayout_captureManagerWindow, id_counter):

        if self.q_combobox_end_condition.currentText() == 'Time...':

            parent_window.resize(487, 490)
            parent_window.setMinimumSize(QtCore.QSize(487, 490))
            parent_window.setMaximumSize(QtCore.QSize(487, 490))

            self.q_button_add_node.deleteLater()
            self.q_button_cancel_button.deleteLater()
            self.q_main_layout.removeItem(self.q_layout_addnode_buttons)
            
            self.q_label_end_condition_minutes = QtWidgets.QLabel(parent_window)
            self.q_label_end_condition_minutes.setObjectName("q_label_end_condition_minutes")
            self.q_label_end_condition_minutes.setText("Minutes:")
            
            self.q_spinbox_end_condition_minutes = QtWidgets.QSpinBox(parent_window)
            self.q_spinbox_end_condition_minutes.setObjectName("q_spinbox_end_condition_minutes")
            self.q_spinbox_end_condition_minutes.setMaximum(59)
            
            self.q_label_end_condition_seconds = QtWidgets.QLabel(parent_window)
            self.q_label_end_condition_seconds.setObjectName("q_label_end_condition_seconds")
            self.q_label_end_condition_seconds.setText("Seconds:")
            
            self.q_spinbox_end_condition_seconds = QtWidgets.QSpinBox(parent_window)
            self.q_spinbox_end_condition_seconds.setObjectName("q_spinbox_end_condition_seconds")
            self.q_spinbox_end_condition_seconds.setMaximum(59)
        
            self.q_button_add_node = QtWidgets.QPushButton(parent_window)
            self.q_button_add_node.setObjectName("q_button_add_node")
            self.q_button_add_node.setText("Add Node")
            self.q_button_add_node.clicked.connect(lambda: self.addNode(
                parent_window, id_counter))
            
            self.q_button_cancel_button = QtWidgets.QPushButton(parent_window)
            self.q_button_cancel_button.setObjectName("q_button_cancel_button")
            self.q_button_cancel_button.setText("Cancel")
            self.q_button_cancel_button.clicked.connect(parent_window.close)

            self.q_layout_end_condition_time = QtWidgets.QHBoxLayout()
            self.q_layout_end_condition_time.setObjectName("q_layout_end_condition_time")
            self.q_layout_end_condition_time.addWidget(self.q_label_end_condition_minutes)
            self.q_layout_end_condition_time.addWidget(self.q_spinbox_end_condition_minutes)
            self.q_layout_end_condition_time.addWidget(self.q_label_end_condition_seconds)
            self.q_layout_end_condition_time.addWidget(self.q_spinbox_end_condition_seconds)
            self.spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.q_layout_end_condition_time.addItem(self.spacerItem5)

            self.q_layout_addnode_buttons = QtWidgets.QHBoxLayout()
            self.q_layout_addnode_buttons.setObjectName("q_layout_addnode_buttons")
            self.q_layout_addnode_buttons.addWidget(self.q_button_add_node)
            self.q_layout_addnode_buttons.addWidget(self.q_button_cancel_button)

            self.q_main_layout.addLayout(self.q_layout_end_condition_time)
            self.q_main_layout.addLayout(self.q_layout_addnode_buttons)
        
        else:

            parent_window.resize(487, 460)
            parent_window.setMinimumSize(QtCore.QSize(487, 460))
            parent_window.setMaximumSize(QtCore.QSize(487, 460))

            self.q_label_end_condition_minutes.deleteLater()
            self.q_spinbox_end_condition_minutes.deleteLater()
            self.q_label_end_condition_seconds.deleteLater()
            self.q_spinbox_end_condition_seconds.deleteLater()

            self.q_main_layout.removeItem(self.q_layout_addnode_buttons)
            self.q_main_layout.removeItem(self.q_layout_end_condition_time)

            self.q_button_add_node.deleteLater()
            self.q_button_cancel_button.deleteLater()
            self.q_main_layout.removeItem(self.q_layout_addnode_buttons)

            self.q_layout_addnode_buttons = QtWidgets.QHBoxLayout()
            self.q_layout_addnode_buttons.setObjectName("q_layout_addnode_buttons")
            self.q_button_add_node = QtWidgets.QPushButton(parent_window)
            self.q_button_add_node.setObjectName("q_button_add_node")
            self.q_layout_addnode_buttons.addWidget(self.q_button_add_node)
            self.q_button_cancel_button = QtWidgets.QPushButton(parent_window)
            self.q_button_cancel_button.setObjectName("q_button_cancel_button")
            self.q_layout_addnode_buttons.addWidget(self.q_button_cancel_button)
            self.q_main_layout.addLayout(self.q_layout_addnode_buttons)
            self.q_button_add_node.setText(_translate("parent_window", "Add Node"))
            self.q_button_cancel_button.setText(_translate("parent_window", "Cancel"))

            self.q_button_add_node.clicked.connect(lambda: self.addNode(
                parent_window, id_counter))
            self.q_button_cancel_button.clicked.connect(parent_window.close)

    def nmapSignal(self):
        if self.nmapFlag is True:
            self.q_line_edit_nmap_arguments_input.setEnabled(False)
            self.nmapFlag = False
        else:
            self.q_line_edit_nmap_arguments_input.setEnabled(True)
            self.nmapFlag = True

    def niktoSignal(self):
        if self.niktoFlag is True:
            self.q_line_edit_nikto_arguments_input.setEnabled(False)
            self.niktoFlag = False
        else:
            self.q_line_edit_nikto_arguments_input.setEnabled(True)
            self.niktoFlag = True

    def addNode(self, addNode_Window, id_counter):
        # TODO: Implement this
        subnet = '0'
        log = ''
        if self.q_checkbox_log_network_node.isChecked():
            log = 'True'
        else:
            log = 'False'
        type = self.q_combobox_node_type.currentText()
        if type == 'CORE' or type == 'VM':
            type = 'PC'
        elif type == 'VM' or type == 'Docker':
            type = 'PC'  # temp solution
        name = self.q_line_edit_node_name_input.text()
        MAC = self.q_line_edit_node_MAC_address_input.text()
        IP = self.q_line_edit_node_IP_Adress_input.text()
        IP_parse = IP.split(".")
        ip_counter = int(IP_parse[2]) + 1
        # subnet = addNodeWindowUI.nodeSeparateSubNetNodeCheckBox_addNodeWindow.isChecked()
        user_pw = ''
        scanner_bin = ''
        arguments = ''
        num_iterations = 1
        max_parallel_runs = 1
        end_condition = ''
        scanning = self.q_checkbox_scanner_node.isChecked()
        if scanning:
            user_pw = self.q_line_edit_node_us_pw_input.text()
            scanner_bin = self.q_line_edit_node_scanner_binary_input.text()
            arguments = self.q_line_edit_nmap_arguments_input.text() + "$$$" + \
                        self.q_line_edit_nikto_arguments_input.text()
            num_iterations = self.q_spinbox_iterations_number.value()
            max_parallel_runs = self.q_spinbox_max_parallel_runs.value()
            if self.q_combobox_end_condition.currentText() == 'on-scan-complete':
                end_condition = 'on-scan-complete'
            else:
                # TODO: Handle minutes and seconds.
                minutes = str(self.q_spinbox_end_condition_minutes.value())
                seconds = str(self.q_spinbox_end_condition_seconds.value())
                end_condition = f'time-{minutes}:{seconds}'
            #toolButton = QtWidgets.QToolButton(CentralLayout_captureManagerWindow)
            #toolButton.setText('Scanner')
            # node_item = QTreeWidgetItem([subnet, log, type, name, MAC, IP])
            # nodesList_captureManagerWindow.addTopLevelItem(node_item)
            # nodesList_captureManagerWindow.setItemWidget(node_item, 6, toolButton)
        scenario_name = projectsList_captureManagerWindow.selectedItems()[0].text(0)
        scenario_id = self.sds_controller.get_scenario_id(scenario_name)
        nodes_list = self.sds_controller.get_all_nodes(scenario_name)
        id_counter += 1
        self.sds_controller.insert_node(scenario_id, id_counter, log, type, name, IP, MAC,
                                        subnet, scanning, user_pw, scanner_bin, arguments, int(num_iterations),
                                        max_parallel_runs, end_condition)
        nodes_list = self.sds_controller.get_all_nodes(scenario_name)
        nodesList_captureManagerWindow.clear()
        for node in nodes_list:
            node_item = QTreeWidgetItem([str(node['listening']),
                                         node['type'], node['name'], node['mac'], node['ip'], str(node['scanning'])])
            nodesList_captureManagerWindow.addTopLevelItem(node_item)
        addNode_Window.close()
        nodesList_captureManagerWindow.header().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)
