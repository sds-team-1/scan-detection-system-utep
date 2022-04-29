from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem

from views.missingFieldsWindow import Ui_missingFields_window


class Ui_newScenarioUnit_window(object):
    def setupNewScenarioUnit(self, newScenarioUnit_window,
                             projectsList_captureManagerWindow, scenarioIterationsSpinbox_captureManagerWindow):
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
        newScenarioUnit_window.setWindowTitle(_translate("newScenarioUnit_window", "New Scenario Unit"))
        self.newScenarioUnitNameLabel_newScenarioUnitWindow.setText(_translate("newScenarioUnit_window", "Scenario Unit Name"))
        self.newScenarioUnitCreateButton_newScenarioUnitWindow.setText(_translate("newScenarioUnit_window", "Create"))
        self.newScenarioUnitCancelButton_newScenarioUnitWindow.setText(_translate("newScenarioUnit_window", "Cancel"))

        self.newScenarioUnitCreateButton_newScenarioUnitWindow.clicked.connect(
            lambda: self.createScenario(newScenarioUnit_window, projectsList_captureManagerWindow,
                                                     scenarioIterationsSpinbox_captureManagerWindow))
        self.newScenarioUnitCancelButton_newScenarioUnitWindow.clicked.connect(
            newScenarioUnit_window.close)

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
            # TODO: This causes an error when creating a scenario.
            project_name = projectsList_captureManagerWindow.selectedItems()[0].text(0)
            # TODO: INSERT ITERATIONS HERE
            su_iterations = scenarioIterationsSpinbox_captureManagerWindow.value()

                # TODO: Test this
            s = QTreeWidgetItem([scenario_name])
            p = projectsList_captureManagerWindow.selectedItems()[0]
            p.addChild(s)
            projectsList_captureManagerWindow.expandAll()
            newScenarioUnit_Window.close()
