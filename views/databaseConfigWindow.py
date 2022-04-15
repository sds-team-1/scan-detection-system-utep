from PyQt5 import QtCore, QtWidgets


class Ui_databaseConfig_window(object):
    def setupDatabaseConfig(self, databaseConfig_window):
        databaseConfig_window.setObjectName("databaseConfig_window")
        databaseConfig_window.setEnabled(True)
        databaseConfig_window.resize(513, 165)
        databaseConfig_window.setMinimumSize(QtCore.QSize(513, 165))
        databaseConfig_window.setMaximumSize(QtCore.QSize(513, 165))
        self.DatabaseConfigWindowLayout = QtWidgets.QGridLayout(databaseConfig_window)
        self.DatabaseConfigWindowLayout.setObjectName("DatabaseConfigWindowLayout")
        self.mainLayout_databaseConfigWindow = QtWidgets.QVBoxLayout()
        self.mainLayout_databaseConfigWindow.setObjectName("mainLayout_databaseConfigWindow")

        self.databaseConfigProtocolLayout_databaseConfigWindow = QtWidgets.QHBoxLayout()
        self.databaseConfigProtocolLayout_databaseConfigWindow.setObjectName("databaseConfigProtocolLayout_databaseConfigWindow")
        self.databaseConfigProtocolLabel_databaseConfigWindow = QtWidgets.QLabel(databaseConfig_window)
        self.databaseConfigProtocolLabel_databaseConfigWindow.setObjectName("databaseConfigProtocolLabel_databaseConfigWindow")
        self.databaseConfigProtocolLayout_databaseConfigWindow.addWidget(self.databaseConfigProtocolLabel_databaseConfigWindow)
        self.databaseConfigProtocolLabel2_databaseConfigWindow = QtWidgets.QLabel(databaseConfig_window)
        self.databaseConfigProtocolLabel2_databaseConfigWindow.setObjectName("databaseConfigProtocolLabel2_databaseConfigWindow")
        self.databaseConfigProtocolLayout_databaseConfigWindow.addWidget(self.databaseConfigProtocolLabel2_databaseConfigWindow)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.databaseConfigProtocolLayout_databaseConfigWindow.addItem(spacerItem)
        self.mainLayout_databaseConfigWindow.addLayout(self.databaseConfigProtocolLayout_databaseConfigWindow)


        self.databaseConfigIPLayout_databaseConfigWindow = QtWidgets.QHBoxLayout()
        self.databaseConfigIPLayout_databaseConfigWindow.setObjectName("databaseConfigIPLayout_databaseConfigWindow")
        self.databaseConfigIPLabel_databaseConfigWindow = QtWidgets.QLabel(databaseConfig_window)
        self.databaseConfigIPLabel_databaseConfigWindow.setObjectName("databaseConfigIPLabel_databaseConfigWindow")
        self.databaseConfigIPLayout_databaseConfigWindow.addWidget(self.databaseConfigIPLabel_databaseConfigWindow)
        self.databaseConfigIPInput_databaseConfigWindow = QtWidgets.QLineEdit(databaseConfig_window)
        self.databaseConfigIPInput_databaseConfigWindow.setObjectName("databaseConfigIPInput_databaseConfigWindow")
        self.databaseConfigIPLayout_databaseConfigWindow.addWidget(self.databaseConfigIPInput_databaseConfigWindow)
        self.mainLayout_databaseConfigWindow.addLayout(self.databaseConfigIPLayout_databaseConfigWindow)

        self.databaseConfigPortLayout_databaseConfigWindow = QtWidgets.QHBoxLayout()
        self.databaseConfigPortLayout_databaseConfigWindow.setObjectName("databaseConfigPortLayout_databaseConfigWindow")
        self.databaseConfigPortLabel_databaseConfigWindow = QtWidgets.QLabel(databaseConfig_window)
        self.databaseConfigPortLabel_databaseConfigWindow.setObjectName("databaseConfigPortLabel_databaseConfigWindow")
        self.databaseConfigPortLayout_databaseConfigWindow.addWidget(self.databaseConfigPortLabel_databaseConfigWindow)
        self.databaseConfigPortInput_databaseConfigWindow = QtWidgets.QLineEdit(databaseConfig_window)
        self.databaseConfigPortInput_databaseConfigWindow.setObjectName("databaseConfigPortInput_databaseConfigWindow")
        self.databaseConfigPortLayout_databaseConfigWindow.addWidget(self.databaseConfigPortInput_databaseConfigWindow)
        self.mainLayout_databaseConfigWindow.addLayout(self.databaseConfigPortLayout_databaseConfigWindow)


        self.databaseConfigIPButtonsLayout_databaseConfigWindow = QtWidgets.QHBoxLayout()
        self.databaseConfigIPButtonsLayout_databaseConfigWindow.setObjectName("databaseConfigIPButtonsLayout_databaseConfigWindow")
        self.databaseConfigIPConnectButton_databaseConfigWindow = QtWidgets.QPushButton(databaseConfig_window)
        self.databaseConfigIPConnectButton_databaseConfigWindow.setObjectName("databaseConfigIPConnectButton_databaseConfigWindow")
        self.databaseConfigIPButtonsLayout_databaseConfigWindow.addWidget(self.databaseConfigIPConnectButton_databaseConfigWindow)
        self.databaseConfigIPCancelButton_databaseConfigWindow = QtWidgets.QPushButton(databaseConfig_window)
        self.databaseConfigIPCancelButton_databaseConfigWindow.setObjectName("databaseConfigIPCancelButton_databaseConfigWindow")
        self.databaseConfigIPButtonsLayout_databaseConfigWindow.addWidget(self.databaseConfigIPCancelButton_databaseConfigWindow)
        self.mainLayout_databaseConfigWindow.addLayout(self.databaseConfigIPButtonsLayout_databaseConfigWindow)
        self.DatabaseConfigWindowLayout.addLayout(self.mainLayout_databaseConfigWindow, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(databaseConfig_window)

        _translate = QtCore.QCoreApplication.translate
        databaseConfig_window.setWindowTitle(_translate("databaseConfig_window", "Database Configuration"))
        self.databaseConfigProtocolLabel_databaseConfigWindow.setText( _translate("databaseConfig_window", "Database Protocol:"))
        self.databaseConfigProtocolLabel2_databaseConfigWindow.setText(_translate("databaseConfig_window", "    mongodb://"))
        self.databaseConfigIPLabel_databaseConfigWindow.setText(_translate("databaseConfig_window", "Database IP Address:"))
        self.databaseConfigPortLabel_databaseConfigWindow.setText(_translate("databaseConfig_window", "Database Port:           "))
        self.databaseConfigIPConnectButton_databaseConfigWindow.setText(_translate("databaseConfig_window", "Connect"))
        self.databaseConfigIPCancelButton_databaseConfigWindow.setText(_translate("databaseConfig_window", "Cancel"))
