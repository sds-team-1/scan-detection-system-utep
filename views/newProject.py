from typing import List
from PyQt5 import QtCore, QtWidgets

from views.missingFieldsWindow import Ui_missingFields_window


class Ui_newProject_window(object):
    def setupNewProject(self, newProject_window, sds_controller, projectsList_captureManagerWindow, workspace_window, project_to_edit = None):
        self.sds_controller = sds_controller
        self.workspace_window = workspace_window
        newProject_window.setObjectName("newProject_window")
        newProject_window.setEnabled(True)
        newProject_window.resize(487, 135)
        newProject_window.setMinimumSize(QtCore.QSize(487, 135))
        newProject_window.setMaximumSize(QtCore.QSize(487, 135))
        self.NewProjectWindowLayout = QtWidgets.QGridLayout(newProject_window)
        self.NewProjectWindowLayout.setObjectName("NewProjectWindowLayout")
        self.mainLayout_newProjectWindow = QtWidgets.QVBoxLayout()
        self.mainLayout_newProjectWindow.setObjectName("mainLayout_newProjectWindow")
        self.newProjectNameLayout_newProjectWindow = QtWidgets.QHBoxLayout()
        self.newProjectNameLayout_newProjectWindow.setObjectName("newProjectNameLayout_newProjectWindow")
        self.newProjectNameLabel_newProjectWindow = QtWidgets.QLabel(newProject_window)
        self.newProjectNameLabel_newProjectWindow.setObjectName("newProjectNameLabel_newProjectWindow")
        self.newProjectNameLayout_newProjectWindow.addWidget(self.newProjectNameLabel_newProjectWindow)
        self.newProjectNameInput_newProjectWindow = QtWidgets.QLineEdit(newProject_window)
        self.newProjectNameInput_newProjectWindow.setObjectName("newProjectNameInput_newProjectWindow")
        self.newProjectNameLayout_newProjectWindow.addWidget(self.newProjectNameInput_newProjectWindow)
        self.mainLayout_newProjectWindow.addLayout(self.newProjectNameLayout_newProjectWindow)
        self.newProjectMaxUnitsLayout_newProjectWindow = QtWidgets.QHBoxLayout()
        self.newProjectMaxUnitsLayout_newProjectWindow.setObjectName("newProjectMaxUnitsLayout_newProjectWindow")
        self.newProjectMaxLabel_newProjectWindow = QtWidgets.QLabel(newProject_window)
        self.newProjectMaxLabel_newProjectWindow.setObjectName("newProjectMaxLabel_newProjectWindow")
        self.newProjectMaxUnitsLayout_newProjectWindow.addWidget(self.newProjectMaxLabel_newProjectWindow)
        self.newProjectMaxUnitsSpinbox_newProjectWindow = QtWidgets.QSpinBox(newProject_window)
        self.newProjectMaxUnitsSpinbox_newProjectWindow.setObjectName("newProjectMaxUnitsSpinbox_newProjectWindow")
        self.newProjectMaxUnitsSpinbox_newProjectWindow.setValue(1)
        self.newProjectMaxUnitsLayout_newProjectWindow.addWidget(self.newProjectMaxUnitsSpinbox_newProjectWindow)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.newProjectMaxUnitsLayout_newProjectWindow.addItem(spacerItem)
        self.mainLayout_newProjectWindow.addLayout(self.newProjectMaxUnitsLayout_newProjectWindow)
        self.newProjectButtonsLayout_newProjectWindow = QtWidgets.QHBoxLayout()
        self.newProjectButtonsLayout_newProjectWindow.setObjectName("newProjectButtonsLayout_newProjectWindow")
        self.newProjectCreateButton_newProjectWindow = QtWidgets.QPushButton(newProject_window)
        self.newProjectCreateButton_newProjectWindow.setObjectName("newProjectCreateButton_newProjectWindow")
        self.newProjectButtonsLayout_newProjectWindow.addWidget(self.newProjectCreateButton_newProjectWindow)
        self.newProjectCancelButton_newProjectWindow = QtWidgets.QPushButton(newProject_window)
        self.newProjectCancelButton_newProjectWindow.setObjectName("newProjectCancelButton_newProjectWindow")
        self.newProjectButtonsLayout_newProjectWindow.addWidget(self.newProjectCancelButton_newProjectWindow)
        self.mainLayout_newProjectWindow.addLayout(self.newProjectButtonsLayout_newProjectWindow)
        self.NewProjectWindowLayout.addLayout(self.mainLayout_newProjectWindow, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(newProject_window)
        _translate = QtCore.QCoreApplication.translate

        if not project_to_edit:
            newProject_window.setWindowTitle(_translate("newProject_window", "New Project"))
            self.newProjectNameLabel_newProjectWindow.setText(_translate("newProject_window", "Project Name:     "))
            self.newProjectMaxLabel_newProjectWindow.setText(_translate("newProject_window", "Maximum Scenario Units in "
                                                                                            "Parallel:"))
            self.newProjectCreateButton_newProjectWindow.setText(_translate("newProject_window", "Create"))
            self.newProjectCancelButton_newProjectWindow.setText(_translate("newProject_window", "Cancel"))

            self.newProjectCreateButton_newProjectWindow.clicked.connect(
                lambda: self.createProject(projectsList_captureManagerWindow, newProject_window))
            self.newProjectCancelButton_newProjectWindow.clicked.connect(newProject_window.close)
        else:
            newProject_window.setWindowTitle(_translate('newProject_window', 'Edit Project'))
            self.newProjectNameLabel_newProjectWindow.setText(_translate('newProject_window', 'Project Name:      '))
            self.newProjectMaxLabel_newProjectWindow.setText(_translate('newProject_window', 'Maximum Scenario Units in Parallel:'))
            self.newProjectCreateButton_newProjectWindow.setText(_translate('newProject_window', 'Save'))
            self.newProjectCancelButton_newProjectWindow.setText(_translate('newProject_window', 'Cancel'))
            self.newProjectNameInput_newProjectWindow.setText(project_to_edit)
            self.newProjectCreateButton_newProjectWindow.clicked.connect(lambda: self.edit_project(projectsList_captureManagerWindow, newProject_window, project_to_edit))
            self.newProjectCancelButton_newProjectWindow.clicked.connect(newProject_window.close)

    def edit_project(self, projectsList_captureManagerWindow, editProject_window, old_project_name):
        '''Edits project'''
        new_project_name = self.newProjectNameInput_newProjectWindow.text()
        new_parallel = self.newProjectMaxUnitsSpinbox_newProjectWindow.value()
        if not new_project_name or new_parallel == 0:
            missingFields_window = Ui_missingFields_window()
            missingFieldsWindowUI = Ui_missingFields_window()
            missingFieldsWindowUI.setupMissingFields(missingFields_window)
            missingFields_window.show()
        else:
            success = self.sds_controller.edit_project(old_project_name, new_project_name, new_parallel)

            if not success:
                pass
            else: 
                self.newProjectMaxUnitsSpinbox_newProjectWindow.setValue(1)
                self.newProjectNameInput_newProjectWindow.clear()
                editProject_window.close()
                # Populate the tree or make it refresh
                items: List[QtWidgets.QTreeWidgetItem] = projectsList_captureManagerWindow.findItems(old_project_name, QtCore.Qt.MatchFlag.MatchExactly)
                items[0].setText(0, new_project_name)

    def createProject(self, projectsList_captureManagerWindow, newProject_window):
        project_name = self.newProjectNameInput_newProjectWindow.text()
        project_parallel = self.newProjectMaxUnitsSpinbox_newProjectWindow.value()

        # If the input is incorrect show the missing fields window
        if not project_name or project_parallel == 0:
            missingFields_Window = QtWidgets.QDialog()
            missingFieldsWindowUI = Ui_missingFields_window()
            missingFieldsWindowUI.setupMissingFields(missingFields_Window)
            missingFields_Window.show()
        # Otherwise save the project
        else:
            p = QtWidgets.QTreeWidgetItem([project_name])
            # Use the sds controller to save the project
            self.sds_controller._enforce_state('workplace_construction')
            self.sds_controller._enforce_state('project_construction')
            self.sds_controller.specify_project_name(project_name)
            self.sds_controller.specify_num_parrallel_units(project_parallel)
            success = self.sds_controller.finish_project_construction()

            if not success:
                # TODO: Add a warning message
                pass
            else:
                # Adds the TreeWidgetItem to the project list
                projectsList_captureManagerWindow.addTopLevelItem(p)
                # Resets the values for the window
                self.newProjectMaxUnitsSpinbox_newProjectWindow.setValue(1)
                self.newProjectNameInput_newProjectWindow.clear()
                newProject_window.close()
