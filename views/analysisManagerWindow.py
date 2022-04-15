from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import QTreeWidgetItem
import pyshark
import os

from Models.pcap import Pcap
from Models.capture import Capture


class Ui_AnalysisManagerWindow(object):

    # test_pcap = Pcap("first pcap", "./pcaps", "first pcap")
    # # test_pcap.create_json_file()
    # # test_pcap.to_json()
    # # test_pcap.create_json_file()
    # # test_pcap.to_json()
    # test_capture.add_pcap(test_pcap)
    # test_capture.add_pcap(test_pcap_2)

    test_capture = Capture("", os.path.join(os.getcwd(), "pcaps"))
    # test_capture.add_pcap(Pcap("/pcap1.pcap", "./pcaps", "pcap1.pcap"))
    #test_capture.add_pcap(Pcap(os.path.join("pcap1.pcap"), "", "pcap1.pcap"))
    #test_capture.add_pcap(Pcap(os.path.join("pcap2.pcapng"), "", "pcap2.pcap"))
    #test_capture.add_pcap(Pcap(os.path.join("pcap3.pcapng"), "", "pcap3.pcap"))


    #test_capture.create_merged_file()
    #test_capture.merge_pcaps()

    # self.iterate_packets(cap)
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
        self.pcapsTabWidget_analysisManagerWindow = QtWidgets.QTabWidget(self.CentralLayout_analysisManagerWindow)
        self.pcapsTabWidget_analysisManagerWindow.setObjectName("pcapsTabWidget_analysisManagerWindow")
        # self.Pcap_pcap = QtWidgets.QWidget()
        # self.Pcap_pcap.setObjectName("Pcap_pcap")
        # self.gridLayout = QtWidgets.QGridLayout(self.Pcap_pcap)
        # self.gridLayout.setObjectName("gridLayout")
        # self.pcapList_analysisManagerWindow = QtWidgets.QTreeWidget()
        # self.pcapList_analysisManagerWindow.setObjectName("pcapList_analysisManagerWindow")
        # self.gridLayout.addWidget(self.pcapList_analysisManagerWindow, 0, 0, 1, 1)
        # self.pcapsTabWidget_analysisManagerWindow.addTab(self.Pcap_pcap, "")
        #self.pcap_1 = QtWidgets.QWidget()
        #self.pcap_1.setObjectName("pcap_1")
        #self.pcapsTabWidget_analysisManagerWindow.addTab(self.pcap_1, "")
        self.pcapsLayout_analysisManagerWindow.addWidget(self.pcapsTabWidget_analysisManagerWindow)
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
        self.filtersButton_analysisManagerWindow.clicked.connect(
            lambda: self.iterate_packets(self.test_capture, self.filterInput_analysisManagerWindow.text(), self.scenariosList_analysisManagerWindow.selectedItems()[0].text(0)))
        self.buttonsLayout_analysisManagerWindow.addWidget(self.filtersButton_analysisManagerWindow)

        self.mergeAllButton_analysisManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
        self.mergeAllButton_analysisManagerWindow.setObjectName("mergeAllButton_analysisManagerWindow")
        self.mergeAllButton_analysisManagerWindow.clicked.connect(
            lambda: self.merge_all())
        self.buttonsLayout_analysisManagerWindow.addWidget(self.mergeAllButton_analysisManagerWindow)


        self.closeAnalysisManager_analysisManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
        self.closeAnalysisManager_analysisManagerWindow.setObjectName("closeAnalysisManager_analysisManagerWindow")
        self.buttonsLayout_analysisManagerWindow.addWidget(self.closeAnalysisManager_analysisManagerWindow)
        self.gridLayout_2.addLayout(self.buttonsLayout_analysisManagerWindow, 0, 0, 1, 1)
        AnalysisManagerWindow.setCentralWidget(self.CentralLayout_analysisManagerWindow)
        self.closeAnalysisManager_analysisManagerWindow.clicked.connect(AnalysisManagerWindow.close)

        QtCore.QMetaObject.connectSlotsByName(AnalysisManagerWindow)

        _translate = QtCore.QCoreApplication.translate
        AnalysisManagerWindow.setWindowTitle(_translate("AnalysisManagerWindow", "Scan Detection System - Analysis Manager"))
        self.scenariosList_analysisManagerWindow.headerItem().setText(0, _translate("AnalysisManagerWindow", "Pcap Files"))
        __sortingEnabled = self.scenariosList_analysisManagerWindow.isSortingEnabled()
        self.scenariosList_analysisManagerWindow.setSortingEnabled(False)
        self.scenariosList_analysisManagerWindow.setSortingEnabled(__sortingEnabled)
        #self.pcapsTabWidget_analysisManagerWindow.setTabText(self.pcapsTabWidget_analysisManagerWindow.indexOf(self.Pcap_pcap), _translate("AnalysisManagerWindow", "Pcap.pcap"))
        #self.pcapsTabWidget_analysisManagerWindow.setTabText(self.pcapsTabWidget_analysisManagerWindow.indexOf(self.pcap_1), _translate("AnalysisManagerWindow", "1.pcap"))
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
        self.mergeAllButton_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "      Merge All Pcaps      "))
        self.closeAnalysisManager_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "Close Analysis Manager"))
        #self.iterate_packets(self.test_capture, "", 0)
        self.add_pcaps()
        self.show_pcap_list()
        self.scenariosList_analysisManagerWindow.doubleClicked.connect(lambda: self.open_tab())
        # self.scenariosList_analysisManagerWindow.doubleClicked.connect(
        #     lambda: self.iterate_packets(self.test_capture, "",
        #                                  self.scenariosList_analysisManagerWindow.selectedItems()[0].text(0)))

























        # cap = pyshark.FileCapture('pcap1.pcap',
        #                           only_summaries=True)
        # for pkt in cap:
        #     l = []
        #     l.append(str(pkt.no))
        #     l.append(str(pkt.time))
        #     l.append(str(pkt.source))
        #     l.append(str(pkt.destination))
        #     l.append(str(pkt.protocol))
        #     l.append(str(pkt.length))
        #     l.append(str(pkt.info))
        #     l1 = QTreeWidgetItem(l)
        #     self.pcapList_analysisManagerWindow.addTopLevelItem(l1)

    def iterate_packets(self,capture, filter, pcap):
        self.pcapList_analysisManagerWindow.clear()
        packets = capture.iterate_file(filter, pcap)

        for pkt in packets:
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
        packets.close()
    def show_pcap_list(self):
        self.scenariosList_analysisManagerWindow.clear()
        for pcap in self.test_capture.pcaps:
            print(pcap.name)
            x = QtWidgets.QTreeWidgetItem([pcap.name])
            self.scenariosList_analysisManagerWindow.addTopLevelItem(x)
    def open_tab(self):
        pcap = QtWidgets.QWidget()
        pcap.setObjectName(self.scenariosList_analysisManagerWindow.selectedItems()[0].text(0))
        #gridLayout = QtWidgets.QGridLayout(pcap)
        #gridLayout.setObjectName("gridLayout")

        self.gridLayout = QtWidgets.QGridLayout(pcap)
        self.gridLayout.setObjectName("gridLayout")
        self.pcapList_analysisManagerWindow = QtWidgets.QTreeWidget()
        self.pcapList_analysisManagerWindow.setObjectName("pcapList_analysisManagerWindow")
        self.gridLayout.addWidget(self.pcapList_analysisManagerWindow, 0, 0, 1, 1)
        self.pcapsTabWidget_analysisManagerWindow.addTab(pcap, self.scenariosList_analysisManagerWindow.selectedItems()[0].text(0))
        self.pcapList_analysisManagerWindow.headerItem().setText(0,  "No.")
        self.pcapList_analysisManagerWindow.headerItem().setText(1,  "Time")
        self.pcapList_analysisManagerWindow.headerItem().setText(2,  "Source")
        self.pcapList_analysisManagerWindow.headerItem().setText(3,  "Destination")
        self.pcapList_analysisManagerWindow.headerItem().setText(4,  "Protocol")
        self.pcapList_analysisManagerWindow.headerItem().setText(5,  "Length")
        self.pcapList_analysisManagerWindow.headerItem().setText(6,  "Info")



        self.pcapsTabWidget_analysisManagerWindow.addTab(pcap, self.scenariosList_analysisManagerWindow.selectedItems()[0].text(0))
        #self.gridLayout.addWidget(self.pcapList_analysisManagerWindow, 0, 0, 1, 1)

        self.iterate_packets(self.test_capture, "",
                             self.scenariosList_analysisManagerWindow.selectedItems()[0].text(0))
        self.pcapsTabWidget_analysisManagerWindow.tabsClosable()

    def add_pcaps(self):
        for filename in os.listdir(self.test_capture.path):
            f = os.path.join(self.test_capture.path, filename)
            if os.path.isfile(f):
                print(filename)
                pcap = Pcap(filename, self.test_capture.path, filename)
                self.test_capture.add_pcap(pcap)

    def merge_all(self):
        self.test_capture.create_merged_file()
        self.test_capture.merge_pcaps()
        self.show_pcap_list()