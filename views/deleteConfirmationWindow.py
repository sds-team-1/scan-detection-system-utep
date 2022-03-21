from PyQt5 import QtCore, QtWidgets


class Ui_deleteConfirmation_window(object):
    def setupDeleteConfirmation(self, deleteConfirmation_window):
        deleteConfirmation_window.setObjectName("deleteConfirmation_window")
        deleteConfirmation_window.setEnabled(True)
        deleteConfirmation_window.resize(415, 160)
        deleteConfirmation_window.setMinimumSize(QtCore.QSize(300, 160))
        deleteConfirmation_window.setMaximumSize(QtCore.QSize(415, 160))
        self.DeleteConfirmationWindowLayout = QtWidgets.QGridLayout(deleteConfirmation_window)
        self.DeleteConfirmationWindowLayout.setObjectName("DeleteConfirmationWindowLayout")
        self.mainLayout_deleteConfirmation_window = QtWidgets.QVBoxLayout()
        self.mainLayout_deleteConfirmation_window.setObjectName("mainLayout_deleteConfirmation_window")
        self.deleteConfirmationLayout_deleteConfirmationWindow = QtWidgets.QVBoxLayout()
        self.deleteConfirmationLayout_deleteConfirmationWindow.setObjectName("deleteConfirmationLayout_deleteConfirmationWindow")
        self.deleteConfirmationLabel_deleteConfirmationWindow = QtWidgets.QLabel(deleteConfirmation_window)
        self.deleteConfirmationLabel_deleteConfirmationWindow.setObjectName("deleteConfirmationLabel_deleteConfirmationWindow")
        self.deleteConfirmationLayout_deleteConfirmationWindow.addWidget(self.deleteConfirmationLabel_deleteConfirmationWindow)
        self.mainLayout_deleteConfirmation_window.addLayout(self.deleteConfirmationLayout_deleteConfirmationWindow)
        self.deleteConfirmationButtonsLayout_deleteConfirmationWindow = QtWidgets.QHBoxLayout()
        self.deleteConfirmationButtonsLayout_deleteConfirmationWindow.setObjectName("deleteConfirmationButtonsLayout_deleteConfirmationWindow")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.deleteConfirmationButtonsLayout_deleteConfirmationWindow.addItem(spacerItem)
        self.cancelConfirmationButton_deleteConfirmationWindow = QtWidgets.QPushButton(deleteConfirmation_window)
        self.cancelConfirmationButton_deleteConfirmationWindow.setObjectName("cancelConfirmationButton_deleteConfirmationWindow")
        self.deleteConfirmationButtonsLayout_deleteConfirmationWindow.addWidget(self.cancelConfirmationButton_deleteConfirmationWindow)
        self.deleteConfirmationButton_deleteConfirmationWindow = QtWidgets.QPushButton(deleteConfirmation_window)
        self.deleteConfirmationButton_deleteConfirmationWindow.setObjectName("deleteConfirmationButton_deleteConfirmationWindow")
        self.deleteConfirmationButtonsLayout_deleteConfirmationWindow.addWidget(self.deleteConfirmationButton_deleteConfirmationWindow)
        self.mainLayout_deleteConfirmation_window.addLayout(self.deleteConfirmationButtonsLayout_deleteConfirmationWindow)
        self.DeleteConfirmationWindowLayout.addLayout(self.mainLayout_deleteConfirmation_window, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(deleteConfirmation_window)

        _translate = QtCore.QCoreApplication.translate
        deleteConfirmation_window.setWindowTitle(_translate("deleteConfirmation_window", "Delete Confirmation"))
        self.deleteConfirmationLabel_deleteConfirmationWindow.setText(_translate("deleteConfirmation_window", "Are you sure you want to delete \"\"?"))
        self.cancelConfirmationButton_deleteConfirmationWindow.setText(_translate("deleteConfirmation_window", "  Cancel  "))
        self.deleteConfirmationButton_deleteConfirmationWindow.setText(_translate("deleteConfirmation_window", "  Delete  "))
