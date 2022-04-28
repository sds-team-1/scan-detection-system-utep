from PyQt5 import QtCore, QtWidgets


class Ui_databaseError_window(object):
    def setupDatabaseError(self, databaseError_window):
        databaseError_window.setObjectName("databaseError_window")
        databaseError_window.setEnabled(True)
        databaseError_window.resize(415, 160)
        databaseError_window.setMinimumSize(QtCore.QSize(300, 160))
        databaseError_window.setMaximumSize(QtCore.QSize(415, 160))
        self.DatabaseErrorWindowLayout = QtWidgets.QGridLayout(databaseError_window)
        self.DatabaseErrorWindowLayout.setObjectName("DatabaseErrorWindowLayout")
        self.mainLayout_databaseErrorWindow = QtWidgets.QVBoxLayout()
        self.mainLayout_databaseErrorWindow.setObjectName("mainLayout_databaseErrorWindow")
        self.databaseErrorLayout_databaseErrorWindow = QtWidgets.QVBoxLayout()
        self.databaseErrorLayout_databaseErrorWindow.setObjectName("databaseErrorLayout_databaseErrorWindow")
        self.databaseErrorLabel1_databaseErrorWindow = QtWidgets.QLabel(databaseError_window)
        self.databaseErrorLabel1_databaseErrorWindow.setObjectName("databaseErrorLabel1_databaseErrorWindow")
        self.databaseErrorLayout_databaseErrorWindow.addWidget(self.databaseErrorLabel1_databaseErrorWindow)
        self.databaseErrorLabel2_databaseErrorWindow = QtWidgets.QLabel(databaseError_window)
        self.databaseErrorLabel2_databaseErrorWindow.setObjectName("databaseErrorLabel2_databaseErrorWindow")
        self.databaseErrorLayout_databaseErrorWindow.addWidget(self.databaseErrorLabel2_databaseErrorWindow)
        self.mainLayout_databaseErrorWindow.addLayout(self.databaseErrorLayout_databaseErrorWindow)
        self.databaseErrorButtonsLayout_databaseErrorWindow = QtWidgets.QHBoxLayout()
        self.databaseErrorButtonsLayout_databaseErrorWindow.setObjectName("databaseErrorButtonsLayout_databaseErrorWindow")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.databaseErrorButtonsLayout_databaseErrorWindow.addItem(spacerItem)
        self.databaseErrorCloseButton_databaseErrorWindow = QtWidgets.QPushButton(databaseError_window)
        self.databaseErrorCloseButton_databaseErrorWindow.setObjectName("databaseErrorCloseButton_databaseErrorWindow")
        self.databaseErrorButtonsLayout_databaseErrorWindow.addWidget(self.databaseErrorCloseButton_databaseErrorWindow)
        self.mainLayout_databaseErrorWindow.addLayout(self.databaseErrorButtonsLayout_databaseErrorWindow)
        self.DatabaseErrorWindowLayout.addLayout(self.mainLayout_databaseErrorWindow, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(databaseError_window)

        _translate = QtCore.QCoreApplication.translate
        databaseError_window.setWindowTitle(_translate("databaseError_window", "Database Error Connection"))
        self.databaseErrorLabel1_databaseErrorWindow.setText(_translate("databaseError_window", "The database connection was not successful."))
        self.databaseErrorLabel2_databaseErrorWindow.setText(_translate("databaseError_window", "Please, try again."))
        self.databaseErrorCloseButton_databaseErrorWindow.setText(_translate("databaseError_window", "  Close  "))

        self.databaseErrorCloseButton_databaseErrorWindow.clicked.connect(databaseError_window.close)
