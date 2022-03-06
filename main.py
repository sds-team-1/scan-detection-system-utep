from random import random
from PyQt5 import QtCore, QtGui, QtWidgets
from Helpers import DatabaseHelper as DatabaseHelper
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 700)
        MainWindow.setMinimumSize(QtCore.QSize(812, 580))

        self.CentralLayout_MainWindow = QtWidgets.QWidget(MainWindow)
        self.CentralLayout_MainWindow.setObjectName("CentralLayout_MainWindow")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.CentralLayout_MainWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.TabWidgetLayout_MainWindow = QtWidgets.QVBoxLayout()
        self.TabWidgetLayout_MainWindow.setObjectName("TabWidgetLayout_MainWindow")

        self.TabWidget_MainWindow = QtWidgets.QTabWidget(self.CentralLayout_MainWindow)
        self.TabWidget_MainWindow.setObjectName("TabWidget_MainWindow")

        self.TabWidgetLayout_MainWindow.addWidget(self.TabWidget_MainWindow)
        self.gridLayout_2.addLayout(self.TabWidgetLayout_MainWindow, 1, 0, 1, 1)

        self.ButtonsLayout_MainWindow = QtWidgets.QHBoxLayout()
        self.ButtonsLayout_MainWindow.setObjectName("ButtonsLayout_MainWindow")
        self.NewButton_MainWindow = QtWidgets.QPushButton(self.CentralLayout_MainWindow)
        self.NewButton_MainWindow.setObjectName("NewButton_MainWindow")
        self.ButtonsLayout_MainWindow.addWidget(self.NewButton_MainWindow)
        self.OpenButton_MainWindow = QtWidgets.QPushButton(self.CentralLayout_MainWindow)
        self.OpenButton_MainWindow.setObjectName("OpenButton_MainWindow")
        self.ButtonsLayout_MainWindow.addWidget(self.OpenButton_MainWindow)
        self.SaveButton_MainWindow = QtWidgets.QPushButton(self.CentralLayout_MainWindow)
        self.SaveButton_MainWindow.setObjectName("SaveButton_MainWindow")
        self.ButtonsLayout_MainWindow.addWidget(self.SaveButton_MainWindow)
        self.ImportButton_MainWindow = QtWidgets.QPushButton(self.CentralLayout_MainWindow)
        self.ImportButton_MainWindow.setObjectName("ImportButton_MainWindow")
        self.ButtonsLayout_MainWindow.addWidget(self.ImportButton_MainWindow)
        self.ExportButton_MainWindow = QtWidgets.QPushButton(self.CentralLayout_MainWindow)
        self.ExportButton_MainWindow.setObjectName("ExportButton_MainWindow")
        self.ButtonsLayout_MainWindow.addWidget(self.ExportButton_MainWindow)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ButtonsLayout_MainWindow.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.ButtonsLayout_MainWindow, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.CentralLayout_MainWindow)

        self.retranslateUi(MainWindow)
        self.TabWidget_MainWindow.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scan Detection System"))

        self.NewButton_MainWindow.setToolTip(_translate("MainWindow", "New Project"))
        self.NewButton_MainWindow.setText(_translate("MainWindow", "  New  "))
        self.OpenButton_MainWindow.setToolTip(_translate("MainWindow", "Open Project"))
        self.OpenButton_MainWindow.setText(_translate("MainWindow", "  Open  "))
        self.SaveButton_MainWindow.setToolTip(_translate("MainWindow", "Save Project"))
        self.SaveButton_MainWindow.setText(_translate("MainWindow", "  Save  "))
        self.ImportButton_MainWindow.setToolTip(_translate("MainWindow", "Import Project"))
        self.ImportButton_MainWindow.setText(_translate("MainWindow", "Import"))
        self.ExportButton_MainWindow.setToolTip(_translate("MainWindow", "Export Project"))
        self.ExportButton_MainWindow.setText(_translate("MainWindow", "Export"))

        self.NewButton_MainWindow.clicked.connect(self.add_tab)

        self.SaveButton_MainWindow.setEnabled(False)
        self.ExportButton_MainWindow.setEnabled(False)

    def add_tab(self):
        _translate = QtCore.QCoreApplication.translate

        for i in range(2):
            s = str(i + 1)
            s = 'Scenario ' + s
            self.Tab_MainWindow = QtWidgets.QWidget()
            self.Tab_MainWindow.setObjectName("Tab_MainWindow")
            self.gridLayout = QtWidgets.QGridLayout(self.Tab_MainWindow)
            self.gridLayout.setObjectName("gridLayout")
            self.TabLayout_MainWindow = QtWidgets.QVBoxLayout()
            self.TabLayout_MainWindow.setObjectName("TabLayout_MainWindow")
            self.ScenarioButtonsLayout_MainWindow = QtWidgets.QHBoxLayout()
            self.ScenarioButtonsLayout_MainWindow.setObjectName("ScenarioButtonsLayout_MainWindow")
            self.StartScenarioButton_MainWindow = QtWidgets.QPushButton(self.Tab_MainWindow)
            self.StartScenarioButton_MainWindow.setObjectName("StartScenarioButton_MainWindow")
            self.ScenarioButtonsLayout_MainWindow.addWidget(self.StartScenarioButton_MainWindow)
            self.StopScenarioButton_MainWindow = QtWidgets.QPushButton(self.Tab_MainWindow)
            self.StopScenarioButton_MainWindow.setObjectName("StopScenarioButton_MainWindow")
            self.ScenarioButtonsLayout_MainWindow.addWidget(self.StopScenarioButton_MainWindow)
            self.RestoreScenarioButton_MainWindow = QtWidgets.QPushButton(self.Tab_MainWindow)
            self.RestoreScenarioButton_MainWindow.setObjectName("RestoreScenarioButton_MainWindow")
            self.ScenarioButtonsLayout_MainWindow.addWidget(self.RestoreScenarioButton_MainWindow)
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.ScenarioButtonsLayout_MainWindow.addItem(spacerItem)
            self.TabLayout_MainWindow.addLayout(self.ScenarioButtonsLayout_MainWindow)
            self.ServicesLayout_MainWindow = QtWidgets.QVBoxLayout()
            self.ServicesLayout_MainWindow.setObjectName("ServicesLayout_MainWindow")
            self.CORESDSServiceLayout_MainWindow = QtWidgets.QHBoxLayout()
            self.CORESDSServiceLayout_MainWindow.setObjectName("CORESDSServiceLayout_MainWindow")
            self.CORESDSServiceLabel_MainWindow = QtWidgets.QLabel(self.Tab_MainWindow)
            self.CORESDSServiceLabel_MainWindow.setObjectName("CORESDSServiceLabel_MainWindow")
            self.CORESDSServiceLayout_MainWindow.addWidget(self.CORESDSServiceLabel_MainWindow)
            self.CORESDSServiceInput_MainWindow = QtWidgets.QLineEdit(self.Tab_MainWindow)
            self.CORESDSServiceInput_MainWindow.setObjectName("CORESDSServiceInput_MainWindow")
            self.CORESDSServiceLayout_MainWindow.addWidget(self.CORESDSServiceInput_MainWindow)
            self.ServicesLayout_MainWindow.addLayout(self.CORESDSServiceLayout_MainWindow)
            self.COREPortLayout_MainWindow = QtWidgets.QHBoxLayout()
            self.COREPortLayout_MainWindow.setObjectName("COREPortLayout_MainWindow")
            self.COREPortLabel_MainWindow = QtWidgets.QLabel(self.Tab_MainWindow)
            self.COREPortLabel_MainWindow.setObjectName("COREPortLabel_MainWindow")
            self.COREPortLayout_MainWindow.addWidget(self.COREPortLabel_MainWindow)
            self.COREPortInput_MainWindow = QtWidgets.QLineEdit(self.Tab_MainWindow)
            self.COREPortInput_MainWindow.setObjectName("COREPortInput_MainWindow")
            self.COREPortLayout_MainWindow.addWidget(self.COREPortInput_MainWindow)
            self.ServicesLayout_MainWindow.addLayout(self.COREPortLayout_MainWindow)
            self.SDSVMServiceLayout_MainWindow = QtWidgets.QHBoxLayout()
            self.SDSVMServiceLayout_MainWindow.setObjectName("SDSVMServiceLayout_MainWindow")
            self.SDSVMServiceLabel_MainWindow = QtWidgets.QLabel(self.Tab_MainWindow)
            self.SDSVMServiceLabel_MainWindow.setObjectName("SDSVMServiceLabel_MainWindow")
            self.SDSVMServiceLayout_MainWindow.addWidget(self.SDSVMServiceLabel_MainWindow)
            self.SDSVMServiceInput_MainWindow = QtWidgets.QLineEdit(self.Tab_MainWindow)
            self.SDSVMServiceInput_MainWindow.setObjectName("SDSVMServiceInput_MainWindow")
            self.SDSVMServiceLayout_MainWindow.addWidget(self.SDSVMServiceInput_MainWindow)
            self.ServicesLayout_MainWindow.addLayout(self.SDSVMServiceLayout_MainWindow)
            self.SDSDockerServiceLayout_MainWindow = QtWidgets.QHBoxLayout()
            self.SDSDockerServiceLayout_MainWindow.setObjectName("SDSDockerServiceLayout_MainWindow")
            self.SDSDockerServiceLabel_MainWindow = QtWidgets.QLabel(self.Tab_MainWindow)
            self.SDSDockerServiceLabel_MainWindow.setObjectName("SDSDockerServiceLabel_MainWindow")
            self.SDSDockerServiceLayout_MainWindow.addWidget(self.SDSDockerServiceLabel_MainWindow)
            self.SDSDockerServiceInput_MainWindow = QtWidgets.QLineEdit(self.Tab_MainWindow)
            self.SDSDockerServiceInput_MainWindow.setObjectName("SDSDockerServiceInput_MainWindow")
            self.SDSDockerServiceLayout_MainWindow.addWidget(self.SDSDockerServiceInput_MainWindow)
            self.ServicesLayout_MainWindow.addLayout(self.SDSDockerServiceLayout_MainWindow)
            self.TabLayout_MainWindow.addLayout(self.ServicesLayout_MainWindow)
            self.NodesTreeWidget_MainWindow = QtWidgets.QTreeWidget(self.Tab_MainWindow)
            self.NodesTreeWidget_MainWindow.setObjectName("NodesTreeWidget_MainWindow")
            font = QtGui.QFont()
            font.setPointSize(14)
            font.setBold(False)
            font.setWeight(50)
            self.NodesTreeWidget_MainWindow.headerItem().setFont(0, font)
            font = QtGui.QFont()
            font.setPointSize(14)
            font.setBold(False)
            font.setWeight(50)
            self.NodesTreeWidget_MainWindow.headerItem().setFont(1, font)
            font = QtGui.QFont()
            font.setPointSize(14)
            font.setBold(False)
            font.setWeight(50)
            self.NodesTreeWidget_MainWindow.headerItem().setFont(2, font)
            font = QtGui.QFont()
            font.setPointSize(14)
            self.NodesTreeWidget_MainWindow.headerItem().setFont(3, font)
            font = QtGui.QFont()
            font.setPointSize(14)
            self.NodesTreeWidget_MainWindow.headerItem().setFont(4, font)
            font = QtGui.QFont()
            font.setPointSize(14)
            font.setBold(False)
            font.setWeight(50)
            self.NodesTreeWidget_MainWindow.headerItem().setFont(5, font)
            font = QtGui.QFont()
            font.setPointSize(14)
            font.setBold(False)
            font.setWeight(50)
            self.NodesTreeWidget_MainWindow.headerItem().setFont(6, font)
            self.TabLayout_MainWindow.addWidget(self.NodesTreeWidget_MainWindow)
            self.ScenarioBottomSectionLayout_MainWindow = QtWidgets.QHBoxLayout()
            self.ScenarioBottomSectionLayout_MainWindow.setObjectName("ScenarioBottomSectionLayout_MainWindow")
            self.ScenarioStatusLabel_MainWindow = QtWidgets.QLabel(self.Tab_MainWindow)
            self.ScenarioStatusLabel_MainWindow.setObjectName("ScenarioStatusLabel_MainWindow")
            self.ScenarioBottomSectionLayout_MainWindow.addWidget(self.ScenarioStatusLabel_MainWindow)
            self.ScenarioStatus_MainWindow = QtWidgets.QLabel(self.Tab_MainWindow)
            self.ScenarioStatus_MainWindow.setObjectName("ScenarioStatus_MainWindow")
            self.ScenarioBottomSectionLayout_MainWindow.addWidget(self.ScenarioStatus_MainWindow)
            spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.ScenarioBottomSectionLayout_MainWindow.addItem(spacerItem1)
            self.ScenarioAddNodeButton_MainWindow = QtWidgets.QPushButton(self.Tab_MainWindow)
            self.ScenarioAddNodeButton_MainWindow.setObjectName("ScenarioAddNodeButton_MainWindow")
            self.ScenarioBottomSectionLayout_MainWindow.addWidget(self.ScenarioAddNodeButton_MainWindow)
            self.TabLayout_MainWindow.addLayout(self.ScenarioBottomSectionLayout_MainWindow)
            self.gridLayout.addLayout(self.TabLayout_MainWindow, 0, 0, 1, 1)

            self.TabWidget_MainWindow.addTab(self.Tab_MainWindow, s)

            self.StartScenarioButton_MainWindow.setToolTip(_translate("MainWindow", "Start Scenario"))
            self.StartScenarioButton_MainWindow.setText(_translate("MainWindow", "  Start  "))
            self.StopScenarioButton_MainWindow.setToolTip(_translate("MainWindow", "Stop Scenario"))
            self.StopScenarioButton_MainWindow.setText(_translate("MainWindow", "  Stop  "))
            self.RestoreScenarioButton_MainWindow.setToolTip(_translate("MainWindow", "Restore Scenario"))
            self.RestoreScenarioButton_MainWindow.setText(_translate("MainWindow", "Restore"))
            self.CORESDSServiceLabel_MainWindow.setText(_translate("MainWindow", "CORE SDS Service:   "))
            self.COREPortLabel_MainWindow.setText(_translate("MainWindow", "CORE Port Number:  "))
            self.SDSVMServiceLabel_MainWindow.setText(_translate("MainWindow", "SDS VM Service:       "))
            self.SDSDockerServiceLabel_MainWindow.setText(_translate("MainWindow", "SDS Docker Service:"))
            self.NodesTreeWidget_MainWindow.headerItem().setText(0, _translate("MainWindow", "Listening"))
            self.NodesTreeWidget_MainWindow.headerItem().setText(1, _translate("MainWindow",
                                                                               "Type                                               "))
            self.NodesTreeWidget_MainWindow.headerItem().setText(2, _translate("MainWindow",
                                                                               "Name                                                                                                                                          "))
            self.NodesTreeWidget_MainWindow.headerItem().setText(3, _translate("MainWindow", "MAC Address  "))
            self.NodesTreeWidget_MainWindow.headerItem().setText(4, _translate("MainWindow", "IP Address"))
            self.NodesTreeWidget_MainWindow.headerItem().setText(5, _translate("MainWindow", "Port Number"))
            self.NodesTreeWidget_MainWindow.headerItem().setText(6, _translate("MainWindow", "Scan/Victim Node"))
            self.ScenarioStatusLabel_MainWindow.setText(_translate("MainWindow", "Scenario Status:"))
            self.ScenarioStatus_MainWindow.setText(_translate("MainWindow", "Active"))
            self.ScenarioAddNodeButton_MainWindow.setToolTip(_translate("MainWindow", "Add New Node"))
            self.ScenarioAddNodeButton_MainWindow.setText(_translate("MainWindow", "  Add Node  "))
            self.TabWidget_MainWindow.setTabText(self.TabWidget_MainWindow.indexOf(self.Tab_MainWindow),
                                                 _translate("MainWindow", s))

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    # example of how to insert a document into mongo
    # SDSdb = DatabaseHelper.SDSDatabaseHelper()
    # tempObjectToInsert = {}
    # tempObjectToInsert['name'] = 'Test'
    # tempObjectToInsert['type'] = 'test type'
    # tempObjectToInsert['_id'] = random.randint(1, 100)
    # SDSdb.insertObject(tempObjectToInsert)

    sys.exit(app.exec_())