from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem


class Ui_addNode_window(object):
    def setupAddNode(self, parent_window,
                     projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                     CentralLayout_captureManagerWindow, ip_counter, MAC, id_counter):

        parent_window.setObjectName("addNode_window")
        parent_window.setEnabled(True)
        parent_window.resize(487, 240)
        parent_window.setMinimumSize(QtCore.QSize(487, 240))
        parent_window.setMaximumSize(QtCore.QSize(487, 240))
        parent_window.setWindowTitle('Add new node')


        # Set up a label for node type
        self.q_node_type_label = QtWidgets.QLabel(parent_window)
        self.q_node_type_label.setObjectName("nodeTypeLabel_addNodeWindow")
        self.q_node_type_label.setText("Node Type")


        # Combo box for node type
        self.q_combo_box_node_type = QtWidgets.QComboBox(parent_window)
        self.q_combo_box_node_type.setObjectName("nodeTypeComboBox_addNodeWindow")

        # Set up combo box for node type
        self.q_combo_box_node_type.addItem('CORE')
        self.q_combo_box_node_type.addItem('VM')
        self.q_combo_box_node_type.addItem('Docker ')
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)


        # Row that holds the combo box for node type
        self.q_row_node_type_label_and_combo_box = QtWidgets.QHBoxLayout()
        self.q_row_node_type_label_and_combo_box.setObjectName("nodeTypeLayout_addNodeWindow")
        self.q_row_node_type_label_and_combo_box.addWidget(self.q_node_type_label)
        self.q_row_node_type_label_and_combo_box.addWidget(self.q_combo_box_node_type)
        self.q_row_node_type_label_and_combo_box.addItem(self.spacerItem)


        # Label for node name
        self.q_label_node_name = QtWidgets.QLabel(parent_window)
        self.q_label_node_name.setObjectName("nodeNameLabel_addNodeWindow")
        self.q_label_node_name.setText("Node Name:")

        # line edit input for node name
        self.q_line_edit_node_name = QtWidgets.QLineEdit(parent_window)
        self.q_line_edit_node_name.setObjectName("nodeNameInput_addNodeWindow")

        # Row that holds the label and line edit for node name
        self.q_row_node_name_label_and_input = QtWidgets.QHBoxLayout()
        self.q_row_node_name_label_and_input.setObjectName("nodeNameLayout_addNodeWindow")
        self.q_row_node_name_label_and_input.addWidget(self.q_label_node_name)
        self.q_row_node_name_label_and_input.addWidget(self.q_line_edit_node_name)



        # Label for mac address
        self.q_label_mac_address_label = QtWidgets.QLabel(parent_window)
        self.q_label_mac_address_label.setObjectName("nodeMACAddressLabel_addNodeWindow")
        self.q_label_mac_address_label.setText("MAC Address")

        # lined edit mac address input
        self.q_line_edit_mac_address_input = QtWidgets.QLineEdit(parent_window)
        self.q_line_edit_mac_address_input.setObjectName("nodeMACAddressInput_addNodeWindow")

        # Row that holds the label and line edit for mac address
        self.q_row_mac_address_row = QtWidgets.QHBoxLayout()
        self.q_row_mac_address_row.setObjectName("nodeMACAddressLayout_addNodeWindow")
        self.q_row_mac_address_row.addWidget(self.q_label_mac_address_label)
        self.q_row_mac_address_row.addWidget(self.q_line_edit_mac_address_input)


        # label for ip address
        self.q_label_ip_address_label = QtWidgets.QLabel(parent_window)
        self.q_label_ip_address_label.setObjectName("nodeIPAddressLabel_addNodeWindow")
        self.q_label_ip_address_label.setText("IP Address")

        # line edit ip address input
        self.q_line_edit_ip_address_input = QtWidgets.QLineEdit(parent_window)
        self.q_line_edit_ip_address_input.setObjectName("nodeIPAddressInput_addNodeWindow")
        self.q_line_edit_ip_address_input.setText(f"1.1.{ip_counter}.2")


        # Row that holds the label and line edit for ip address
        self.q_row_node_ip_address = QtWidgets.QHBoxLayout()
        self.q_row_node_ip_address.setObjectName("nodeIPAddressLayout_addNodeWindow")
        self.q_row_node_ip_address.addWidget(self.q_label_ip_address_label)
        self.q_row_node_ip_address.addWidget(self.q_line_edit_ip_address_input)


        # spacer item
        self.spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)


        # Set up 3 checkboxes for web server log net traffic, scanner
        self.q_checkbox_node_web_server = QtWidgets.QCheckBox(parent_window)
        self.q_checkbox_node_web_server.setObjectName("nodeWebServerNodeCheckBox_addNodeWindow")
        self.q_checkbox_node_web_server.setText("Web Server")


        self.q_check_box_node_log_net_traffic = QtWidgets.QCheckBox(parent_window)
        self.q_check_box_node_log_net_traffic.setObjectName("nodeLogNetNodeCheckBox_addNodeWindow")
        self.q_check_box_node_log_net_traffic.setText("Log Net Traffic")

        self.q_check_box_scanner_node = QtWidgets.QCheckBox(parent_window)
        self.q_check_box_scanner_node.setObjectName("nodeScannerNodeCheckBox_addNodeWindow")
        self.q_check_box_scanner_node.setText("Scanner Node")


        # Row that holds the checkboxes for web server, log net traffic, and scanner
        self.q_row_node_scanner = QtWidgets.QHBoxLayout()
        self.q_row_node_scanner.setObjectName("nodeScannerNodeLayout_addNodeWindow")
        self.q_row_node_scanner.addItem(self.spacerItem1)
        self.q_row_node_scanner.addWidget(self.q_check_box_node_log_net_traffic)
        self.q_row_node_scanner.addWidget(self.q_checkbox_node_web_server)
        self.q_row_node_scanner.addWidget(self.q_check_box_scanner_node)


        # Add node button
        self.q_button_add_node_button = QtWidgets.QPushButton(parent_window)
        self.q_button_add_node_button.setObjectName("addNodeButton_addNodeWindow")
        self.q_button_add_node_button.setText("Add Node")

        # Cancel button
        self.q_button_cancel_button = QtWidgets.QPushButton(parent_window)
        self.q_button_cancel_button.setObjectName("addNodeCancelButton_addNodeWindow")
        self.q_button_cancel_button.setText("Cancel")



        # row that holds the button for adding the node and the cancel button
        self.q_row_add_node_button = QtWidgets.QHBoxLayout()
        self.q_row_add_node_button.setObjectName("addNodeButtonsLayout_addNodeWindow")
        self.q_row_add_node_button.addWidget(self.q_button_add_node_button)
        self.q_row_add_node_button.addWidget(self.q_button_cancel_button)



        # Column that holds the row for the above rows defined
        self.q_col_main = QtWidgets.QVBoxLayout()
        self.q_col_main.setObjectName("mainLayout_addNodeWindow")
        self.q_col_main.addLayout(self.q_row_node_type_label_and_combo_box)
        self.q_col_main.addLayout(self.q_row_node_name_label_and_input)
        self.q_col_main.addLayout(self.q_row_mac_address_row)
        self.q_col_main.addLayout(self.q_row_node_ip_address)
        self.q_col_main.addLayout(self.q_row_node_scanner)
        self.q_col_main.addLayout(self.q_row_add_node_button)

        # main layout
        self.q_grid_main_layout = QtWidgets.QGridLayout(parent_window)
        self.q_grid_main_layout.setObjectName("AddNodeWindowLayout")
        self.q_grid_main_layout.addLayout(self.q_col_main, 0, 0, 1, 1)


        # Set up the event listeners
        self.q_check_box_scanner_node.toggled.connect(lambda: self.scanner_node_checkbox_clicked(
            parent_window, _translate, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
            CentralLayout_captureManagerWindow, id_counter))


        self.q_button_add_node_button.clicked.connect(lambda: self.addNode(
            parent_window, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
            CentralLayout_captureManagerWindow, id_counter))

        self.q_button_cancel_button.clicked.connect(parent_window.close)


        MAC += 1
        node_mac = str(MAC)[1:]
        node_mac = f"{node_mac[0:2]}:{node_mac[2:4]}:{node_mac[4:6]}:{node_mac[6:8]}:{node_mac[8:10]}:{node_mac[10:12]}"
        self.q_line_edit_mac_address_input.setText(node_mac)

    def scanner_node_checkbox_clicked(self, parent_window, _translate, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                    CentralLayout_captureManagerWindow, id_counter):
        if self.q_check_box_scanner_node.isChecked():
            self.nmapFlag = False
            self.niktoFlag = False
            parent_window.resize(487, 490)
            parent_window.setMinimumSize(QtCore.QSize(487, 490))
            parent_window.setMaximumSize(QtCore.QSize(487, 490))

            self.q_button_add_node_button.deleteLater()
            self.q_button_cancel_button.deleteLater()
            self.q_col_main.removeItem(self.q_row_add_node_button)

            self.nodeUserPassLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeUserPassLayout_addNodeWindow.setObjectName("nodeUserPassLayout_addNodeWindow")
            self.nodeUserPassLabel_addNodeWindow = QtWidgets.QLabel(parent_window)
            self.nodeUserPassLabel_addNodeWindow.setObjectName("nodeUserPassLabel_addNodeWindow")
            self.nodeUserPassLayout_addNodeWindow.addWidget(self.nodeUserPassLabel_addNodeWindow)
            self.nodeUserPassInput_addNodeWindow = QtWidgets.QLineEdit(parent_window)
            self.nodeUserPassInput_addNodeWindow.setObjectName("nodeUserPassInput_addNodeWindow")
            self.nodeUserPassLayout_addNodeWindow.addWidget(self.nodeUserPassInput_addNodeWindow)
            self.q_col_main.addLayout(self.nodeUserPassLayout_addNodeWindow)
            self.nodeScannerBinaryLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeScannerBinaryLayout_addNodeWindow.setObjectName("nodeScannerBinaryLayout_addNodeWindow")
            self.nodeScannerBinaryLabel_addNodeWindow = QtWidgets.QLabel(parent_window)
            self.nodeScannerBinaryLabel_addNodeWindow.setObjectName("nodeScannerBinaryLabel_addNodeWindow")
            self.nodeScannerBinaryLayout_addNodeWindow.addWidget(self.nodeScannerBinaryLabel_addNodeWindow)
            self.nodeScannerBinaryInput_addNodeWindow = QtWidgets.QLineEdit(parent_window)
            self.nodeScannerBinaryInput_addNodeWindow.setObjectName("nodeScannerBinaryInput_addNodeWindow")
            self.nodeScannerBinaryLayout_addNodeWindow.addWidget(self.nodeScannerBinaryInput_addNodeWindow)
            self.q_col_main.addLayout(self.nodeScannerBinaryLayout_addNodeWindow)

            self.nodeScannersNNNodeLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeScannersNNNodeLayout_addNodeWindow.setObjectName("nodeScannersNNNodeLayout_addNodeWindow")
            self.spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
            self.nodeScannersNNNodeLayout_addNodeWindow.addItem(self.spacerItem1)
            self.nodeNMapNodeCheckBox_addNodeWindow = QtWidgets.QCheckBox(parent_window)
            self.nodeNMapNodeCheckBox_addNodeWindow.setObjectName("nodeNMapNodeCheckBox_addNodeWindow")
            self.nodeScannersNNNodeLayout_addNodeWindow.addWidget(self.nodeNMapNodeCheckBox_addNodeWindow)
            self.nodeNiktoNodeCheckBox_addNodeWindow = QtWidgets.QCheckBox(parent_window)
            self.nodeNiktoNodeCheckBox_addNodeWindow.setObjectName("nodeNiktoNodeCheckBox_addNodeWindow")
            self.nodeScannersNNNodeLayout_addNodeWindow.addWidget(self.nodeNiktoNodeCheckBox_addNodeWindow)
            self.q_col_main.addLayout(self.nodeScannersNNNodeLayout_addNodeWindow)

            self.nodeNMapNodeCheckBox_addNodeWindow.toggled.connect(self.nmapSignal)
            self.nodeNiktoNodeCheckBox_addNodeWindow.toggled.connect(self.niktoSignal)

            self.nodeNMapArgumentsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeNMapArgumentsLayout_addNodeWindow.setObjectName("nodeNMapArgumentsLayout_addNodeWindow")
            self.nodeNMapArgumentsLabel_addNodeWindow = QtWidgets.QLabel(parent_window)
            self.nodeNMapArgumentsLabel_addNodeWindow.setObjectName("nodeNMapArgumentsLabel_addNodeWindow")
            self.nodeNMapArgumentsLayout_addNodeWindow.addWidget(self.nodeNMapArgumentsLabel_addNodeWindow)
            self.nodeNMapArgumentsInput_addNodeWindow = QtWidgets.QLineEdit(parent_window)
            self.nodeNMapArgumentsInput_addNodeWindow.setObjectName("nodeNMapArgumentsInput_addNodeWindow")
            self.nodeNMapArgumentsLayout_addNodeWindow.addWidget(self.nodeNMapArgumentsInput_addNodeWindow)
            self.q_col_main.addLayout(self.nodeNMapArgumentsLayout_addNodeWindow)
            self.nodeNMapArgumentsInput_addNodeWindow.setDisabled(True)

            self.nodeNiktoArgumentsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeNiktoArgumentsLayout_addNodeWindow.setObjectName("nodeNiktoArgumentsLayout_addNodeWindow")
            self.nodeNiktoArgumentsLabel_addNodeWindow = QtWidgets.QLabel(parent_window)
            self.nodeNiktoArgumentsLabel_addNodeWindow.setObjectName("nodeNiktoArgumentsLabel_addNodeWindow")
            self.nodeNiktoArgumentsLayout_addNodeWindow.addWidget(self.nodeNiktoArgumentsLabel_addNodeWindow)
            self.nodeNiktoArgumentsInput_addNodeWindow = QtWidgets.QLineEdit(parent_window)
            self.nodeNiktoArgumentsInput_addNodeWindow.setObjectName("nodeNiktoArgumentsInput_addNodeWindow")
            self.nodeNiktoArgumentsLayout_addNodeWindow.addWidget(self.nodeNiktoArgumentsInput_addNodeWindow)
            self.q_col_main.addLayout(self.nodeNiktoArgumentsLayout_addNodeWindow)
            self.nodeNiktoArgumentsInput_addNodeWindow.setDisabled(True)

            self.nodeNumIterationsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeNumIterationsLayout_addNodeWindow.setObjectName("nodeNumIterationsLayout_addNodeWindow")
            self.nodeNumIterationsLabel_addNodeWindow = QtWidgets.QLabel(parent_window)
            self.nodeNumIterationsLabel_addNodeWindow.setObjectName("nodeNumIterationsLabel_addNodeWindow")
            self.nodeNumIterationsLayout_addNodeWindow.addWidget(self.nodeNumIterationsLabel_addNodeWindow)
            self.nodeNumIterationsSpinBox_addNodeWindow = QtWidgets.QSpinBox(parent_window)
            self.nodeNumIterationsSpinBox_addNodeWindow.setObjectName("nodeNumIterationsSpinBox_addNodeWindow")
            self.nodeNumIterationsSpinBox_addNodeWindow.setValue(1)
            self.nodeNumIterationsLayout_addNodeWindow.addWidget(self.nodeNumIterationsSpinBox_addNodeWindow)
            self.spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
            self.nodeNumIterationsLayout_addNodeWindow.addItem(self.spacerItem2)
            self.q_col_main.addLayout(self.nodeNumIterationsLayout_addNodeWindow)
            self.nodeMaxParallelRunsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeMaxParallelRunsLayout_addNodeWindow.setObjectName("nodeMaxParallelRunsLayout_addNodeWindow")
            self.nodeMaxParallelRunsLabel_addNodeWindow = QtWidgets.QLabel(parent_window)
            self.nodeMaxParallelRunsLabel_addNodeWindow.setObjectName("nodeMaxParallelRunsLabel_addNodeWindow")
            self.nodeMaxParallelRunsLayout_addNodeWindow.addWidget(self.nodeMaxParallelRunsLabel_addNodeWindow)
            self.nodeMaxParallelRunsSpinBox_addNodeWindow = QtWidgets.QSpinBox(parent_window)
            self.nodeMaxParallelRunsSpinBox_addNodeWindow.setObjectName("nodeMaxParallelRunsSpinBox_addNodeWindow")
            self.nodeMaxParallelRunsSpinBox_addNodeWindow.setValue(1)
            self.nodeMaxParallelRunsLayout_addNodeWindow.addWidget(self.nodeMaxParallelRunsSpinBox_addNodeWindow)
            self.spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
            self.nodeMaxParallelRunsLayout_addNodeWindow.addItem(self.spacerItem3)
            self.q_col_main.addLayout(self.nodeMaxParallelRunsLayout_addNodeWindow)

            self.nodeEndConditionLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeEndConditionLayout_addNodeWindow.setObjectName("nodeEndConditionLayout_addNodeWindow")
            self.nodeEndConditionLabel_addNodeWindow = QtWidgets.QLabel(parent_window)
            self.nodeEndConditionLabel_addNodeWindow.setObjectName("nodeEndConditionLabel_addNodeWindow")
            self.nodeEndConditionLayout_addNodeWindow.addWidget(self.nodeEndConditionLabel_addNodeWindow)

            self.nodeEndConditionCombobox_addNodeWindow = QtWidgets.QComboBox(parent_window)
            self.nodeEndConditionCombobox_addNodeWindow.setObjectName("nodeEndConditionCombobox_addNodeWindow")
            self.nodeEndConditionCombobox_addNodeWindow.addItem('on-scan-complete')
            self.nodeEndConditionCombobox_addNodeWindow.addItem('Time...')
            self.nodeEndConditionLayout_addNodeWindow.addWidget(self.nodeEndConditionCombobox_addNodeWindow)
            self.spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
            self.nodeEndConditionLayout_addNodeWindow.addItem(self.spacerItem4)

            self.nodeEndConditionCombobox_addNodeWindow.currentIndexChanged.connect(lambda: self.end_condition_changed(
                parent_window, _translate, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                CentralLayout_captureManagerWindow, id_counter))

            self.q_col_main.addLayout(self.nodeEndConditionLayout_addNodeWindow)

            self.nodeUserPassLabel_addNodeWindow.setText(_translate("addNode_window", "User/Pass:             "))
            self.nodeScannerBinaryLabel_addNodeWindow.setText(_translate("addNode_window", "Scanner-Binary:    "))

            self.nodeNMapNodeCheckBox_addNodeWindow.setText(_translate("addNode_window", "NMap"))
            self.nodeNiktoNodeCheckBox_addNodeWindow.setText(_translate("addNode_window", "Nikto"))

            self.nodeNMapArgumentsLabel_addNodeWindow.setText(_translate("addNode_window", "NMap Arguments: "))
            self.nodeNiktoArgumentsLabel_addNodeWindow.setText(_translate("addNode_window", "Nikto Arguments:  "))

            self.nodeNumIterationsLabel_addNodeWindow.setText(_translate("addNode_window", "Number-Iterations:"))
            self.nodeMaxParallelRunsLabel_addNodeWindow.setText(_translate("addNode_window", "Max-Parallel-Runs:"))
            self.nodeEndConditionLabel_addNodeWindow.setText(_translate("addNode_window", "End-Condition:       "))

            self.q_row_add_node_button = QtWidgets.QHBoxLayout()
            self.q_row_add_node_button.setObjectName("addNodeButtonsLayout_addNodeWindow")
            self.q_button_add_node_button = QtWidgets.QPushButton(parent_window)
            self.q_button_add_node_button.setObjectName("addNodeButton_addNodeWindow")
            self.q_row_add_node_button.addWidget(self.q_button_add_node_button)
            self.q_button_cancel_button = QtWidgets.QPushButton(parent_window)
            self.q_button_cancel_button.setObjectName("addNodeCancelButton_addNodeWindow")
            self.q_row_add_node_button.addWidget(self.q_button_cancel_button)
            self.q_col_main.addLayout(self.q_row_add_node_button)
            self.q_button_add_node_button.setText(_translate("addNode_window", "Add Node"))
            self.q_button_cancel_button.setText(_translate("addNode_window", "Cancel"))

            self.q_button_add_node_button.clicked.connect(lambda: self.addNode(
                parent_window, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                CentralLayout_captureManagerWindow, id_counter))
            self.q_button_cancel_button.clicked.connect(parent_window.close)

        else:
            parent_window.resize(487, 240)
            parent_window.setMinimumSize(QtCore.QSize(487, 240))
            parent_window.setMaximumSize(QtCore.QSize(487, 240))

            self.nodeUserPassLabel_addNodeWindow.deleteLater()
            self.nodeUserPassInput_addNodeWindow.deleteLater()
            self.nodeScannerBinaryLabel_addNodeWindow.deleteLater()
            self.nodeScannerBinaryInput_addNodeWindow.deleteLater()

            self.nodeNMapArgumentsLabel_addNodeWindow.deleteLater()
            self.nodeNMapArgumentsInput_addNodeWindow.deleteLater()

            self.nodeNiktoArgumentsLabel_addNodeWindow.deleteLater()
            self.nodeNiktoArgumentsInput_addNodeWindow.deleteLater()

            self.nodeNMapNodeCheckBox_addNodeWindow.deleteLater()
            self.nodeNiktoNodeCheckBox_addNodeWindow.deleteLater()

            self.nodeNumIterationsLabel_addNodeWindow.deleteLater()
            self.nodeNumIterationsSpinBox_addNodeWindow.deleteLater()
            self.nodeMaxParallelRunsLabel_addNodeWindow.deleteLater()
            self.nodeMaxParallelRunsSpinBox_addNodeWindow.deleteLater()
            self.nodeEndConditionLabel_addNodeWindow.deleteLater()
            if self.nodeEndConditionCombobox_addNodeWindow.currentText() == 'Time...':
                self.minutesSpinbox_addNodeWindow.deleteLater()
                self.minutesLabel_addNodeWindow.deleteLater()
                self.secondsSpinbox_addNodeWindow.deleteLater()
                self.secondsLabel_addNodeWindow.deleteLater()
                self.q_col_main.removeItem(self.nodeTimeLayout_addNodeWindow)
            self.nodeEndConditionCombobox_addNodeWindow.deleteLater()

            self.q_col_main.removeItem(self.nodeUserPassLayout_addNodeWindow)
            self.q_col_main.removeItem(self.nodeScannerBinaryLayout_addNodeWindow)

            self.q_col_main.removeItem(self.nodeNMapArgumentsLayout_addNodeWindow)
            self.q_col_main.removeItem(self.nodeNiktoArgumentsLayout_addNodeWindow)
            self.q_col_main.removeItem(self.nodeScannersNNNodeLayout_addNodeWindow)

            self.q_col_main.removeItem(self.nodeNumIterationsLayout_addNodeWindow)
            self.q_col_main.removeItem(self.nodeMaxParallelRunsLayout_addNodeWindow)
            self.q_col_main.removeItem(self.nodeEndConditionLayout_addNodeWindow)
            self.q_col_main.removeItem(self.q_row_add_node_button)

            self.q_button_add_node_button.deleteLater()
            self.q_button_cancel_button.deleteLater()
            self.q_col_main.removeItem(self.q_row_add_node_button)

            self.q_row_add_node_button = QtWidgets.QHBoxLayout()
            self.q_row_add_node_button.setObjectName("addNodeButtonsLayout_addNodeWindow")
            self.q_button_add_node_button = QtWidgets.QPushButton(parent_window)
            self.q_button_add_node_button.setObjectName("addNodeButton_addNodeWindow")
            self.q_row_add_node_button.addWidget(self.q_button_add_node_button)
            self.q_button_cancel_button = QtWidgets.QPushButton(parent_window)
            self.q_button_cancel_button.setObjectName("addNodeCancelButton_addNodeWindow")
            self.q_row_add_node_button.addWidget(self.q_button_cancel_button)
            self.q_col_main.addLayout(self.q_row_add_node_button)
            self.q_button_add_node_button.setText(_translate("addNode_window", "Add Node"))
            self.q_button_cancel_button.setText(_translate("addNode_window", "Cancel"))

            self.q_button_add_node_button.clicked.connect(lambda: self.addNode(
                parent_window, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                CentralLayout_captureManagerWindow, id_counter))
            self.q_button_cancel_button.clicked.connect(parent_window.close)

    def end_condition_changed(self, addNode_window, _translate, projectsList_captureManagerWindow,
                              nodesList_captureManagerWindow, CentralLayout_captureManagerWindow, id_counter):
        if self.nodeEndConditionCombobox_addNodeWindow.currentText() == 'Time...':
            addNode_window.resize(487, 490)
            addNode_window.setMinimumSize(QtCore.QSize(487, 490))
            addNode_window.setMaximumSize(QtCore.QSize(487, 490))

            self.q_button_add_node_button.deleteLater()
            self.q_button_cancel_button.deleteLater()
            self.q_col_main.removeItem(self.q_row_add_node_button)

            self.nodeTimeLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeTimeLayout_addNodeWindow.setObjectName("nodeTimeLayout_addNodeWindow")
            self.minutesLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.minutesLabel_addNodeWindow.setObjectName("minutesLabel_addNodeWindow")
            self.nodeTimeLayout_addNodeWindow.addWidget(self.minutesLabel_addNodeWindow)
            self.minutesSpinbox_addNodeWindow = QtWidgets.QSpinBox(addNode_window)
            self.minutesSpinbox_addNodeWindow.setObjectName("minutesSpinbox_addNodeWindow")
            self.minutesSpinbox_addNodeWindow.setMaximum(59)
            self.nodeTimeLayout_addNodeWindow.addWidget(self.minutesSpinbox_addNodeWindow)
            self.secondsLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.secondsLabel_addNodeWindow.setObjectName("secondsLabel_addNodeWindow")
            self.nodeTimeLayout_addNodeWindow.addWidget(self.secondsLabel_addNodeWindow)
            self.secondsSpinbox_addNodeWindow = QtWidgets.QSpinBox(addNode_window)
            self.secondsSpinbox_addNodeWindow.setObjectName("secondsSpinbox_addNodeWindow")
            self.secondsSpinbox_addNodeWindow.setMaximum(59)
            self.nodeTimeLayout_addNodeWindow.addWidget(self.secondsSpinbox_addNodeWindow)
            self.spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
            self.nodeTimeLayout_addNodeWindow.addItem(self.spacerItem5)
            self.q_col_main.addLayout(self.nodeTimeLayout_addNodeWindow)

            self.q_row_add_node_button = QtWidgets.QHBoxLayout()
            self.q_row_add_node_button.setObjectName("addNodeButtonsLayout_addNodeWindow")
            self.q_button_add_node_button = QtWidgets.QPushButton(addNode_window)
            self.q_button_add_node_button.setObjectName("addNodeButton_addNodeWindow")
            self.q_row_add_node_button.addWidget(self.q_button_add_node_button)
            self.q_button_cancel_button = QtWidgets.QPushButton(addNode_window)
            self.q_button_cancel_button.setObjectName("addNodeCancelButton_addNodeWindow")
            self.q_row_add_node_button.addWidget(self.q_button_cancel_button)
            self.q_col_main.addLayout(self.q_row_add_node_button)
            self.minutesLabel_addNodeWindow.setText(_translate("addNode_window", "Minutes:"))
            self.secondsLabel_addNodeWindow.setText(_translate("addNode_window", "Seconds:"))
            self.q_button_add_node_button.setText(_translate("addNode_window", "Add Node"))
            self.q_button_cancel_button.setText(_translate("addNode_window", "Cancel"))

            self.q_button_add_node_button.clicked.connect(lambda: self.addNode(
                addNode_window, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                CentralLayout_captureManagerWindow, id_counter))
            self.q_button_cancel_button.clicked.connect(addNode_window.close)

        else:
            addNode_window.resize(487, 460)
            addNode_window.setMinimumSize(QtCore.QSize(487, 460))
            addNode_window.setMaximumSize(QtCore.QSize(487, 460))

            self.minutesLabel_addNodeWindow.deleteLater()
            self.minutesSpinbox_addNodeWindow.deleteLater()
            self.secondsLabel_addNodeWindow.deleteLater()
            self.secondsSpinbox_addNodeWindow.deleteLater()

            self.q_col_main.removeItem(self.q_row_add_node_button)
            self.q_col_main.removeItem(self.nodeTimeLayout_addNodeWindow)

            self.q_button_add_node_button.deleteLater()
            self.q_button_cancel_button.deleteLater()
            self.q_col_main.removeItem(self.q_row_add_node_button)

            self.q_row_add_node_button = QtWidgets.QHBoxLayout()
            self.q_row_add_node_button.setObjectName("addNodeButtonsLayout_addNodeWindow")
            self.q_button_add_node_button = QtWidgets.QPushButton(addNode_window)
            self.q_button_add_node_button.setObjectName("addNodeButton_addNodeWindow")
            self.q_row_add_node_button.addWidget(self.q_button_add_node_button)
            self.q_button_cancel_button = QtWidgets.QPushButton(addNode_window)
            self.q_button_cancel_button.setObjectName("addNodeCancelButton_addNodeWindow")
            self.q_row_add_node_button.addWidget(self.q_button_cancel_button)
            self.q_col_main.addLayout(self.q_row_add_node_button)
            self.q_button_add_node_button.setText(_translate("addNode_window", "Add Node"))
            self.q_button_cancel_button.setText(_translate("addNode_window", "Cancel"))

            self.q_button_add_node_button.clicked.connect(lambda: self.addNode(
                addNode_window, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                CentralLayout_captureManagerWindow, id_counter))
            self.q_button_cancel_button.clicked.connect(addNode_window.close)

    def nmapSignal(self):
        if self.nmapFlag is True:
            self.nodeNMapArgumentsInput_addNodeWindow.setEnabled(False)
            self.nmapFlag = False
        else:
            self.nodeNMapArgumentsInput_addNodeWindow.setEnabled(True)
            self.nmapFlag = True

    def niktoSignal(self):
        if self.niktoFlag is True:
            self.nodeNiktoArgumentsInput_addNodeWindow.setEnabled(False)
            self.niktoFlag = False
        else:
            self.nodeNiktoArgumentsInput_addNodeWindow.setEnabled(True)
            self.niktoFlag = True

    def addNode(self, addNode_Window, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                CentralLayout_captureManagerWindow, id_counter):
        # TODO: Implement this
        subnet = '0'
        log = ''
        if self.q_check_box_node_log_net_traffic.isChecked():
            log = 'True'
        else:
            log = 'False'
        type = self.q_combo_box_node_type.currentText()
        if type == 'CORE' or type == 'VM':
            type = 'PC'
        elif type == 'VM' or type == 'Docker':
            type = 'PC'  # temp solution
        name = self.q_line_edit_node_name.text()
        MAC = self.q_line_edit_mac_address_input.text()
        IP = self.q_line_edit_ip_address_input.text()
        IP_parse = IP.split(".")
        ip_counter = int(IP_parse[2]) + 1
        # subnet = addNodeWindowUI.nodeSeparateSubNetNodeCheckBox_addNodeWindow.isChecked()
        user_pw = ''
        scanner_bin = ''
        arguments = ''
        num_iterations = 1
        max_parallel_runs = 1
        end_condition = ''
        scanning = self.q_check_box_scanner_node.isChecked()
        if scanning:
            user_pw = self.nodeUserPassInput_addNodeWindow.text()
            scanner_bin = self.nodeScannerBinaryInput_addNodeWindow.text()
            arguments = self.nodeNMapArgumentsInput_addNodeWindow.text() + "$$$" + \
                        self.nodeNiktoArgumentsInput_addNodeWindow.text()
            num_iterations = self.nodeNumIterationsSpinBox_addNodeWindow.value()
            max_parallel_runs = self.nodeMaxParallelRunsSpinBox_addNodeWindow.value()
            if self.nodeEndConditionCombobox_addNodeWindow.currentText() == 'on-scan-complete':
                end_condition = 'on-scan-complete'
            else:
                # TODO: Handle minutes and seconds.
                minutes = str(self.minutesSpinbox_addNodeWindow.value())
                seconds = str(self.secondsSpinbox_addNodeWindow.value())
                end_condition = f'time-{minutes}:{seconds}'
            toolButton = QtWidgets.QToolButton(CentralLayout_captureManagerWindow)
            toolButton.setText('Scanner')
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
