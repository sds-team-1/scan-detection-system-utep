from PyQt5 import QtCore, QtWidgets
from Models.modelClasses import Project
from PyQt5.QtWidgets import QMessageBox


class Ui_newProject_window(object):
    def setupNewProject(self, newProject_window, projectsList_captureManagerWindow):
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
        newProject_window.setWindowTitle(_translate("newProject_window", "New Project"))
        self.newProjectNameLabel_newProjectWindow.setText(_translate("newProject_window", "Project Name:     "))
        self.newProjectMaxLabel_newProjectWindow.setText(_translate("newProject_window", "Maximum Scenario Units in "
                                                                                         "Parallel:"))
        self.newProjectCreateButton_newProjectWindow.setText(_translate("newProject_window", "Create"))
        self.newProjectCancelButton_newProjectWindow.setText(_translate("newProject_window", "Cancel"))

        self.newProjectCreateButton_newProjectWindow.clicked.connect(
            lambda: self.createProject(projectsList_captureManagerWindow, newProject_window))
        self.newProjectCancelButton_newProjectWindow.clicked.connect(newProject_window.close)

    def createProject(self, captureManagerWindow, newProject_window):
        project_name = self.newProjectNameInput_newProjectWindow.text()
        project_parallel = self.newProjectMaxUnitsSpinbox_newProjectWindow.value()
        dup =  False
        for project in captureManagerWindow.workspace_object.projects:
            if project.name ==  project_name:
                dup = True
                msg = QMessageBox()
                msg.setWindowTitle("Project Name Already Exists")
                msg.setText('The Project name is already defined in the database.')
                x = msg.exec_()
        if dup == False:
            newProject = Project(project_name,project_parallel,[])
            captureManagerWindow.workspace_object.projects.append(newProject)
            captureManagerWindow.generate_projects()
            newProject_window.close()
        # If the input is incorrect show the missing fields window
        # if not project_name or project_parallel == 0:
        #     missingFields_Window = QtWidgets.QDialog()
        #     missingFieldsWindowUI = Ui_missingFields_window()
        #     missingFieldsWindowUI.setupMissingFields(missingFields_Window)
        #     missingFields_Window.show()
        # # Otherwise save the project
        # else:
        #     # TODO: INSERT PROJECT TO THE DATABASE AND CREATE THE PROJECT OBJECT AND INSERT IT TO THE WORKSPACE OBJECT
        #     p = QtWidgets.QTreeWidgetItem([project_name])
        #     # Adds the TreeWidgetItem to the project list
        #     captureManagerWindow.addTopLevelItem(p)
        #     # Resets the values for the window
        #     self.newProjectMaxUnitsSpinbox_newProjectWindow.setValue(0)
        #     self.newProjectNameInput_newProjectWindow.clear()

