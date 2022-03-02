# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewProjectUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewProjectWindow(object):
    def setupUi(self, NewProjectWindow):
        NewProjectWindow.setObjectName("NewProjectWindow")
        NewProjectWindow.setEnabled(True)
        NewProjectWindow.resize(487, 299)
        NewProjectWindow.setMinimumSize(QtCore.QSize(487, 299))
        NewProjectWindow.setMaximumSize(QtCore.QSize(487, 299))
        self.NewProjectWindowLayout = QtWidgets.QGridLayout(NewProjectWindow)
        self.NewProjectWindowLayout.setObjectName("NewProjectWindowLayout")
        self.NewProjectLayout = QtWidgets.QVBoxLayout()
        self.NewProjectLayout.setObjectName("NewProjectLayout")
        self.NewProjectNameLayout = QtWidgets.QHBoxLayout()
        self.NewProjectNameLayout.setObjectName("NewProjectNameLayout")
        self.NewProjectNameLabel = QtWidgets.QLabel(NewProjectWindow)
        self.NewProjectNameLabel.setObjectName("NewProjectNameLabel")
        self.NewProjectNameLayout.addWidget(self.NewProjectNameLabel)
        self.NewProjectNameInput = QtWidgets.QLineEdit(NewProjectWindow)
        self.NewProjectNameInput.setObjectName("NewProjectNameInput")
        self.NewProjectNameLayout.addWidget(self.NewProjectNameInput)
        self.NewProjectLayout.addLayout(self.NewProjectNameLayout)
        self.NewProjectLocationLayout = QtWidgets.QHBoxLayout()
        self.NewProjectLocationLayout.setObjectName("NewProjectLocationLayout")
        self.NewProjectLocationLabel = QtWidgets.QLabel(NewProjectWindow)
        self.NewProjectLocationLabel.setObjectName("NewProjectLocationLabel")
        self.NewProjectLocationLayout.addWidget(self.NewProjectLocationLabel)
        self.NewProjectLocationInput = QtWidgets.QLineEdit(NewProjectWindow)
        self.NewProjectLocationInput.setObjectName("NewProjectLocationInput")
        self.NewProjectLocationLayout.addWidget(self.NewProjectLocationInput)
        self.NewProjectLocationBrowse = QtWidgets.QPushButton(NewProjectWindow)
        self.NewProjectLocationBrowse.setObjectName("NewProjectLocationBrowse")
        self.NewProjectLocationLayout.addWidget(self.NewProjectLocationBrowse)
        self.NewProjectLayout.addLayout(self.NewProjectLocationLayout)
        self.NewProjectScenariosLayout = QtWidgets.QHBoxLayout()
        self.NewProjectScenariosLayout.setObjectName("NewProjectScenariosLayout")
        self.NewProjectScenariosLabel = QtWidgets.QLabel(NewProjectWindow)
        self.NewProjectScenariosLabel.setObjectName("NewProjectScenariosLabel")
        self.NewProjectScenariosLayout.addWidget(self.NewProjectScenariosLabel)
        self.NewProjectScenariosDropdown = QtWidgets.QComboBox(NewProjectWindow)
        self.NewProjectScenariosDropdown.setObjectName("NewProjectScenariosDropdown")
        self.NewProjectScenariosLayout.addWidget(self.NewProjectScenariosDropdown)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.NewProjectScenariosLayout.addItem(spacerItem)
        self.NewProjectLayout.addLayout(self.NewProjectScenariosLayout)
        self.NewProjectButtonsLayout = QtWidgets.QHBoxLayout()
        self.NewProjectButtonsLayout.setObjectName("NewProjectButtonsLayout")
        self.NewProjectCreateButton = QtWidgets.QPushButton(NewProjectWindow)
        self.NewProjectCreateButton.setObjectName("NewProjectCreateButton")
        self.NewProjectButtonsLayout.addWidget(self.NewProjectCreateButton)
        self.NewProjectCancelButton = QtWidgets.QPushButton(NewProjectWindow)
        self.NewProjectCancelButton.setObjectName("NewProjectCancelButton")
        self.NewProjectButtonsLayout.addWidget(self.NewProjectCancelButton)
        self.NewProjectLayout.addLayout(self.NewProjectButtonsLayout)
        self.NewProjectWindowLayout.addLayout(self.NewProjectLayout, 0, 0, 1, 1)

        self.retranslateUi(NewProjectWindow)
        QtCore.QMetaObject.connectSlotsByName(NewProjectWindow)

    def retranslateUi(self, NewProjectWindow):
        _translate = QtCore.QCoreApplication.translate
        NewProjectWindow.setWindowTitle(_translate("NewProjectWindow", "New Project"))
        self.NewProjectNameLabel.setText(_translate("NewProjectWindow", "Project Name:     "))
        self.NewProjectLocationLabel.setText(_translate("NewProjectWindow", "Project Location:"))
        self.NewProjectLocationBrowse.setText(_translate("NewProjectWindow", "Browse..."))
        self.NewProjectScenariosLabel.setText(_translate("NewProjectWindow", "Maximum Scenario Units:"))
        self.NewProjectCreateButton.setText(_translate("NewProjectWindow", "Create"))
        self.NewProjectCancelButton.setText(_translate("NewProjectWindow", "Cancel"))
