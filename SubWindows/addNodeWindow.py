# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddNodeUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddNodeWindow(object):
    def setupUi(self, AddNodeWindow):
        AddNodeWindow.setObjectName("AddNodeWindow")
        AddNodeWindow.setEnabled(True)
        AddNodeWindow.resize(487, 299)
        AddNodeWindow.setMinimumSize(QtCore.QSize(487, 299))
        AddNodeWindow.setMaximumSize(QtCore.QSize(487, 299))
        self.NewProjectWindowLayout = QtWidgets.QGridLayout(AddNodeWindow)
        self.NewProjectWindowLayout.setObjectName("NewProjectWindowLayout")
        self.AddNodeLayout = QtWidgets.QVBoxLayout()
        self.AddNodeLayout.setObjectName("AddNodeLayout")
        self.TypeNode_AddNodeWindow = QtWidgets.QHBoxLayout()
        self.TypeNode_AddNodeWindow.setObjectName("TypeNode_AddNodeWindow")
        self.NewProjectNameLabel = QtWidgets.QLabel(AddNodeWindow)
        self.NewProjectNameLabel.setObjectName("NewProjectNameLabel")
        self.TypeNode_AddNodeWindow.addWidget(self.NewProjectNameLabel)
        self.comboBox = QtWidgets.QComboBox(AddNodeWindow)
        self.comboBox.setObjectName("comboBox")
        self.TypeNode_AddNodeWindow.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.TypeNode_AddNodeWindow.addItem(spacerItem)
        self.AddNodeLayout.addLayout(self.TypeNode_AddNodeWindow)
        self.NewProjectLocationLayout = QtWidgets.QHBoxLayout()
        self.NewProjectLocationLayout.setObjectName("NewProjectLocationLayout")
        self.NewProjectLocationLabel = QtWidgets.QLabel(AddNodeWindow)
        self.NewProjectLocationLabel.setObjectName("NewProjectLocationLabel")
        self.NewProjectLocationLayout.addWidget(self.NewProjectLocationLabel)
        self.NewProjectLocationInput = QtWidgets.QLineEdit(AddNodeWindow)
        self.NewProjectLocationInput.setObjectName("NewProjectLocationInput")
        self.NewProjectLocationLayout.addWidget(self.NewProjectLocationInput)
        self.AddNodeLayout.addLayout(self.NewProjectLocationLayout)
        self.NewProjectScenariosLayout = QtWidgets.QHBoxLayout()
        self.NewProjectScenariosLayout.setObjectName("NewProjectScenariosLayout")
        self.label = QtWidgets.QLabel(AddNodeWindow)
        self.label.setObjectName("label")
        self.NewProjectScenariosLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(AddNodeWindow)
        self.lineEdit.setObjectName("lineEdit")
        self.NewProjectScenariosLayout.addWidget(self.lineEdit)
        self.AddNodeLayout.addLayout(self.NewProjectScenariosLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(AddNodeWindow)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(AddNodeWindow)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.AddNodeLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.checkBox = QtWidgets.QCheckBox(AddNodeWindow)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.AddNodeLayout.addLayout(self.horizontalLayout_2)
        self.NewProjectButtonsLayout = QtWidgets.QHBoxLayout()
        self.NewProjectButtonsLayout.setObjectName("NewProjectButtonsLayout")
        self.NewProjectCreateButton = QtWidgets.QPushButton(AddNodeWindow)
        self.NewProjectCreateButton.setObjectName("NewProjectCreateButton")
        self.NewProjectButtonsLayout.addWidget(self.NewProjectCreateButton)
        self.NewProjectCancelButton = QtWidgets.QPushButton(AddNodeWindow)
        self.NewProjectCancelButton.setObjectName("NewProjectCancelButton")
        self.NewProjectButtonsLayout.addWidget(self.NewProjectCancelButton)
        self.AddNodeLayout.addLayout(self.NewProjectButtonsLayout)
        self.NewProjectWindowLayout.addLayout(self.AddNodeLayout, 0, 0, 1, 1)

        self.retranslateUi(AddNodeWindow)
        QtCore.QMetaObject.connectSlotsByName(AddNodeWindow)

    def retranslateUi(self, AddNodeWindow):
        _translate = QtCore.QCoreApplication.translate
        AddNodeWindow.setWindowTitle(_translate("AddNodeWindow", "Add Node"))
        self.NewProjectNameLabel.setText(_translate("AddNodeWindow", "Type:            "))
        self.NewProjectLocationLabel.setText(_translate("AddNodeWindow", "Name:           "))
        self.label.setText(_translate("AddNodeWindow", "IP Address:  "))
        self.label_2.setText(_translate("AddNodeWindow", "Port Number"))
        self.checkBox.setText(_translate("AddNodeWindow", "Scanner Node"))
        self.NewProjectCreateButton.setText(_translate("AddNodeWindow", "Add Node"))
        self.NewProjectCancelButton.setText(_translate("AddNodeWindow", "Cancel"))
