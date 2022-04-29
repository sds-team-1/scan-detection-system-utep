from typing import List
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem

from views.missingFieldsWindow import Ui_missingFields_window


class Ui_newScenarioUnit_window(object):
    def setupNewScenarioUnit(self, newScenarioUnit_window, sds_controller,
                             projectsList_captureManagerWindow, scenarioIterationsSpinbox_captureManagerWindow, 
                             scenario_to_edit=None):
        self.sds_controller = sds_controller
        newScenarioUnit_window.setObjectName("newScenarioUnit_window")
        newScenarioUnit_window.setEnabled(True)
        newScenarioUnit_window.resize(513, 115)
        newScenarioUnit_window.setMinimumSize(QtCore.QSize(513, 115))
        newScenarioUnit_window.setMaximumSize(QtCore.QSize(513, 115))
        self.NewScenarioUnitWindowLayout = QtWidgets.QGridLayout(newScenarioUnit_window)
        self.NewScenarioUnitWindowLayout.setObjectName("NewScenarioUnitWindowLayout")
        self.mainLayout_newScenarioUnitWindow = QtWidgets.QVBoxLayout()
        self.mainLayout_newScenarioUnitWindow.setObjectName("mainLayout_newScenarioUnitWindow")
        self.newScenarioUnitNameLayout_newScenarioUnitWindow = QtWidgets.QHBoxLayout()
        self.newScenarioUnitNameLayout_newScenarioUnitWindow.setObjectName("newScenarioUnitNameLayout_newScenarioUnitWindow")
        self.newScenarioUnitNameLabel_newScenarioUnitWindow = QtWidgets.QLabel(newScenarioUnit_window)
        self.newScenarioUnitNameLabel_newScenarioUnitWindow.setObjectName("newScenarioUnitNameLabel_newScenarioUnitWindow")
        self.newScenarioUnitNameLayout_newScenarioUnitWindow.addWidget(self.newScenarioUnitNameLabel_newScenarioUnitWindow)
        self.newScenarioUnitNameInput_newScenarioUnitWindow = QtWidgets.QLineEdit(newScenarioUnit_window)
        self.newScenarioUnitNameInput_newScenarioUnitWindow.setObjectName("newScenarioUnitNameInput_newScenarioUnitWindow")
        self.newScenarioUnitNameLayout_newScenarioUnitWindow.addWidget(self.newScenarioUnitNameInput_newScenarioUnitWindow)
        self.mainLayout_newScenarioUnitWindow.addLayout(self.newScenarioUnitNameLayout_newScenarioUnitWindow)

        self.newScenarioUnitButtonsLayout_newScenarioUnitWindow = QtWidgets.QHBoxLayout()
        self.newScenarioUnitButtonsLayout_newScenarioUnitWindow.setObjectName("newScenarioUnitButtonsLayout_newScenarioUnitWindow")
        self.newScenarioUnitCreateButton_newScenarioUnitWindow = QtWidgets.QPushButton(newScenarioUnit_window)
        self.newScenarioUnitCreateButton_newScenarioUnitWindow.setObjectName("newScenarioUnitCreateButton_newScenarioUnitWindow")
        self.newScenarioUnitButtonsLayout_newScenarioUnitWindow.addWidget(self.newScenarioUnitCreateButton_newScenarioUnitWindow)
        self.newScenarioUnitCancelButton_newScenarioUnitWindow = QtWidgets.QPushButton(newScenarioUnit_window)
        self.newScenarioUnitCancelButton_newScenarioUnitWindow.setObjectName("newScenarioUnitCancelButton_newScenarioUnitWindow")
        self.newScenarioUnitButtonsLayout_newScenarioUnitWindow.addWidget(self.newScenarioUnitCancelButton_newScenarioUnitWindow)
        self.mainLayout_newScenarioUnitWindow.addLayout(self.newScenarioUnitButtonsLayout_newScenarioUnitWindow)
        self.NewScenarioUnitWindowLayout.addLayout(self.mainLayout_newScenarioUnitWindow, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(newScenarioUnit_window)

        _translate = QtCore.QCoreApplication.translate
        if not scenario_to_edit:
            newScenarioUnit_window.setWindowTitle(_translate("newScenarioUnit_window", "New Scenario Unit"))
            self.newScenarioUnitNameLabel_newScenarioUnitWindow.setText(_translate("newScenarioUnit_window", "Scenario Unit Name"))
            self.newScenarioUnitCreateButton_newScenarioUnitWindow.setText(_translate("newScenarioUnit_window", "Create"))
            self.newScenarioUnitCancelButton_newScenarioUnitWindow.setText(_translate("newScenarioUnit_window", "Cancel"))

            self.newScenarioUnitCreateButton_newScenarioUnitWindow.clicked.connect(
                lambda: self.createScenario(newScenarioUnit_window, projectsList_captureManagerWindow,
                                                        scenarioIterationsSpinbox_captureManagerWindow))
            self.newScenarioUnitCancelButton_newScenarioUnitWindow.clicked.connect(
                newScenarioUnit_window.close)
        else: 
            newScenarioUnit_window.setWindowTitle(_translate('newScenarioUnit_window', 'Edit Scenario Unit'))
            self.newScenarioUnitNameLabel_newScenarioUnitWindow.setText(_translate('newScenarioUnit_window', 'Scenario Unit Name'))
            self.newScenarioUnitCreateButton_newScenarioUnitWindow.setText(_translate('newScenarioUnit_window', 'Save'))
            self.newScenarioUnitCancelButton_newScenarioUnitWindow.setText(_translate('newScenarioUnit_window', 'Cancel'))
            self.newScenarioUnitNameInput_newScenarioUnitWindow.setText(scenario_to_edit)
            
            self.newScenarioUnitCreateButton_newScenarioUnitWindow.clicked.connect(
                lambda: self.edit_scenario(newScenarioUnit_window, projectsList_captureManagerWindow,
                    scenario_to_edit)
            )
            self.newScenarioUnitCancelButton_newScenarioUnitWindow.clicked.connect(newScenarioUnit_window.close)
        
    def edit_scenario(self, editScenarioUnit_Window, projectsList_captureManagerWindow,
        old_scenario_name):
        '''Edits the scenario unit'''
        new_scenario_name = self.newScenarioUnitNameInput_newScenarioUnitWindow.text()
        scenario_id = self.sds_controller.get_scenario_id(old_scenario_name)
        success = self.sds_controller.edit_scenario_unit(scenario_id, new_scenario_name)
        if success:
            editScenarioUnit_Window.close()
            '''items: List[QtWidgets.QTreeWidgetItem] = projectsList_captureManagerWindow.findItems(old_scenario_name, QtCore.Qt.MatchFlag.MatchExactly, column=1)
            print(items)
            items[0].setText(0, new_scenario_name)'''

    def createScenario(
            self, newScenarioUnit_Window, projectsList_captureManagerWindow,
            scenarioIterationsSpinbox_captureManagerWindow):
        scenario_name = self.newScenarioUnitNameInput_newScenarioUnitWindow.text()
        if not scenario_name:
            missingFields_Window = QtWidgets.QDialog()
            missingFieldsWindowUI = Ui_missingFields_window()
            missingFieldsWindowUI.setupMissingFields(missingFields_Window)
            missingFields_Window.show()
        else:
            self.sds_controller._enforce_state('init_project')
            self.sds_controller.add_scenario_unit()
            self.sds_controller.insert_scenario_name(scenario_name)
            # TODO: This causes an error when creating a scenario.
            project_name = projectsList_captureManagerWindow.selectedItems()[0].text(0)
            # TODO: INSERT ITERATIONS HERE
            su_iterations = scenarioIterationsSpinbox_captureManagerWindow.value()
            success = self.sds_controller.finish_scenario_unit_construction(project_name, su_iterations)
            if not success:
                # TODO: Display error
                pass
            else:
                # TODO: Test this
                s = QTreeWidgetItem([scenario_name])
                p = projectsList_captureManagerWindow.selectedItems()[0]
                p.addChild(s)
                projectsList_captureManagerWindow.expandAll()
                newScenarioUnit_Window.close()
