from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import QTreeWidgetItem, QFileDialog
import pyshark
import os

from Models.pcap import Pcap
from Models.capture import Capture


def add_pcaps(capture):
    for filename in os.listdir(capture.path):
        f = os.path.join(capture.path, filename)
        if os.path.isfile(f):
            if '.pcap' in filename or '.pcapng' in filename:
                pcap = Pcap(filename, capture.path, filename)
                capture.add_pcap(pcap)


class Ui_AnalysisManagerWindow(object):

    # test_pcap = Pcap("first pcap", "./pcaps", "first pcap")
    # # test_pcap.create_json_file()
    # # test_pcap.to_json()
    # # test_pcap.create_json_file()
    # # test_pcap.to_json()

    def setupAnalysisManager(self, AnalysisManagerWindow, InitialWorkspaceWindow):
        self.InitialWorkspaceWindow = InitialWorkspaceWindow
        AnalysisManagerWindow.setObjectName("AnalysisManagerWindow")
        AnalysisManagerWindow.resize(1131, 747)
        AnalysisManagerWindow.setMinimumSize(QtCore.QSize(812, 580))
        self.CentralLayout_analysisManagerWindow = QtWidgets.QWidget(AnalysisManagerWindow)
        self.CentralLayout_analysisManagerWindow.setObjectName("CentralLayout_analysisManagerWindow")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.CentralLayout_analysisManagerWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.upperLayout_analysisManagerWindow = QtWidgets.QVBoxLayout()
        self.upperLayout_analysisManagerWindow.setObjectName("upperLayout_analysisManagerWindow")
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
        self.buttonsLayout_analysisManagerWindow.addWidget(self.filtersButton_analysisManagerWindow)
        self.mergeButton_analysisManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
        self.mergeButton_analysisManagerWindow.setObjectName("mergeButton_analysisManagerWindow")
        self.buttonsLayout_analysisManagerWindow.addWidget(self.mergeButton_analysisManagerWindow)
        self.exportButton_analysisManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
        self.exportButton_analysisManagerWindow.setObjectName("exportButton_analysisManagerWindow")
        self.buttonsLayout_analysisManagerWindow.addWidget(self.exportButton_analysisManagerWindow)
        self.closeAnalysisManager_analysisManagerWindow = QtWidgets.QPushButton(
            self.CentralLayout_analysisManagerWindow)
        self.closeAnalysisManager_analysisManagerWindow.setObjectName("closeAnalysisManager_analysisManagerWindow")
        self.buttonsLayout_analysisManagerWindow.addWidget(self.closeAnalysisManager_analysisManagerWindow)
        self.upperLayout_analysisManagerWindow.addLayout(self.buttonsLayout_analysisManagerWindow)

        self.layoutPcapsDirectory_analysisManagerWindow = QtWidgets.QHBoxLayout()
        self.layoutPcapsDirectory_analysisManagerWindow.setObjectName("layoutPcapsDirectory_analysisManagerWindow")
        self.inputPcapsDirectory_analysisManagerWindow = QtWidgets.QLineEdit(self.CentralLayout_analysisManagerWindow)
        self.inputPcapsDirectory_analysisManagerWindow.setObjectName("inputPcapsDirectory_analysisManagerWindow")
        self.layoutPcapsDirectory_analysisManagerWindow.addWidget(self.inputPcapsDirectory_analysisManagerWindow)
        self.browsePcapsDirectory_analysisManagerWindow = QtWidgets.QPushButton(
            self.CentralLayout_analysisManagerWindow)
        self.browsePcapsDirectory_analysisManagerWindow.setObjectName("browsePcapsDirectory_analysisManagerWindow")
        self.layoutPcapsDirectory_analysisManagerWindow.addWidget(self.browsePcapsDirectory_analysisManagerWindow)
        # spacerItem1 = QtWidgets.QSpacerItem(418, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # self.layoutPcapsDirectory_analysisManagerWindow.addItem(spacerItem1)
        self.upperLayout_analysisManagerWindow.addLayout(self.layoutPcapsDirectory_analysisManagerWindow)

        self.gridLayout_2.addLayout(self.upperLayout_analysisManagerWindow, 0, 0, 1, 1)
        AnalysisManagerWindow.setCentralWidget(self.CentralLayout_analysisManagerWindow)
        self.closeAnalysisManager_analysisManagerWindow.clicked.connect(
            lambda: self.closeAnalysisManager(AnalysisManagerWindow))

        QtCore.QMetaObject.connectSlotsByName(AnalysisManagerWindow)

        _translate = QtCore.QCoreApplication.translate
        AnalysisManagerWindow.setWindowTitle(
            _translate("AnalysisManagerWindow", "Scan Detection System - Analysis Manager"))
        self.scenariosList_analysisManagerWindow.headerItem().setText(0,
                                                                      _translate("AnalysisManagerWindow", "Pcap Files"))
        __sortingEnabled = self.scenariosList_analysisManagerWindow.isSortingEnabled()
        self.scenariosList_analysisManagerWindow.setSortingEnabled(False)
        self.scenariosList_analysisManagerWindow.setSortingEnabled(__sortingEnabled)
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(0, _translate("AnalysisManagerWindow",
                                                                                        "Protocol"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(1, _translate("AnalysisManagerWindow",
                                                                                        "Percent Packets"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(2, _translate("AnalysisManagerWindow",
                                                                                        "Packets"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(3, _translate("AnalysisManagerWindow",
                                                                                        "Percent Bytes"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(4,
                                                                          _translate("AnalysisManagerWindow", "Bytes"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(5,
                                                                          _translate("AnalysisManagerWindow", "Bits/s"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(6, _translate("AnalysisManagerWindow",
                                                                                        "End Packets"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(7, _translate("AnalysisManagerWindow",
                                                                                        "End Bytes"))
        self.protocolStatsList_analysisManagerWindow.headerItem().setText(8, _translate("AnalysisManagerWindow",
                                                                                        "End Bits/s"))
        self.filtersButton_analysisManagerWindow.setToolTip(_translate("AnalysisManagerWindow", "New Project"))
        self.filtersButton_analysisManagerWindow.setText(
            _translate("AnalysisManagerWindow", "      Apply Filter      "))
        self.mergeButton_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "      Merge Pcaps      "))
        self.exportButton_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "      Export Pcaps      "))
        self.browsePcapsDirectory_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "    Browse   "))
        self.closeAnalysisManager_analysisManagerWindow.setText(
            _translate("AnalysisManagerWindow", "Close Analysis Manager"))

        self.scenariosList_analysisManagerWindow.clicked.connect(self.selectedPcapCheckbox)
        self.scenariosList_analysisManagerWindow.itemSelectionChanged.connect(self.pcap_selected)
        self.scenariosList_analysisManagerWindow.doubleClicked.connect(lambda: self.open_tab())
        self.filtersButton_analysisManagerWindow.clicked.connect(
            lambda: self.iterate_packets(self.test_capture, self.filterInput_analysisManagerWindow.text(),
                                         self.scenariosList_analysisManagerWindow.selectedItems()[0].text(0)))

        self.mergeButton_analysisManagerWindow.clicked.connect(lambda: self.merge())

        self.inputPcapsDirectory_analysisManagerWindow.setReadOnly(True)

        self.filtersButton_analysisManagerWindow.setEnabled(False)
        self.mergeButton_analysisManagerWindow.setEnabled(False)
        self.exportButton_analysisManagerWindow.setEnabled(False)

        self.browsePcapsDirectory_analysisManagerWindow.clicked.connect(self.browsePcapDir)

        AnalysisManagerWindow.closeEvent = self.CloseEvent

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

        # self.Pcap_pcap = QtWidgets.QWidget()
        # self.Pcap_pcap.setObjectName("Pcap_pcap")
        # self.gridLayout = QtWidgets.QGridLayout(self.Pcap_pcap)
        # self.gridLayout.setObjectName("gridLayout")
        # self.pcapList_analysisManagerWindow = QtWidgets.QTreeWidget()
        # self.pcapList_analysisManagerWindow.setObjectName("pcapList_analysisManagerWindow")
        # self.gridLayout.addWidget(self.pcapList_analysisManagerWindow, 0, 0, 1, 1)
        # self.pcapsTabWidget_analysisManagerWindow.addTab(self.Pcap_pcap, "")
        # self.pcap_1 = QtWidgets.QWidget()
        # self.pcap_1.setObjectName("pcap_1")
        # self.pcapsTabWidget_analysisManagerWindow.addTab(self.pcap_1, "")

        # self.iterate_packets(self.test_capture, "", 0)

        # self.pcapsTabWidget_analysisManagerWindow.setTabText(self.pcapsTabWidget_analysisManagerWindow.indexOf(self.Pcap_pcap), _translate("AnalysisManagerWindow", "Pcap.pcap"))
        # self.pcapsTabWidget_analysisManagerWindow.setTabText(self.pcapsTabWidget_analysisManagerWindow.indexOf(self.pcap_1), _translate("AnalysisManagerWindow", "1.pcap"))


    def closeAnalysisManager(self, AnalysisManagerWindow):
        AnalysisManagerWindow.close()
        self.InitialWorkspaceWindow.show()


    def CloseEvent(self, event):
        self.InitialWorkspaceWindow.show()


    def iterate_packets(self, capture, filter, pcap):
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

    def pcap_selected(self):
        self.filtersButton_analysisManagerWindow.setEnabled(True)

    def selectedPcapCheckbox(self):
        checked = 0

        for i in range(self.scenariosList_analysisManagerWindow.topLevelItemCount()):
            top_item = self.scenariosList_analysisManagerWindow.topLevelItem(i)
            if top_item.checkState(0) == 2:
                checked += 1

        if checked > 1:
            self.mergeButton_analysisManagerWindow.setEnabled(True)
            self.exportButton_analysisManagerWindow.setEnabled(True)

        else:
            self.mergeButton_analysisManagerWindow.setEnabled(False)
            self.exportButton_analysisManagerWindow.setEnabled(False)

    def show_pcap_list(self, capture):
        self.scenariosList_analysisManagerWindow.clear()
        for pcap in capture.pcaps:
            x = QtWidgets.QTreeWidgetItem([pcap.name])
            x.setCheckState(0, QtCore.Qt.Unchecked)
            self.scenariosList_analysisManagerWindow.addTopLevelItem(x)

    def open_tab(self):
        pcap = QtWidgets.QWidget()
        pcap.setObjectName(self.scenariosList_analysisManagerWindow.selectedItems()[0].text(0))
        # gridLayout = QtWidgets.QGridLayout(pcap)
        # gridLayout.setObjectName("gridLayout")

        self.gridLayout = QtWidgets.QGridLayout(pcap)
        self.gridLayout.setObjectName("gridLayout")
        self.pcapList_analysisManagerWindow = QtWidgets.QTreeWidget()
        self.pcapList_analysisManagerWindow.setObjectName("pcapList_analysisManagerWindow")
        self.gridLayout.addWidget(self.pcapList_analysisManagerWindow, 0, 0, 1, 1)
        self.pcapsTabWidget_analysisManagerWindow.addTab(pcap, self.scenariosList_analysisManagerWindow.selectedItems()[
            0].text(0))
        self.pcapList_analysisManagerWindow.headerItem().setText(0, "No.")
        self.pcapList_analysisManagerWindow.headerItem().setText(1, "Time")
        self.pcapList_analysisManagerWindow.headerItem().setText(2, "Source")
        self.pcapList_analysisManagerWindow.headerItem().setText(3, "Destination")
        self.pcapList_analysisManagerWindow.headerItem().setText(4, "Protocol")
        self.pcapList_analysisManagerWindow.headerItem().setText(5, "Length")
        self.pcapList_analysisManagerWindow.headerItem().setText(6, "Info")

        self.pcapsTabWidget_analysisManagerWindow.addTab(pcap, self.scenariosList_analysisManagerWindow.selectedItems()[
            0].text(0))
        # self.gridLayout.addWidget(self.pcapList_analysisManagerWindow, 0, 0, 1, 1)

        self.iterate_packets(self.test_capture, "",
                             self.scenariosList_analysisManagerWindow.selectedItems()[0].text(0))
        self.pcapsTabWidget_analysisManagerWindow.tabsClosable()

    def merge(self):
        #self.test_capture.create_merged_file()
        selected_pcaps = []
        merged_file, _ = QFileDialog.getSaveFileName(
        self.mergeButton_analysisManagerWindow, "Save pcap file", '', "pcap Files (*.pcap *.pcapng)")
        if merged_file:
            for i in range(self.scenariosList_analysisManagerWindow.topLevelItemCount()):
                top_item = self.scenariosList_analysisManagerWindow.topLevelItem(i)
                if top_item.checkState(0) == 2:
                    selected_pcaps.append(top_item.text(0))
            filename = merged_file.split('/')
            filename = filename[-1]
            filepath = merged_file.replace(filename, '')
            self.test_capture.merge_pcaps(merged_file, selected_pcaps, filename, filepath)
            self.show_pcap_list(self.test_capture)

    def browsePcapDir(self):
        dialog = QFileDialog()
        directory = dialog.getExistingDirectory(self.inputPcapsDirectory_analysisManagerWindow,
                                                'Select Pcaps Directory')

        if directory:
            self.inputPcapsDirectory_analysisManagerWindow.setText(directory)
            self.test_capture = Capture("", directory)
            add_pcaps(self.test_capture)
            self.show_pcap_list(self.test_capture)
