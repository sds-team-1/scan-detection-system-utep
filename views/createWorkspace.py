import time

from PyQt5 import QtCore, QtWidgets

from Database.databaseFunctions import generate_workspaces_list_window
from views.captureManagerWindow import Ui_CaptureManagerWindow
from views.missingFieldsWindow import Ui_missingFields_window

from Database.databaseFunctions import generate_workspaces_list_window


class Ui_newWorkspace_window(object):
    def setupCreateWorkspace(self, newWorkspace_window, workspace_Window, sds_controller, workspace_list = None, input_to_edit = None):
        self.sds_controller = sds_controller
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
        # Switch between editing and creating.
        if not input_to_edit:
            newWorkspace_window.setWindowTitle(_translate("newWorkspace_window", "New Workspace"))
            self.workspaceNameLabel_newWorkspaceWindow.setText(_translate("newWorkspace_window", "Workspace Name:     "))
            self.createWorkspaceButton_newWorkspaceWindow.setText(_translate("newWorkspace_window", "Create"))
            self.cancelWorkspaceButton_newWorkspaceWindow.setText(_translate("newWorkspace_window", "Cancel"))
            self.createWorkspaceButton_newWorkspaceWindow.clicked.connect(lambda: self.createWorkspace(newWorkspace_window, workspace_Window))
            self.cancelWorkspaceButton_newWorkspaceWindow.clicked.connect(newWorkspace_window.close)
        else:
            newWorkspace_window.setWindowTitle(_translate('newWorkspace_window', 'Edit Workspace'))
            self.workspaceNameLabel_newWorkspaceWindow.setText(_translate('newWorkspace_window', 'Workspace Name:     '))
            self.createWorkspaceButton_newWorkspaceWindow.setText(_translate('newWorkspace_window', 'Save'))
            self.cancelWorkspaceButton_newWorkspaceWindow.setText(_translate('newWorkspace_window', 'Cancel'))
            self.workspaceNameInput_newWorkspaceWindow.setText(input_to_edit)
            self.createWorkspaceButton_newWorkspaceWindow.clicked.connect(lambda: self.editWorkspace(newWorkspace_window, workspace_list, workspace_Window, input_to_edit))
            self.cancelWorkspaceButton_newWorkspaceWindow.clicked.connect(newWorkspace_window.close)
            
    def editWorkspace(self, editWorkspace_window, workspaceList, workspace_window, workspace_edit_name):
        ''' Starts and populates the workspace window'''
        # Get new workspace name 
        new_ws_name = self.workspaceNameInput_newWorkspaceWindow.text()
        # Check if its valid
        if not new_ws_name:
            missingFields_window = QtWidgets.QDialog()
            missingFieldsWindowUI = Ui_missingFields_window()
            missingFieldsWindowUI.setupMissingFields(missingFields_window)
            missingFields_window.show()
        else:
            success = self.sds_controller.edit_workspace_name(workspace_edit_name, new_ws_name)
            if not success:
                pass
            else:
                editWorkspace_window.close()
                generate_workspaces_list_window(workspaceList, self.sds_controller)

    def createWorkspace(self, createWorkspace_Window, workspace_Window):
        # Get workspace name
        ws_name = self.workspaceNameInput_newWorkspaceWindow.text()
        # Check if valid input
        if not ws_name:
            missingFields_Window = QtWidgets.QDialog()
            missingFieldsWindowUI = Ui_missingFields_window()
            missingFieldsWindowUI.setupMissingFields(missingFields_Window)
            missingFields_Window.show()
        else:
            # Insert into controller of new workspace.
            self.sds_controller.specify_workplace_name(ws_name)
            workspace_injection_success: bool = self.sds_controller.finish_workplace_construction()
            # TODO: Based on the success, insert another window if error
            if not workspace_injection_success:
                workspace_exists_error = QtWidgets.QDialog()
                pass
            else:
                time.sleep(1)
                captureManager_Window = QtWidgets.QMainWindow()
                captureManagerWindowUI = Ui_CaptureManagerWindow()
                captureManagerWindowUI.setupCaptureManager(captureManager_Window, self.sds_controller, workspace_Window)
                captureManager_Window.setWindowTitle(ws_name + ' - Scan Detection System')
                captureManager_Window.show()
                createWorkspace_Window.close()
                workspace_Window.close()
