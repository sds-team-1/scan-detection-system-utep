from PyQt5 import QtCore, QtWidgets


class Ui_newWorkspace_window(object):
    def setupCreateWorkspace(self, newWorkspace_window : QtWidgets.QDialog):
        newWorkspace_window.setObjectName("newWorkspace_window")
        newWorkspace_window.setEnabled(True)
        newWorkspace_window.resize(487, 120)
        newWorkspace_window.setMinimumSize(QtCore.QSize(487, 120))
        newWorkspace_window.setMaximumSize(QtCore.QSize(487, 120))
        self.NewProjectWindowLayout = QtWidgets.QGridLayout(newWorkspace_window)
        self.NewProjectWindowLayout.setObjectName("NewProjectWindowLayout")
        self.newWorkspaceLayout = QtWidgets.QVBoxLayout()
        self.newWorkspaceLayout.setObjectName("newWorkspaceLayout")
        self.newWorkspaceNameLayout_newWorkspaceWindow = QtWidgets.QHBoxLayout()
        self.newWorkspaceNameLayout_newWorkspaceWindow.setObjectName("newWorkspaceNameLayout_newWorkspaceWindow")
        self.workspaceNameLabel_newWorkspaceWindow = QtWidgets.QLabel(newWorkspace_window)
        self.workspaceNameLabel_newWorkspaceWindow.setObjectName("workspaceNameLabel_newWorkspaceWindow")
        self.newWorkspaceNameLayout_newWorkspaceWindow.addWidget(self.workspaceNameLabel_newWorkspaceWindow)
        self.workspaceNameInput_newWorkspaceWindow = QtWidgets.QLineEdit(newWorkspace_window)
        self.workspaceNameInput_newWorkspaceWindow.setObjectName("workspaceNameInput_newWorkspaceWindow")
        self.newWorkspaceNameLayout_newWorkspaceWindow.addWidget(self.workspaceNameInput_newWorkspaceWindow)
        self.newWorkspaceLayout.addLayout(self.newWorkspaceNameLayout_newWorkspaceWindow)
        self.newWorkspaceButtonsLayout_newWorkspaceWindow = QtWidgets.QHBoxLayout()
        self.newWorkspaceButtonsLayout_newWorkspaceWindow.setObjectName("newWorkspaceButtonsLayout_newWorkspaceWindow")
        self.createWorkspaceButton_newWorkspaceWindow = QtWidgets.QPushButton(newWorkspace_window)
        self.createWorkspaceButton_newWorkspaceWindow.setObjectName("createWorkspaceButton_newWorkspaceWindow")
        self.newWorkspaceButtonsLayout_newWorkspaceWindow.addWidget(self.createWorkspaceButton_newWorkspaceWindow)
        self.cancelWorkspaceButton_newWorkspaceWindow = QtWidgets.QPushButton(newWorkspace_window)
        self.cancelWorkspaceButton_newWorkspaceWindow.setObjectName("cancelWorkspaceButton_newWorkspaceWindow")
        self.newWorkspaceButtonsLayout_newWorkspaceWindow.addWidget(self.cancelWorkspaceButton_newWorkspaceWindow)
        self.newWorkspaceLayout.addLayout(self.newWorkspaceButtonsLayout_newWorkspaceWindow)
        self.NewProjectWindowLayout.addLayout(self.newWorkspaceLayout, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(newWorkspace_window)

        _translate = QtCore.QCoreApplication.translate
        newWorkspace_window.setWindowTitle(_translate("newWorkspace_window", "New Workspace"))
        self.workspaceNameLabel_newWorkspaceWindow.setText(_translate("newWorkspace_window", "Workspace Name:     "))
        self.createWorkspaceButton_newWorkspaceWindow.setText(_translate("newWorkspace_window", "Create"))
        self.cancelWorkspaceButton_newWorkspaceWindow.setText(_translate("newWorkspace_window", "Cancel"))
