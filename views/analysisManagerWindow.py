from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import QTreeWidgetItem
import pyshark
import os


class Ui_AnalysisManagerWindow(object):

    def setupAnalysisManager(self, AnalysisManagerWindow):
        AnalysisManagerWindow.setObjectName("AnalysisManagerWindow")
        AnalysisManagerWindow.resize(1131, 747)
        AnalysisManagerWindow.setMinimumSize(QtCore.QSize(812, 580))
        self.CentralLayout_analysisManagerWindow = QtWidgets.QWidget(AnalysisManagerWindow)
        self.CentralLayout_analysisManagerWindow.setObjectName("CentralLayout_analysisManagerWindow")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.CentralLayout_analysisManagerWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.centralSectionLayout_analysisManagerWindow = QtWidgets.QHBoxLayout()
        self.centralSectionLayout_analysisManagerWindow.setObjectName("centralSectionLayout_analysisManagerWindow")
        self.scenariosList_analysisManagerWindow = QtWidgets.QTreeWidget(self.CentralLayout_analysisManagerWindow)
        self.scenariosList_analysisManagerWindow.setMinimumSize(QtCore.QSize(220, 0))
        self.scenariosList_analysisManagerWindow.setMaximumSize(QtCore.QSize(220, 16777215))
        self.scenariosList_analysisManagerWindow.setObjectName("scenariosList_analysisManagerWindow")
        self.centralSectionLayout_analysisManagerWindow.addWidget(self.scenariosList_analysisManagerWindow)
        self.scenariosLayout_analysisManagerWindow = QtWidgets.QVBoxLayout()
        self.scenariosLayout_analysisManagerWindow.setObjectName("scenariosLayout_analysisManagerWindow")
        self.pcapsLayout_analysisManagerWindow = QtWidgets.QVBoxLayout()
        self.pcapsLayout_analysisManagerWindow.setObjectName("pcapsLayout_analysisManagerWindow")
        self.Pcap_pcap = QtWidgets.QWidget()
        self.Pcap_pcap.setObjectName("Pcap_pcap")
        self.gridLayout = QtWidgets.QGridLayout(self.Pcap_pcap)
        self.gridLayout.setObjectName("gridLayout")
        self.pcapList_analysisManagerWindow = QtWidgets.QTreeWidget(self.Pcap_pcap)
        self.pcapList_analysisManagerWindow.setObjectName("pcapList_analysisManagerWindow")
        self.gridLayout.addWidget(self.pcapList_analysisManagerWindow, 0, 0, 1, 1)
        self.pcapsLayout_analysisManagerWindow.addWidget(self.pcapList_analysisManagerWindow)
        self.scenariosLayout_analysisManagerWindow.addLayout(self.pcapsLayout_analysisManagerWindow)
        self.protocolStatsLayout_analysisManagerWindow = QtWidgets.QHBoxLayout()
        self.protocolStatsLayout_analysisManagerWindow.setObjectName("protocolStatsLayout_analysisManagerWindow")
        self.protocolStatsList_analysisManagerWindow = QtWidgets.QTreeWidget(self.CentralLayout_analysisManagerWindow)
        self.protocolStatsList_analysisManagerWindow.setObjectName("protocolStatsList_analysisManagerWindow")
        self.protocolStatsLayout_analysisManagerWindow.addWidget(self.protocolStatsList_analysisManagerWindow)
        self.scenariosLayout_analysisManagerWindow.addLayout(self.protocolStatsLayout_analysisManagerWindow)
        self.centralSectionLayout_analysisManagerWindow.addLayout(self.scenariosLayout_analysisManagerWindow)
        self.gridLayout_2.addLayout(self.centralSectionLayout_analysisManagerWindow, 1, 0, 1, 1)
        self.buttonsLayout_analysisManagerWindow = QtWidgets.QHBoxLayout()
        self.buttonsLayout_analysisManagerWindow.setObjectName("buttonsLayout_analysisManagerWindow")


        self.filterInput_analysisManagerWindow = QtWidgets.QLineEdit(self.CentralLayout_analysisManagerWindow)
        self.filterInput_analysisManagerWindow.setObjectName("filterInput_analysisManagerWindow")
        self.buttonsLayout_analysisManagerWindow.addWidget(self.filterInput_analysisManagerWindow)

        self.filtersButton_analysisManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
        self.filtersButton_analysisManagerWindow.setObjectName("filtersButton_analysisManagerWindow")
        self.buttonsLayout_analysisManagerWindow.addWidget(self.filtersButton_analysisManagerWindow)
        self.closeAnalysisManager_analysisManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
        self.closeAnalysisManager_analysisManagerWindow.setObjectName("closeAnalysisManager_analysisManagerWindow")
        self.buttonsLayout_analysisManagerWindow.addWidget(self.closeAnalysisManager_analysisManagerWindow)
        self.gridLayout_2.addLayout(self.buttonsLayout_analysisManagerWindow, 0, 0, 1, 1)
        AnalysisManagerWindow.setCentralWidget(self.CentralLayout_analysisManagerWindow)

        QtCore.QMetaObject.connectSlotsByName(AnalysisManagerWindow)

        _translate = QtCore.QCoreApplication.translate
        AnalysisManagerWindow.setWindowTitle(_translate("AnalysisManagerWindow", "Scan Detection System - Analysis Manager"))
        self.scenariosList_analysisManagerWindow.headerItem().setText(0, _translate("AnalysisManagerWindow", "Pcap Files"))
        __sortingEnabled = self.scenariosList_analysisManagerWindow.isSortingEnabled()
        self.scenariosList_analysisManagerWindow.setSortingEnabled(False)
        self.scenariosList_analysisManagerWindow.setSortingEnabled(__sortingEnabled)
        self.pcapList_analysisManagerWindow.headerItem().setText(0, _translate("AnalysisManagerWindow", "No."))
        self.pcapList_analysisManagerWindow.headerItem().setText(1, _translate("AnalysisManagerWindow", "Time"))
        self.pcapList_analysisManagerWindow.headerItem().setText(2, _translate("AnalysisManagerWindow", "Source"))
        self.pcapList_analysisManagerWindow.headerItem().setText(3, _translate("AnalysisManagerWindow", "Destination"))
        self.pcapList_analysisManagerWindow.headerItem().setText(4, _translate("AnalysisManagerWindow", "Protocol"))
        self.pcapList_analysisManagerWindow.headerItem().setText(5, _translate("AnalysisManagerWindow", "Length"))
        self.pcapList_analysisManagerWindow.headerItem().setText(6, _translate("AnalysisManagerWindow", "Info"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(0, _translate("AnalysisManagerWindow", "Protocol"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(1, _translate("AnalysisManagerWindow", "Percent Packets"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(2, _translate("AnalysisManagerWindow", "Packets"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(3, _translate("AnalysisManagerWindow", "Percent Bytes"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(4, _translate("AnalysisManagerWindow", "Bytes"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(5, _translate("AnalysisManagerWindow", "Bits/s"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(6, _translate("AnalysisManagerWindow", "End Packets"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(7, _translate("AnalysisManagerWindow", "End Bytes"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(8, _translate("AnalysisManagerWindow", "End Bits/s"))
        self.filtersButton_analysisManagerWindow.setToolTip(_translate("AnalysisManagerWindow", "New Project"))
        self.filtersButton_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "      Apply Filter      "))
        self.closeAnalysisManager_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "Close Analysis Manager"))

        self.scenariosList_analysisManagerWindow.itemSelectionChanged.connect(self.pcap_selected)

        for file in os.listdir('pcaps'):
            x = QtWidgets.QTreeWidgetItem([str(file)])
            self.scenariosList_analysisManagerWindow.addTopLevelItem(x)


    def pcap_selected(self):
        self.pcapList_analysisManagerWindow.clear()

        cap = pyshark.FileCapture('pcaps/' + self.scenariosList_analysisManagerWindow.selectedItems()[0].text(0),
                                  only_summaries=True)

        for pkt in cap:
            l = []
            l.append(str(pkt.no))
            l.append(str(pkt.time))
            l.append(str(pkt.source))
            l.append(str(pkt.destination))
            l.append(str(pkt.protocol))
            l.append(str(pkt.length))
            l.append(str(pkt.info))
            l1 = QTreeWidgetItem(l)
            self.pcapList_analysisManagerWindow.addTopLevelItem(l1)
