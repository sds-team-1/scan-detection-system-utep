import json
import os
import uuid

from PyQt5 import QtCore, QtWidgets

from Database.databaseFunctions import set_up_database_connection, connect_subsystems_and_database
from views.databaseErrorWindow import Ui_databaseError_window


class Ui_databaseConfig_window(object):
    def setupDatabaseConfig(self, databaseConfig_window, sds_controller, workspacesList_workspaceWindow):
        self.workspacesList_workspaceWindow = workspacesList_workspaceWindow
        self.sds_controller = sds_controller
        db_config_filename = 'conf/db_config.json'
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

        self.databaseConfigIPConnectButton_databaseConfigWindow.clicked.connect(lambda: self.connect_database(databaseConfig_window, db_config_filename))
        self.databaseConfigIPCancelButton_databaseConfigWindow.clicked.connect(
            databaseConfig_window.close)

    def connect_database(self, databaseConfig_window, db_config_filename):
        database_ip = self.databaseConfigIPInput_databaseConfigWindow.text()
        # Edit config file to insert database ip
        data = None
        with open(db_config_filename, 'r') as config_file:
            data = json.load(config_file)
            data['ip'] = database_ip
        tempfile = os.path.join(os.path.dirname(db_config_filename), str(uuid.uuid4()))
        with open(tempfile, 'w') as config_file:
            json.dump(data, config_file, indent=4)
        os.replace(tempfile, db_config_filename)
        # Try to set up controller w/ database again
        mongo_connection, connection_success = set_up_database_connection()
        if connection_success:
            connect_subsystems_and_database(self.workspacesList_workspaceWindow, self.sds_controller, mongo_connection)
            # If success -> close window
            databaseConfig_window.close()
        else:
            databaseError_Window = QtWidgets.QDialog()
            databaseErrorWindowUI = Ui_databaseError_window()
            databaseErrorWindowUI.setupDatabaseError(databaseError_Window)
            databaseError_Window.show()
