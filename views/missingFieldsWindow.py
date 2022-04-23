from PyQt5 import QtCore, QtWidgets


class Ui_missingFields_window(object):
    def setupMissingFields(self, missingFields_window):
        missingFields_window.setObjectName("missingFields_window")
        missingFields_window.setEnabled(True)
        missingFields_window.resize(425, 160)
        missingFields_window.setMinimumSize(QtCore.QSize(425, 160))
        missingFields_window.setMaximumSize(QtCore.QSize(425, 160))
        self.MissingFieldsWindowLayout = QtWidgets.QGridLayout(missingFields_window)
        self.MissingFieldsWindowLayout.setObjectName("MissingFieldsWindowLayout")
        self.mainLayout_missingFieldsWindow = QtWidgets.QVBoxLayout()
        self.mainLayout_missingFieldsWindow.setObjectName("mainLayout_missingFieldsWindow")
        self.missingFieldsLayout_missingFieldsWindow = QtWidgets.QVBoxLayout()
        self.missingFieldsLayout_missingFieldsWindow.setObjectName("missingFieldsLayout_missingFieldsWindow")
        self.missingFieldsLabel1_missingFieldsWindow = QtWidgets.QLabel(missingFields_window)
        self.missingFieldsLabel1_missingFieldsWindow.setObjectName("missingFieldsLabel1_missingFieldsWindow")
        self.missingFieldsLayout_missingFieldsWindow.addWidget(self.missingFieldsLabel1_missingFieldsWindow)
        self.missingFieldsLabel2_missingFieldsWindow = QtWidgets.QLabel(missingFields_window)
        self.missingFieldsLabel2_missingFieldsWindow.setObjectName("missingFieldsLabel2_missingFieldsWindow")
        self.missingFieldsLayout_missingFieldsWindow.addWidget(self.missingFieldsLabel2_missingFieldsWindow)
        self.mainLayout_missingFieldsWindow.addLayout(self.missingFieldsLayout_missingFieldsWindow)
        self.missingFieldsButtonsLayout_missingFieldsWindow = QtWidgets.QHBoxLayout()
        self.missingFieldsButtonsLayout_missingFieldsWindow.setObjectName("missingFieldsButtonsLayout_missingFieldsWindow")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.missingFieldsButtonsLayout_missingFieldsWindow.addItem(spacerItem)
        self.missingFieldsCloseButton_missingFieldsWindow = QtWidgets.QPushButton(missingFields_window)
        self.missingFieldsCloseButton_missingFieldsWindow.setObjectName("missingFieldsCloseButton_missingFieldsWindow")
        self.missingFieldsButtonsLayout_missingFieldsWindow.addWidget(self.missingFieldsCloseButton_missingFieldsWindow)
        self.mainLayout_missingFieldsWindow.addLayout(self.missingFieldsButtonsLayout_missingFieldsWindow)
        self.MissingFieldsWindowLayout.addLayout(self.mainLayout_missingFieldsWindow, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(missingFields_window)

        _translate = QtCore.QCoreApplication.translate
        missingFields_window.setWindowTitle(_translate("missingFields_window", "Missing Fields "))
        self.missingFieldsLabel1_missingFieldsWindow.setText(_translate("missingFields_window", "There are some fields that had not been filled."))
        self.missingFieldsLabel2_missingFieldsWindow.setText(_translate("missingFields_window", "Please, make sure that everything is correct before you confirm."))
        self.missingFieldsCloseButton_missingFieldsWindow.setText(_translate("missingFields_window", "  Close  "))

        self.missingFieldsCloseButton_missingFieldsWindow.clicked.connect(missingFields_window.close)