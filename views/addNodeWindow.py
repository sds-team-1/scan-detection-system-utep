from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem


class Ui_addNode_window(object):
    def setupAddNode(self, addNode_window, sds_controller,
                     projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                     CentralLayout_captureManagerWindow, ip_counter, MAC, id_counter):
        self.sds_controller = sds_controller
        addNode_window.setObjectName("addNode_window")
        addNode_window.setEnabled(True)
        addNode_window.resize(487, 240)
        addNode_window.setMinimumSize(QtCore.QSize(487, 240))
        addNode_window.setMaximumSize(QtCore.QSize(487, 240))
        self.AddNodeWindowLayout = QtWidgets.QGridLayout(addNode_window)
        self.AddNodeWindowLayout.setObjectName("AddNodeWindowLayout")
        self.mainLayout_addNodeWindow = QtWidgets.QVBoxLayout()
        self.mainLayout_addNodeWindow.setObjectName("mainLayout_addNodeWindow")
        self.nodeTypeLayout_addNodeWindow = QtWidgets.QHBoxLayout()
        self.nodeTypeLayout_addNodeWindow.setObjectName("nodeTypeLayout_addNodeWindow")
        self.nodeTypeLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
        self.nodeTypeLabel_addNodeWindow.setObjectName("nodeTypeLabel_addNodeWindow")
        self.nodeTypeLayout_addNodeWindow.addWidget(self.nodeTypeLabel_addNodeWindow)
        self.nodeTypeComboBox_addNodeWindow = QtWidgets.QComboBox(addNode_window)
        self.nodeTypeComboBox_addNodeWindow.setObjectName("nodeTypeComboBox_addNodeWindow")
        self.nodeTypeLayout_addNodeWindow.addWidget(self.nodeTypeComboBox_addNodeWindow)
        self.nodeTypeComboBox_addNodeWindow.addItem('CORE')
        self.nodeTypeComboBox_addNodeWindow.addItem('VM')
        self.nodeTypeComboBox_addNodeWindow.addItem('Docker ')
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.nodeTypeLayout_addNodeWindow.addItem(self.spacerItem)
        self.mainLayout_addNodeWindow.addLayout(self.nodeTypeLayout_addNodeWindow)
        self.nodeNameLayout_addNodeWindow = QtWidgets.QHBoxLayout()
        self.nodeNameLayout_addNodeWindow.setObjectName("nodeNameLayout_addNodeWindow")
        self.nodeNameLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
        self.nodeNameLabel_addNodeWindow.setObjectName("nodeNameLabel_addNodeWindow")
        self.nodeNameLayout_addNodeWindow.addWidget(self.nodeNameLabel_addNodeWindow)
        self.nodeNameInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
        self.nodeNameInput_addNodeWindow.setObjectName("nodeNameInput_addNodeWindow")
        self.nodeNameLayout_addNodeWindow.addWidget(self.nodeNameInput_addNodeWindow)
        self.mainLayout_addNodeWindow.addLayout(self.nodeNameLayout_addNodeWindow)
        self.nodeMACAddressLayout_addNodeWindow = QtWidgets.QHBoxLayout()
        self.nodeMACAddressLayout_addNodeWindow.setObjectName("nodeMACAddressLayout_addNodeWindow")
        self.nodeMACAddressLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
        self.nodeMACAddressLabel_addNodeWindow.setObjectName("nodeMACAddressLabel_addNodeWindow")
        self.nodeMACAddressLayout_addNodeWindow.addWidget(self.nodeMACAddressLabel_addNodeWindow)
        self.nodeMACAddressInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
        self.nodeMACAddressInput_addNodeWindow.setObjectName("nodeMACAddressInput_addNodeWindow")
        self.nodeMACAddressLayout_addNodeWindow.addWidget(self.nodeMACAddressInput_addNodeWindow)
        self.mainLayout_addNodeWindow.addLayout(self.nodeMACAddressLayout_addNodeWindow)
        self.nodeIPAddressLayout_addNodeWindow = QtWidgets.QHBoxLayout()
        self.nodeIPAddressLayout_addNodeWindow.setObjectName("nodeIPAddressLayout_addNodeWindow")
        self.nodeIPAddressLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
        self.nodeIPAddressLabel_addNodeWindow.setObjectName("nodeIPAddressLabel_addNodeWindow")
        self.nodeIPAddressLayout_addNodeWindow.addWidget(self.nodeIPAddressLabel_addNodeWindow)
        self.nodeIPAddressInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
        self.nodeIPAddressInput_addNodeWindow.setObjectName("nodeIPAddressInput_addNodeWindow")
        self.nodeIPAddressLayout_addNodeWindow.addWidget(self.nodeIPAddressInput_addNodeWindow)
        self.mainLayout_addNodeWindow.addLayout(self.nodeIPAddressLayout_addNodeWindow)

        self.nodeScannerNodeLayout_addNodeWindow = QtWidgets.QHBoxLayout()
        self.nodeScannerNodeLayout_addNodeWindow.setObjectName("nodeScannerNodeLayout_addNodeWindow")
        self.spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.nodeScannerNodeLayout_addNodeWindow.addItem(self.spacerItem1)
        self.nodeWebServerNodeCheckBox_addNodeWindow = QtWidgets.QCheckBox(addNode_window)
        self.nodeWebServerNodeCheckBox_addNodeWindow.setObjectName("nodeWebServerNodeCheckBox_addNodeWindow")
        self.nodeScannerNodeLayout_addNodeWindow.addWidget(self.nodeWebServerNodeCheckBox_addNodeWindow)
        self.nodeLogNetNodeCheckBox_addNodeWindow = QtWidgets.QCheckBox(addNode_window)
        self.nodeLogNetNodeCheckBox_addNodeWindow.setObjectName("nodeLogNetNodeCheckBox_addNodeWindow")
        self.nodeScannerNodeLayout_addNodeWindow.addWidget(self.nodeLogNetNodeCheckBox_addNodeWindow)
        self.nodeScannerNodeCheckBox_addNodeWindow = QtWidgets.QCheckBox(addNode_window)
        self.nodeScannerNodeCheckBox_addNodeWindow.setObjectName("nodeScannerNodeCheckBox_addNodeWindow")
        self.nodeScannerNodeLayout_addNodeWindow.addWidget(self.nodeScannerNodeCheckBox_addNodeWindow)
        self.mainLayout_addNodeWindow.addLayout(self.nodeScannerNodeLayout_addNodeWindow)

        self.addNodeButtonsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
        self.addNodeButtonsLayout_addNodeWindow.setObjectName("addNodeButtonsLayout_addNodeWindow")
        self.addNodeButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
        self.addNodeButton_addNodeWindow.setObjectName("addNodeButton_addNodeWindow")
        self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeButton_addNodeWindow)
        self.addNodeCancelButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
        self.addNodeCancelButton_addNodeWindow.setObjectName("addNodeCancelButton_addNodeWindow")
        self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeCancelButton_addNodeWindow)
        self.mainLayout_addNodeWindow.addLayout(self.addNodeButtonsLayout_addNodeWindow)
        self.AddNodeWindowLayout.addLayout(self.mainLayout_addNodeWindow, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(addNode_window)

        _translate = QtCore.QCoreApplication.translate
        addNode_window.setWindowTitle(_translate("addNode_window", "Add New Node"))
        self.nodeTypeLabel_addNodeWindow.setText(_translate("addNode_window", "Type:                    "))
        self.nodeNameLabel_addNodeWindow.setText(_translate("addNode_window", "Node Name:          "))
        self.nodeMACAddressLabel_addNodeWindow.setText(_translate("addNode_window", "MAC Address:       "))
        self.nodeIPAddressLabel_addNodeWindow.setText(_translate("addNode_window", "IP Address:            "))
        self.nodeWebServerNodeCheckBox_addNodeWindow.setText(_translate("addNode_window", "Web Server"))
        self.nodeLogNetNodeCheckBox_addNodeWindow.setText(_translate("addNode_window", "Log Network Traffic"))
        self.nodeScannerNodeCheckBox_addNodeWindow.setText(_translate("addNode_window", "Scanner Node"))
        self.addNodeButton_addNodeWindow.setText(_translate("addNode_window", "Add Node"))
        self.addNodeCancelButton_addNodeWindow.setText(_translate("addNode_window", "Cancel"))

        self.nodeScannerNodeCheckBox_addNodeWindow.toggled.connect(lambda: self.scannerNode(
            addNode_window, _translate, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
            CentralLayout_captureManagerWindow, id_counter))

        self.addNodeButton_addNodeWindow.clicked.connect(lambda: self.addNode(
            addNode_window, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
            CentralLayout_captureManagerWindow, id_counter))
        self.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_window.close)

        self.nodeIPAddressInput_addNodeWindow.setText(f"1.1.{ip_counter}.2")

        MAC += 1
        node_mac = str(MAC)[1:]
        node_mac = f"{node_mac[0:2]}:{node_mac[2:4]}:{node_mac[4:6]}:{node_mac[6:8]}:{node_mac[8:10]}:{node_mac[10:12]}"
        self.nodeMACAddressInput_addNodeWindow.setText(node_mac)

    def scannerNode(self, addNode_window, _translate, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                    CentralLayout_captureManagerWindow, id_counter):
        if self.nodeScannerNodeCheckBox_addNodeWindow.isChecked():
            self.nmapFlag = False
            self.niktoFlag = False
            addNode_window.resize(487, 490)
            addNode_window.setMinimumSize(QtCore.QSize(487, 490))
            addNode_window.setMaximumSize(QtCore.QSize(487, 490))

            self.addNodeButton_addNodeWindow.deleteLater()
            self.addNodeCancelButton_addNodeWindow.deleteLater()
            self.mainLayout_addNodeWindow.removeItem(self.addNodeButtonsLayout_addNodeWindow)

            self.nodeUserPassLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeUserPassLayout_addNodeWindow.setObjectName("nodeUserPassLayout_addNodeWindow")
            self.nodeUserPassLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeUserPassLabel_addNodeWindow.setObjectName("nodeUserPassLabel_addNodeWindow")
            self.nodeUserPassLayout_addNodeWindow.addWidget(self.nodeUserPassLabel_addNodeWindow)
            self.nodeUserPassInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
            self.nodeUserPassInput_addNodeWindow.setObjectName("nodeUserPassInput_addNodeWindow")
            self.nodeUserPassLayout_addNodeWindow.addWidget(self.nodeUserPassInput_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.nodeUserPassLayout_addNodeWindow)
            self.nodeScannerBinaryLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeScannerBinaryLayout_addNodeWindow.setObjectName("nodeScannerBinaryLayout_addNodeWindow")
            self.nodeScannerBinaryLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeScannerBinaryLabel_addNodeWindow.setObjectName("nodeScannerBinaryLabel_addNodeWindow")
            self.nodeScannerBinaryLayout_addNodeWindow.addWidget(self.nodeScannerBinaryLabel_addNodeWindow)
            self.nodeScannerBinaryInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
            self.nodeScannerBinaryInput_addNodeWindow.setObjectName("nodeScannerBinaryInput_addNodeWindow")
            self.nodeScannerBinaryLayout_addNodeWindow.addWidget(self.nodeScannerBinaryInput_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.nodeScannerBinaryLayout_addNodeWindow)

            self.nodeScannersNNNodeLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeScannersNNNodeLayout_addNodeWindow.setObjectName("nodeScannersNNNodeLayout_addNodeWindow")
            self.spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
            self.nodeScannersNNNodeLayout_addNodeWindow.addItem(self.spacerItem1)
            self.nodeNMapNodeCheckBox_addNodeWindow = QtWidgets.QCheckBox(addNode_window)
            self.nodeNMapNodeCheckBox_addNodeWindow.setObjectName("nodeNMapNodeCheckBox_addNodeWindow")
            self.nodeScannersNNNodeLayout_addNodeWindow.addWidget(self.nodeNMapNodeCheckBox_addNodeWindow)
            self.nodeNiktoNodeCheckBox_addNodeWindow = QtWidgets.QCheckBox(addNode_window)
            self.nodeNiktoNodeCheckBox_addNodeWindow.setObjectName("nodeNiktoNodeCheckBox_addNodeWindow")
            self.nodeScannersNNNodeLayout_addNodeWindow.addWidget(self.nodeNiktoNodeCheckBox_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.nodeScannersNNNodeLayout_addNodeWindow)

            self.nodeNMapNodeCheckBox_addNodeWindow.toggled.connect(self.nmapSignal)
            self.nodeNiktoNodeCheckBox_addNodeWindow.toggled.connect(self.niktoSignal)

            self.nodeNMapArgumentsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeNMapArgumentsLayout_addNodeWindow.setObjectName("nodeNMapArgumentsLayout_addNodeWindow")
            self.nodeNMapArgumentsLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeNMapArgumentsLabel_addNodeWindow.setObjectName("nodeNMapArgumentsLabel_addNodeWindow")
            self.nodeNMapArgumentsLayout_addNodeWindow.addWidget(self.nodeNMapArgumentsLabel_addNodeWindow)
            self.nodeNMapArgumentsInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
            self.nodeNMapArgumentsInput_addNodeWindow.setObjectName("nodeNMapArgumentsInput_addNodeWindow")
            self.nodeNMapArgumentsLayout_addNodeWindow.addWidget(self.nodeNMapArgumentsInput_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.nodeNMapArgumentsLayout_addNodeWindow)
            self.nodeNMapArgumentsInput_addNodeWindow.setDisabled(True)

            self.nodeNiktoArgumentsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeNiktoArgumentsLayout_addNodeWindow.setObjectName("nodeNiktoArgumentsLayout_addNodeWindow")
            self.nodeNiktoArgumentsLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeNiktoArgumentsLabel_addNodeWindow.setObjectName("nodeNiktoArgumentsLabel_addNodeWindow")
            self.nodeNiktoArgumentsLayout_addNodeWindow.addWidget(self.nodeNiktoArgumentsLabel_addNodeWindow)
            self.nodeNiktoArgumentsInput_addNodeWindow = QtWidgets.QLineEdit(addNode_window)
            self.nodeNiktoArgumentsInput_addNodeWindow.setObjectName("nodeNiktoArgumentsInput_addNodeWindow")
            self.nodeNiktoArgumentsLayout_addNodeWindow.addWidget(self.nodeNiktoArgumentsInput_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.nodeNiktoArgumentsLayout_addNodeWindow)
            self.nodeNiktoArgumentsInput_addNodeWindow.setDisabled(True)

            self.nodeNumIterationsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeNumIterationsLayout_addNodeWindow.setObjectName("nodeNumIterationsLayout_addNodeWindow")
            self.nodeNumIterationsLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeNumIterationsLabel_addNodeWindow.setObjectName("nodeNumIterationsLabel_addNodeWindow")
            self.nodeNumIterationsLayout_addNodeWindow.addWidget(self.nodeNumIterationsLabel_addNodeWindow)
            self.nodeNumIterationsSpinBox_addNodeWindow = QtWidgets.QSpinBox(addNode_window)
            self.nodeNumIterationsSpinBox_addNodeWindow.setObjectName("nodeNumIterationsSpinBox_addNodeWindow")
            self.nodeNumIterationsSpinBox_addNodeWindow.setValue(1)
            self.nodeNumIterationsLayout_addNodeWindow.addWidget(self.nodeNumIterationsSpinBox_addNodeWindow)
            self.spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
            self.nodeNumIterationsLayout_addNodeWindow.addItem(self.spacerItem2)
            self.mainLayout_addNodeWindow.addLayout(self.nodeNumIterationsLayout_addNodeWindow)
            self.nodeMaxParallelRunsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeMaxParallelRunsLayout_addNodeWindow.setObjectName("nodeMaxParallelRunsLayout_addNodeWindow")
            self.nodeMaxParallelRunsLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeMaxParallelRunsLabel_addNodeWindow.setObjectName("nodeMaxParallelRunsLabel_addNodeWindow")
            self.nodeMaxParallelRunsLayout_addNodeWindow.addWidget(self.nodeMaxParallelRunsLabel_addNodeWindow)
            self.nodeMaxParallelRunsSpinBox_addNodeWindow = QtWidgets.QSpinBox(addNode_window)
            self.nodeMaxParallelRunsSpinBox_addNodeWindow.setObjectName("nodeMaxParallelRunsSpinBox_addNodeWindow")
            self.nodeMaxParallelRunsSpinBox_addNodeWindow.setValue(1)
            self.nodeMaxParallelRunsLayout_addNodeWindow.addWidget(self.nodeMaxParallelRunsSpinBox_addNodeWindow)
            self.spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
            self.nodeMaxParallelRunsLayout_addNodeWindow.addItem(self.spacerItem3)
            self.mainLayout_addNodeWindow.addLayout(self.nodeMaxParallelRunsLayout_addNodeWindow)

            self.nodeEndConditionLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.nodeEndConditionLayout_addNodeWindow.setObjectName("nodeEndConditionLayout_addNodeWindow")
            self.nodeEndConditionLabel_addNodeWindow = QtWidgets.QLabel(addNode_window)
            self.nodeEndConditionLabel_addNodeWindow.setObjectName("nodeEndConditionLabel_addNodeWindow")
            self.nodeEndConditionLayout_addNodeWindow.addWidget(self.nodeEndConditionLabel_addNodeWindow)

            self.nodeEndConditionCombobox_addNodeWindow = QtWidgets.QComboBox(addNode_window)
            self.nodeEndConditionCombobox_addNodeWindow.setObjectName("nodeEndConditionCombobox_addNodeWindow")
            self.nodeEndConditionCombobox_addNodeWindow.addItem('on-scan-complete')
            self.nodeEndConditionCombobox_addNodeWindow.addItem('Time...')
            self.nodeEndConditionLayout_addNodeWindow.addWidget(self.nodeEndConditionCombobox_addNodeWindow)
            self.spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
            self.nodeEndConditionLayout_addNodeWindow.addItem(self.spacerItem4)

            self.nodeEndConditionCombobox_addNodeWindow.currentIndexChanged.connect(lambda: self.end_condition_changed(
                addNode_window, _translate, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                CentralLayout_captureManagerWindow, id_counter))

            self.mainLayout_addNodeWindow.addLayout(self.nodeEndConditionLayout_addNodeWindow)

            self.nodeUserPassLabel_addNodeWindow.setText(_translate("addNode_window", "User/Pass:             "))
            self.nodeScannerBinaryLabel_addNodeWindow.setText(_translate("addNode_window", "Scanner-Binary:    "))

            self.nodeNMapNodeCheckBox_addNodeWindow.setText(_translate("addNode_window", "NMap"))
            self.nodeNiktoNodeCheckBox_addNodeWindow.setText(_translate("addNode_window", "Nikto"))

            self.nodeNMapArgumentsLabel_addNodeWindow.setText(_translate("addNode_window", "NMap Arguments: "))
            self.nodeNiktoArgumentsLabel_addNodeWindow.setText(_translate("addNode_window", "Nikto Arguments:  "))

            self.nodeNumIterationsLabel_addNodeWindow.setText(_translate("addNode_window", "Number-Iterations:"))
            self.nodeMaxParallelRunsLabel_addNodeWindow.setText(_translate("addNode_window", "Max-Parallel-Runs:"))
            self.nodeEndConditionLabel_addNodeWindow.setText(_translate("addNode_window", "End-Condition:       "))

            self.addNodeButtonsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.addNodeButtonsLayout_addNodeWindow.setObjectName("addNodeButtonsLayout_addNodeWindow")
            self.addNodeButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.addNodeButton_addNodeWindow.setObjectName("addNodeButton_addNodeWindow")
            self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeButton_addNodeWindow)
            self.addNodeCancelButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.addNodeCancelButton_addNodeWindow.setObjectName("addNodeCancelButton_addNodeWindow")
            self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeCancelButton_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.addNodeButtonsLayout_addNodeWindow)
            self.addNodeButton_addNodeWindow.setText(_translate("addNode_window", "Add Node"))
            self.addNodeCancelButton_addNodeWindow.setText(_translate("addNode_window", "Cancel"))

            self.addNodeButton_addNodeWindow.clicked.connect(lambda: self.addNode(
                addNode_window, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                CentralLayout_captureManagerWindow, id_counter))
            self.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_window.close)

        else:
            addNode_window.resize(487, 240)
            addNode_window.setMinimumSize(QtCore.QSize(487, 240))
            addNode_window.setMaximumSize(QtCore.QSize(487, 240))

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
                self.mainLayout_addNodeWindow.removeItem(self.nodeTimeLayout_addNodeWindow)
            self.nodeEndConditionCombobox_addNodeWindow.deleteLater()

            self.mainLayout_addNodeWindow.removeItem(self.nodeUserPassLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.nodeScannerBinaryLayout_addNodeWindow)

            self.mainLayout_addNodeWindow.removeItem(self.nodeNMapArgumentsLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.nodeNiktoArgumentsLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.nodeScannersNNNodeLayout_addNodeWindow)

            self.mainLayout_addNodeWindow.removeItem(self.nodeNumIterationsLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.nodeMaxParallelRunsLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.nodeEndConditionLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.addNodeButtonsLayout_addNodeWindow)

            self.addNodeButton_addNodeWindow.deleteLater()
            self.addNodeCancelButton_addNodeWindow.deleteLater()
            self.mainLayout_addNodeWindow.removeItem(self.addNodeButtonsLayout_addNodeWindow)

            self.addNodeButtonsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.addNodeButtonsLayout_addNodeWindow.setObjectName("addNodeButtonsLayout_addNodeWindow")
            self.addNodeButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.addNodeButton_addNodeWindow.setObjectName("addNodeButton_addNodeWindow")
            self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeButton_addNodeWindow)
            self.addNodeCancelButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.addNodeCancelButton_addNodeWindow.setObjectName("addNodeCancelButton_addNodeWindow")
            self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeCancelButton_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.addNodeButtonsLayout_addNodeWindow)
            self.addNodeButton_addNodeWindow.setText(_translate("addNode_window", "Add Node"))
            self.addNodeCancelButton_addNodeWindow.setText(_translate("addNode_window", "Cancel"))

            self.addNodeButton_addNodeWindow.clicked.connect(lambda: self.addNode(
                addNode_window, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                CentralLayout_captureManagerWindow, id_counter))
            self.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_window.close)

    def end_condition_changed(self, addNode_window, _translate, projectsList_captureManagerWindow,
                              nodesList_captureManagerWindow, CentralLayout_captureManagerWindow, id_counter):
        if self.nodeEndConditionCombobox_addNodeWindow.currentText() == 'Time...':
            addNode_window.resize(487, 490)
            addNode_window.setMinimumSize(QtCore.QSize(487, 490))
            addNode_window.setMaximumSize(QtCore.QSize(487, 490))

            self.addNodeButton_addNodeWindow.deleteLater()
            self.addNodeCancelButton_addNodeWindow.deleteLater()
            self.mainLayout_addNodeWindow.removeItem(self.addNodeButtonsLayout_addNodeWindow)

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
            self.mainLayout_addNodeWindow.addLayout(self.nodeTimeLayout_addNodeWindow)

            self.addNodeButtonsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.addNodeButtonsLayout_addNodeWindow.setObjectName("addNodeButtonsLayout_addNodeWindow")
            self.addNodeButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.addNodeButton_addNodeWindow.setObjectName("addNodeButton_addNodeWindow")
            self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeButton_addNodeWindow)
            self.addNodeCancelButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.addNodeCancelButton_addNodeWindow.setObjectName("addNodeCancelButton_addNodeWindow")
            self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeCancelButton_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.addNodeButtonsLayout_addNodeWindow)
            self.minutesLabel_addNodeWindow.setText(_translate("addNode_window", "Minutes:"))
            self.secondsLabel_addNodeWindow.setText(_translate("addNode_window", "Seconds:"))
            self.addNodeButton_addNodeWindow.setText(_translate("addNode_window", "Add Node"))
            self.addNodeCancelButton_addNodeWindow.setText(_translate("addNode_window", "Cancel"))

            self.addNodeButton_addNodeWindow.clicked.connect(lambda: self.addNode(
                addNode_window, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                CentralLayout_captureManagerWindow, id_counter))
            self.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_window.close)

        else:
            addNode_window.resize(487, 460)
            addNode_window.setMinimumSize(QtCore.QSize(487, 460))
            addNode_window.setMaximumSize(QtCore.QSize(487, 460))

            self.minutesLabel_addNodeWindow.deleteLater()
            self.minutesSpinbox_addNodeWindow.deleteLater()
            self.secondsLabel_addNodeWindow.deleteLater()
            self.secondsSpinbox_addNodeWindow.deleteLater()

            self.mainLayout_addNodeWindow.removeItem(self.addNodeButtonsLayout_addNodeWindow)
            self.mainLayout_addNodeWindow.removeItem(self.nodeTimeLayout_addNodeWindow)

            self.addNodeButton_addNodeWindow.deleteLater()
            self.addNodeCancelButton_addNodeWindow.deleteLater()
            self.mainLayout_addNodeWindow.removeItem(self.addNodeButtonsLayout_addNodeWindow)

            self.addNodeButtonsLayout_addNodeWindow = QtWidgets.QHBoxLayout()
            self.addNodeButtonsLayout_addNodeWindow.setObjectName("addNodeButtonsLayout_addNodeWindow")
            self.addNodeButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.addNodeButton_addNodeWindow.setObjectName("addNodeButton_addNodeWindow")
            self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeButton_addNodeWindow)
            self.addNodeCancelButton_addNodeWindow = QtWidgets.QPushButton(addNode_window)
            self.addNodeCancelButton_addNodeWindow.setObjectName("addNodeCancelButton_addNodeWindow")
            self.addNodeButtonsLayout_addNodeWindow.addWidget(self.addNodeCancelButton_addNodeWindow)
            self.mainLayout_addNodeWindow.addLayout(self.addNodeButtonsLayout_addNodeWindow)
            self.addNodeButton_addNodeWindow.setText(_translate("addNode_window", "Add Node"))
            self.addNodeCancelButton_addNodeWindow.setText(_translate("addNode_window", "Cancel"))

            self.addNodeButton_addNodeWindow.clicked.connect(lambda: self.addNode(
                addNode_window, projectsList_captureManagerWindow, nodesList_captureManagerWindow,
                CentralLayout_captureManagerWindow, id_counter))
            self.addNodeCancelButton_addNodeWindow.clicked.connect(addNode_window.close)

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
        if self.nodeLogNetNodeCheckBox_addNodeWindow.isChecked():
            log = 'True'
        else:
            log = 'False'
        type = self.nodeTypeComboBox_addNodeWindow.currentText()
        if type == 'CORE' or type == 'VM':
            type = 'PC'
        elif type == 'VM' or type == 'Docker':
            type = 'PC'  # temp solution
        name = self.nodeNameInput_addNodeWindow.text()
        MAC = self.nodeMACAddressInput_addNodeWindow.text()
        IP = self.nodeIPAddressInput_addNodeWindow.text()
        IP_parse = IP.split(".")
        ip_counter = int(IP_parse[2]) + 1
        # subnet = addNodeWindowUI.nodeSeparateSubNetNodeCheckBox_addNodeWindow.isChecked()
        user_pw = ''
        scanner_bin = ''
        arguments = ''
        num_iterations = 1
        max_parallel_runs = 1
        end_condition = ''
        scanning = self.nodeScannerNodeCheckBox_addNodeWindow.isChecked()
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
