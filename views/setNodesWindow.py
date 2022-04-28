from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem


class Ui_addSetNodes_window(object):
    def setupAddSetNodes(self, addSetNodes_window, sds_controller,
                         projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                         ip_counter, MAC, id_counter):
        self.sds_controller = sds_controller
        addSetNodes_window.setObjectName("addSetNodes_window")
        addSetNodes_window.setEnabled(True)
        addSetNodes_window.resize(513, 170)
        addSetNodes_window.setMinimumSize(QtCore.QSize(513, 170))
        addSetNodes_window.setMaximumSize(QtCore.QSize(513, 170))
        self.AddSetNodesWindowLayout = QtWidgets.QGridLayout(addSetNodes_window)
        self.AddSetNodesWindowLayout.setObjectName("AddSetNodesWindowLayout")
        self.mainLayout_addSetNodesWindow = QtWidgets.QVBoxLayout()
        self.mainLayout_addSetNodesWindow.setObjectName("mainLayout_addSetNodesWindow")
        
        self.startingNameLayout_addSetNodesWindow = QtWidgets.QHBoxLayout()
        self.startingNameLayout_addSetNodesWindow.setObjectName("startingNameLayout_addSetNodesWindow")
        self.startingNameLabel_addSetNodesWindow = QtWidgets.QLabel(addSetNodes_window)
        self.startingNameLabel_addSetNodesWindow.setObjectName("startingNameLabel_addSetNodesWindow")
        self.startingNameLayout_addSetNodesWindow.addWidget(self.startingNameLabel_addSetNodesWindow)
        self.startingNameInput_addSetNodesWindow = QtWidgets.QLineEdit(addSetNodes_window)
        self.startingNameInput_addSetNodesWindow.setObjectName("startingNameInput_addSetNodesWindow")
        self.startingNameLayout_addSetNodesWindow.addWidget(self.startingNameInput_addSetNodesWindow)
        self.mainLayout_addSetNodesWindow.addLayout(self.startingNameLayout_addSetNodesWindow)
        
        self.startingIPLayout_addSetNodesWindow = QtWidgets.QHBoxLayout()
        self.startingIPLayout_addSetNodesWindow.setObjectName("startingIPLayout_addSetNodesWindow")
        self.startingIPLabel_addSetNodesWindow = QtWidgets.QLabel(addSetNodes_window)
        self.startingIPLabel_addSetNodesWindow.setObjectName("startingIPLabel_addSetNodesWindow")
        self.startingIPLayout_addSetNodesWindow.addWidget(self.startingIPLabel_addSetNodesWindow)
        self.startingIPInput_addSetNodesWindow = QtWidgets.QLineEdit(addSetNodes_window)
        self.startingIPInput_addSetNodesWindow.setObjectName("startingIPInput_addSetNodesWindow")
        self.startingIPLayout_addSetNodesWindow.addWidget(self.startingIPInput_addSetNodesWindow)
        self.mainLayout_addSetNodesWindow.addLayout(self.startingIPLayout_addSetNodesWindow)
        
        self.numberVictimNodesLayout_addSetNodesWindow = QtWidgets.QHBoxLayout()
        self.numberVictimNodesLayout_addSetNodesWindow.setObjectName("numberVictimNodesLayout_addSetNodesWindow")
        self.numberVictimNodesLabel_addSetNodesWindow = QtWidgets.QLabel(addSetNodes_window)
        self.numberVictimNodesLabel_addSetNodesWindow.setObjectName("numberVictimNodesLabel_addSetNodesWindow")
        self.numberVictimNodesLayout_addSetNodesWindow.addWidget(self.numberVictimNodesLabel_addSetNodesWindow)

        self.numberVictimNodesSpinbox_addSetNodesWindow = QtWidgets.QSpinBox(addSetNodes_window)
        self.numberVictimNodesSpinbox_addSetNodesWindow.setObjectName("numberVictimNodesSpinbox_addSetNodesWindow")
        self.numberVictimNodesSpinbox_addSetNodesWindow.setValue(1)
        self.numberVictimNodesLayout_addSetNodesWindow.addWidget(self.numberVictimNodesSpinbox_addSetNodesWindow)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.numberVictimNodesLayout_addSetNodesWindow.addItem(spacerItem)
        self.mainLayout_addSetNodesWindow.addLayout(self.numberVictimNodesLayout_addSetNodesWindow)
        self.buttonsLayout_addSetNodesWindow = QtWidgets.QHBoxLayout()
        self.buttonsLayout_addSetNodesWindow.setObjectName("buttonsLayout_addSetNodesWindow")
        self.setNodesCreateButton_addSetNodesWindow = QtWidgets.QPushButton(addSetNodes_window)
        self.setNodesCreateButton_addSetNodesWindow.setObjectName("setNodesCreateButton_addSetNodesWindow")
        self.buttonsLayout_addSetNodesWindow.addWidget(self.setNodesCreateButton_addSetNodesWindow)
        self.setNodesCancelButton_addSetNodesWindow = QtWidgets.QPushButton(addSetNodes_window)
        self.setNodesCancelButton_addSetNodesWindow.setObjectName("setNodesCancelButton_addSetNodesWindow")
        self.buttonsLayout_addSetNodesWindow.addWidget(self.setNodesCancelButton_addSetNodesWindow)
        self.mainLayout_addSetNodesWindow.addLayout(self.buttonsLayout_addSetNodesWindow)
        self.AddSetNodesWindowLayout.addLayout(self.mainLayout_addSetNodesWindow, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(addSetNodes_window)

        _translate = QtCore.QCoreApplication.translate
        addSetNodes_window.setWindowTitle(_translate("addSetNodes_window", "Add Set of Victim Nodes"))
        self.startingIPLabel_addSetNodesWindow.setText(_translate("addSetNodes_window", "Starting IP Address:     "))
        self.startingNameLabel_addSetNodesWindow.setText(_translate("addSetNodes_window", "Name:     "))
        self.numberVictimNodesLabel_addSetNodesWindow.setText(_translate("addSetNodes_window", "Number of Nodes: "))
        self.setNodesCreateButton_addSetNodesWindow.setText(_translate("addSetNodes_window", "Create"))
        self.setNodesCancelButton_addSetNodesWindow.setText(_translate("addSetNodes_window", "Cancel"))

        self.setNodesCreateButton_addSetNodesWindow.clicked.connect(lambda: self.addSetNodes(
            addSetNodes_window, projectsList_captureManagerWindow, nodesList_captureManagerWindow, id_counter, MAC))
        self.setNodesCancelButton_addSetNodesWindow.clicked.connect(addSetNodes_window.close)

        self.startingIPInput_addSetNodesWindow.setText(f"1.1.{ip_counter}.2")

    # TODO: To be implemented
    def addSetNodes(self, addSetNodes_window, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                    id_counter, MAC):
        starting_ip = self.startingIPInput_addSetNodesWindow.text()
        name = self.startingNameInput_addSetNodesWindow.text()
        split_starting_ip = starting_ip.split(".")
        num_nodes = self.numberVictimNodesSpinbox_addSetNodesWindow.value()
        scenario_name = projectsList_captureManagerWindow.selectedItems()[0].text(0)
        scenario_id = self.sds_controller.get_scenario_id(scenario_name)
        nodes_list = self.sds_controller.get_all_nodes(scenario_name)
        count = 1

        for i in range(int(split_starting_ip[3]), num_nodes + int(split_starting_ip[3]), 1):
            id_counter += 1
            MAC += 1
            node_mac = str(MAC)[1:]
            node_mac = f"{node_mac[0:2]}:{node_mac[2:4]}:{node_mac[4:6]}:{node_mac[6:8]}:{node_mac[8:10]}:{node_mac[10:12]}"
            node_ip = f"{split_starting_ip[0]}.{split_starting_ip[1]}.{split_starting_ip[2]}.{i}"
            node_name = name + str(count)
            self.sds_controller.insert_node(scenario_id, id_counter, False, "PC", node_name, node_ip, node_mac,
                                            True, False, "", "", "", 1,
                                            1, "")
            count += 1

        nodes_list = self.sds_controller.get_all_nodes(scenario_name)
        nodesList_captureManagerWindow.clear()
        for node in nodes_list:
            node_item = QTreeWidgetItem([str(node['listening']),
                                         node['type'], node['name'], node['mac'], node['ip'], str(node['scanning'])])
            nodesList_captureManagerWindow.addTopLevelItem(node_item)
        addSetNodes_window.close()
        nodesList_captureManagerWindow.header().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)

