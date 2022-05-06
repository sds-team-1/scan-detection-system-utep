from typing import List

from Models.modelClasses import Project
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTreeWidgetItem


class Ui_newScenarioUnit_window(object):
    def setupNewScenarioUnit(self, parent_window:QtWidgets.QDialog, selected_project:Project, create_new_scenario_function):

        # Set up parent window properties
        parent_window.setObjectName("newScenarioUnit_window")
        parent_window.setEnabled(True)
        parent_window.resize(513, 115)
        parent_window.setMinimumSize(QtCore.QSize(513, 115))
        parent_window.setMaximumSize(QtCore.QSize(513, 115))
        parent_window.setWindowTitle("New Scenario Unit")

        # Label that says "Scenario Name"
        self.q_label_new_scenario_label = QtWidgets.QLabel(parent_window)
        self.q_label_new_scenario_label.setObjectName("newScenarioUnitNameLabel_newScenarioUnitWindow")
        self.q_label_new_scenario_label.setText("Scenario Unit Name")

        # Input for scenario name
        self.q_line_input_scenario_name = QtWidgets.QLineEdit(parent_window)
        self.q_line_input_scenario_name.setObjectName("newScenarioUnitNameInput_newScenarioUnitWindow")

        # Row that holds the scenario name input and the label
        self.q_row_new_scenario_label_and_input_row = QtWidgets.QHBoxLayout()
        self.q_row_new_scenario_label_and_input_row.setObjectName("newScenarioUnitNameLayout_newScenarioUnitWindow")
        self.q_row_new_scenario_label_and_input_row.addWidget(self.q_label_new_scenario_label)
        self.q_row_new_scenario_label_and_input_row.addWidget(self.q_line_input_scenario_name)

        # Button for create scenario
        self.q_button_create_new_scenario = QtWidgets.QPushButton(parent_window)
        self.q_button_create_new_scenario.setObjectName("newScenarioUnitCreateButton_newScenarioUnitWindow")
        self.q_button_create_new_scenario.setText("Create Scenario")

        # Cancel button
        self.q_button_cancel_button = QtWidgets.QPushButton(parent_window)
        self.q_button_cancel_button.setObjectName("newScenarioUnitCancelButton_newScenarioUnitWindow")
        self.q_button_cancel_button.setText("Cancel")


        # Row that holds the create scenario button and the cancel button
        self.q_row_buttons_row = QtWidgets.QHBoxLayout()
        self.q_row_buttons_row.setObjectName("newScenarioUnitButtonsLayout_newScenarioUnitWindow")
        self.q_row_buttons_row.addWidget(self.q_button_create_new_scenario)
        self.q_row_buttons_row.addWidget(self.q_button_cancel_button)


        # Column that holds the rows created for input and buttons
        self.q_col_main_column = QtWidgets.QVBoxLayout()
        self.q_col_main_column.setObjectName("mainLayout_newScenarioUnitWindow")
        self.q_col_main_column.addLayout(self.q_row_new_scenario_label_and_input_row)
        self.q_col_main_column.addLayout(self.q_row_buttons_row)

        # Main layout
        self.q_grid_layout_main = QtWidgets.QGridLayout(parent_window)
        self.q_grid_layout_main.setObjectName("NewScenarioUnitWindowLayout")
        self.q_grid_layout_main.addLayout(self.q_col_main_column, 0, 0, 1, 1)

        # Connect event listeners
        self.q_button_create_new_scenario.clicked.connect(
            lambda: self.on_create_scenario_button_clicked(parent_window, selected_project, create_new_scenario_function)
        )

        self.q_button_cancel_button.clicked.connect(
            lambda: parent_window.destroy()
        )

    def on_create_scenario_button_clicked(
            self, 
            create_new_scenario_window:QtWidgets.QDialog, 
            selected_project:Project,
            create_new_scenario_function
        ):
        '''
        This function is called when the create scenario button is clicked.
        Gets the name of the scenario unit from the input and creates a new scenario unit.
        Checks that the scenario does not already exist in the project that it is being created under
        '''

        scenario_name = self.q_line_input_scenario_name.text()

        # Check if the scenario name already exists
        for scenario in selected_project.scenarios:
            if scenario.name == scenario_name:
                # If the scenario name already exists, show a message box
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("The scenario name already exists.")
                msg.setWindowTitle("Error")
                msg.exec_()
                return

        if scenario_name == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please enter a scenario name.")
            msg.setWindowTitle("Missing Fields")
            msg.exec_()
            return

        create_new_scenario_window.destroy()
        create_new_scenario_function(selected_project, scenario_name)



