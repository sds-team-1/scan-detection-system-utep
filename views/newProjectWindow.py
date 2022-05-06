from Models.modelClasses import Project
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_newProject_window(object):
    def setupNewProjectWindowUi(self, parent_window:QtWidgets.QDialog, capture_manager_window, create_project_function):
        '''
        parent_window: the parent window that this window will be added to
        capture_manager_window: the capture manager window that this window will be added to
        create_project_function: the function that will be called when the user clicks the create project button
        '''
        # Set up parent window properties
        parent_window.setObjectName("newProject_window")
        parent_window.setEnabled(True)
        parent_window.resize(487, 135)
        parent_window.setMinimumSize(QtCore.QSize(487, 135))
        parent_window.setMaximumSize(QtCore.QSize(487, 135))
        parent_window.setWindowTitle("New Project")


        # Label that says Project Name:
        self.q_label_new_project_label = QtWidgets.QLabel(parent_window)
        self.q_label_new_project_label.setObjectName("newProjectNameLabel_newProjectWindow")
        self.q_label_new_project_label.setText("Project Name:")

        # Line edit input for the project name
        self.q_line_edit_project_name_input = QtWidgets.QLineEdit(parent_window)
        self.q_line_edit_project_name_input.setObjectName("newProjectNameInput_newProjectWindow")


        # Set up a row for the project name label and the line edit input
        self.q_label_project_name_label = QtWidgets.QHBoxLayout()
        self.q_label_project_name_label.setObjectName("newProjectNameLayout_newProjectWindow")
        self.q_label_project_name_label.addWidget(self.q_label_new_project_label)
        self.q_label_project_name_label.addWidget(self.q_line_edit_project_name_input)


        # Label that says Max Units:
        self.q_label_max_units_label = QtWidgets.QLabel(parent_window)
        self.q_label_max_units_label.setObjectName("newProjectMaxLabel_newProjectWindow")
        self.q_label_max_units_label.setText("Maximum Scenario Units in Paralell:")

        # Spinbox for the maximum units
        self.q_spin_box_max_units_value = QtWidgets.QSpinBox(parent_window)
        self.q_spin_box_max_units_value.setObjectName("newProjectMaxUnitsSpinbox_newProjectWindow")
        self.q_spin_box_max_units_value.setValue(1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        # Set up a row for the max units label and the spinbox
        self.q_row_max_units_label_and_input = QtWidgets.QHBoxLayout()
        self.q_row_max_units_label_and_input.setObjectName("newProjectMaxUnitsLayout_newProjectWindow")
        self.q_row_max_units_label_and_input.addWidget(self.q_label_max_units_label)
        self.q_row_max_units_label_and_input.addWidget(self.q_spin_box_max_units_value)
        self.q_row_max_units_label_and_input.addItem(spacerItem)

        # Button for create project
        self.q_button_create_project = QtWidgets.QPushButton(parent_window)
        self.q_button_create_project.setObjectName("newProjectCreateButton_newProjectWindow")
        self.q_button_create_project.setText("Create Project")

        # Button for cancel
        self.q_button_cancel_button = QtWidgets.QPushButton(parent_window)
        self.q_button_cancel_button.setObjectName("newProjectCancelButton_newProjectWindow")
        self.q_button_cancel_button.setText("Cancel")

        # Set up a row and add the buttons to it
        self.q_row_buttons_create_cancel = QtWidgets.QHBoxLayout()
        self.q_row_buttons_create_cancel.setObjectName("newProjectButtonsLayout_newProjectWindow")
        self.q_row_buttons_create_cancel.addWidget(self.q_button_create_project)
        self.q_row_buttons_create_cancel.addWidget(self.q_button_cancel_button)

        # set up a column and add the rows to it
        self.q_col_with_rows = QtWidgets.QVBoxLayout()
        self.q_col_with_rows.setObjectName("mainLayout_newProjectWindow")
        self.q_col_with_rows.addLayout(self.q_label_project_name_label)
        self.q_col_with_rows.addLayout(self.q_row_max_units_label_and_input)
        self.q_col_with_rows.addLayout(self.q_row_buttons_create_cancel)


        # Set up a main layout and add the column to it
        self.q_grid_main_layout = QtWidgets.QGridLayout(parent_window)
        self.q_grid_main_layout.setObjectName("NewProjectWindowLayout")
        self.q_grid_main_layout.addLayout(self.q_col_with_rows, 0, 0, 1, 1)


        # Connect the buttons to the functions
        self.q_button_create_project.clicked.connect(
            lambda: self.createProject(capture_manager_window, parent_window, create_project_function))

        self.q_button_cancel_button.clicked.connect(parent_window.close)

    def createProject(self, capture_manager_window, new_project_window, create_project_function):
        project_name = self.q_line_edit_project_name_input.text()
        project_parallel = self.q_spin_box_max_units_value.value()

        # Check for empty project name or project parallel is less than one
        if project_name == "" or project_parallel < 1:
            QMessageBox.about(new_project_window, "Error", "Project name and parallel must be filled in and greater than 0")
            return

        # Check if there is a project with the same name
        for project in capture_manager_window.workspace_object.projects:
            if project.name ==  project_name:
                msg = QMessageBox()
                msg.setWindowTitle("Project Name Already Exists")
                msg.setText('The Project name is already defined under this workspace.')
                x = msg.exec_()
                return

        # Call the create project function and close the window
        newProject = Project(project_name,project_parallel,[])
        create_project_function(newProject)
        new_project_window.destroy()

