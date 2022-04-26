from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import QTreeWidgetItem, QFileDialog, QAction, QMessageBox
import pyshark
import scapy
from scapy.utils import PcapWriter
from scapy.all import *
import os
import subprocess

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
        self.tabs_opened = []
        self.selected_pcaps = []
        self.tab_index = 0
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
        self.pcapsList_analysisManagerWindow = QtWidgets.QTreeWidget(self.CentralLayout_analysisManagerWindow)
        self.pcapsList_analysisManagerWindow.setMinimumSize(QtCore.QSize(220, 0))
        self.pcapsList_analysisManagerWindow.setMaximumSize(QtCore.QSize(220, 16777215))
        self.pcapsList_analysisManagerWindow.setObjectName("pcapsList_analysisManagerWindow")
        self.centralSectionLayout_analysisManagerWindow.addWidget(self.pcapsList_analysisManagerWindow)
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
        self.upperLayout_analysisManagerWindow.addLayout(self.layoutPcapsDirectory_analysisManagerWindow)

        self.gridLayout_2.addLayout(self.upperLayout_analysisManagerWindow, 0, 0, 1, 1)
        AnalysisManagerWindow.setCentralWidget(self.CentralLayout_analysisManagerWindow)
        self.closeAnalysisManager_analysisManagerWindow.clicked.connect(
            lambda: self.closeAnalysisManager(AnalysisManagerWindow))

        QtCore.QMetaObject.connectSlotsByName(AnalysisManagerWindow)

        _translate = QtCore.QCoreApplication.translate
        AnalysisManagerWindow.setWindowTitle(
            _translate("AnalysisManagerWindow", "Scan Detection System - Analysis Manager"))
        self.pcapsList_analysisManagerWindow.headerItem().setText(0,
                                                                      _translate("AnalysisManagerWindow", "Pcap Files"))
        __sortingEnabled = self.pcapsList_analysisManagerWindow.isSortingEnabled()
        self.pcapsList_analysisManagerWindow.setSortingEnabled(False)
        self.pcapsList_analysisManagerWindow.setSortingEnabled(__sortingEnabled)
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
        self.mergeButton_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "      Merge Pcaps      "))
        self.exportButton_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "      Export Pcaps      "))
        self.browsePcapsDirectory_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "    Browse   "))
        self.closeAnalysisManager_analysisManagerWindow.setText(
            _translate("AnalysisManagerWindow", "Close Analysis Manager"))

        self.pcapsList_analysisManagerWindow.clicked.connect(self.selectedPcapCheckbox)

        self.pcapsList_analysisManagerWindow.doubleClicked.connect(lambda: self.open_tab(_translate))

        self.mergeButton_analysisManagerWindow.clicked.connect(lambda: self.merge())

        self.inputPcapsDirectory_analysisManagerWindow.setReadOnly(True)

        self.mergeButton_analysisManagerWindow.setEnabled(False)
        self.exportButton_analysisManagerWindow.setEnabled(False)

        self.browsePcapsDirectory_analysisManagerWindow.clicked.connect(self.browsePcapDir)

        AnalysisManagerWindow.closeEvent = self.CloseEvent

        self.pcapsTabWidget_analysisManagerWindow.setTabsClosable(True)
        self.pcapsTabWidget_analysisManagerWindow.tabCloseRequested.connect(self.closeTab)

        self.pcapsList_analysisManagerWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pcapsList_analysisManagerWindow.customContextMenuRequested.connect(self.context_menu_pcaps)


    def closeAnalysisManager(self, AnalysisManagerWindow):
        AnalysisManagerWindow.close()
        self.InitialWorkspaceWindow.show()


    def CloseEvent(self, event):
        self.InitialWorkspaceWindow.show()


    def iterate_packets(self, capture, filter, pcap):
        self.packetsList_analysisManagerWindow.clear()
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
            l1.setCheckState(0, QtCore.Qt.Unchecked)
            self.packetsList_analysisManagerWindow.addTopLevelItem(l1)
        packets.close()


    def selectedPcapCheckbox(self):
        checked = 0

        for i in range(self.pcapsList_analysisManagerWindow.topLevelItemCount()):
            top_item = self.pcapsList_analysisManagerWindow.topLevelItem(i)
            if top_item.checkState(0) == 2:
                checked += 1
                if top_item.text(0) not in self.selected_pcaps:
                    self.selected_pcaps.append(top_item.text(0))
            if top_item.checkState(0) == 0 and top_item.text(0) in self.selected_pcaps:
                self.selected_pcaps.remove(top_item.text(0))

        if checked > 1:
            self.mergeButton_analysisManagerWindow.setEnabled(True)
            self.exportButton_analysisManagerWindow.setEnabled(True)

        else:
            self.mergeButton_analysisManagerWindow.setEnabled(False)
            self.exportButton_analysisManagerWindow.setEnabled(False)


    def selectedPacketCheckbox(self):
        checked = 0

        for i in range(self.packetsList_analysisManagerWindow.topLevelItemCount()):
            top_item = self.packetsList_analysisManagerWindow.topLevelItem(i)
            if top_item.checkState(0) == 2:
                checked += 1
                if top_item.text(0) not in self.selected_packets:
                    self.selected_packets.append(top_item.text(0))
            if top_item.checkState(0) == 0 and top_item.text(0) in self.selected_packets:
                self.selected_packets.remove(top_item.text(0))

        if checked > 0:
            self.openPacketWiresharkButton_captureManagerWindow.setEnabled(True)
            self.convertPacketsButton_captureManagerWindow.setEnabled(True)
            self.removePacketsButton_captureManagerWindow.setEnabled(True)

        else:
            self.openPacketWiresharkButton_captureManagerWindow.setEnabled(False)
            self.convertPacketsButton_captureManagerWindow.setEnabled(False)
            self.removePacketsButton_captureManagerWindow.setEnabled(False)

    def show_pcap_list(self, capture):
        self.pcapsList_analysisManagerWindow.clear()
        for pcap in capture.pcaps:
            x = QtWidgets.QTreeWidgetItem([pcap.name])
            x.setCheckState(0, QtCore.Qt.Unchecked)
            self.pcapsList_analysisManagerWindow.addTopLevelItem(x)

    def open_tab(self, _translate):
        if self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0) not in self.tabs_opened:
            self.selected_packets = []
            tab_name = self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0)
            self.tabs_opened.append(self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0))
            pcap = QtWidgets.QWidget()
            pcap.setObjectName(self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0))

            self.gridLayout = QtWidgets.QGridLayout(pcap)
            self.gridLayout.setObjectName("gridLayout")

            self.filterPacketLayout_captureManagerWindow = QtWidgets.QHBoxLayout()
            self.filterPacketLayout_captureManagerWindow.setObjectName("filterPacketLayout_captureManagerWindow")

            self.filterInput_analysisManagerWindow = QtWidgets.QLineEdit(self.CentralLayout_analysisManagerWindow)
            self.filterInput_analysisManagerWindow.setObjectName("filterInput_analysisManagerWindow")
            self.filterPacketLayout_captureManagerWindow.addWidget(self.filterInput_analysisManagerWindow)
            self.filtersButton_analysisManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
            self.filtersButton_analysisManagerWindow.setObjectName("filtersButton_analysisManagerWindow")
            self.filterPacketLayout_captureManagerWindow.addWidget(self.filtersButton_analysisManagerWindow)
            self.gridLayout.addLayout(self.filterPacketLayout_captureManagerWindow, 0, 0, 1, 1)


            self.packetsList_analysisManagerWindow = QtWidgets.QTreeWidget()
            self.packetsList_analysisManagerWindow.setObjectName("packetsList_analysisManagerWindow")
            self.gridLayout.addWidget(self.packetsList_analysisManagerWindow, 1, 0, 1, 1)
            self.pcapsTabWidget_analysisManagerWindow.addTab(pcap, self.pcapsList_analysisManagerWindow.selectedItems()[
                0].text(0))
            self.packetsList_analysisManagerWindow.headerItem().setText(0, "No.")
            self.packetsList_analysisManagerWindow.headerItem().setText(1, "Time")
            self.packetsList_analysisManagerWindow.headerItem().setText(2, "Source")
            self.packetsList_analysisManagerWindow.headerItem().setText(3, "Destination")
            self.packetsList_analysisManagerWindow.headerItem().setText(4, "Protocol")
            self.packetsList_analysisManagerWindow.headerItem().setText(5, "Length")
            self.packetsList_analysisManagerWindow.headerItem().setText(6, "Info")

            self.buttonsPacketLayout_captureManagerWindow = QtWidgets.QHBoxLayout()
            self.buttonsPacketLayout_captureManagerWindow.setObjectName("buttonsPacketLayout_captureManagerWindow")

            self.openPacketWiresharkButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
            self.openPacketWiresharkButton_captureManagerWindow.setObjectName("openPacketWiresharkButton_captureManagerWindow")
            self.buttonsPacketLayout_captureManagerWindow.addWidget(self.openPacketWiresharkButton_captureManagerWindow)

            self.convertPacketsButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
            self.convertPacketsButton_captureManagerWindow.setObjectName("convertPacketsButton_captureManagerWindow")
            self.buttonsPacketLayout_captureManagerWindow.addWidget(self.convertPacketsButton_captureManagerWindow)

            self.removePacketsButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
            self.removePacketsButton_captureManagerWindow.setObjectName("removePacketsButton_captureManagerWindow")
            self.buttonsPacketLayout_captureManagerWindow.addWidget(self.removePacketsButton_captureManagerWindow)

            self.openPacketWiresharkButton_captureManagerWindow.setEnabled(False)
            self.convertPacketsButton_captureManagerWindow.setEnabled(False)
            self.removePacketsButton_captureManagerWindow.setEnabled(False)

            self.gridLayout.addLayout(self.buttonsPacketLayout_captureManagerWindow, 2, 0, 1, 1)

            self.openPacketWiresharkButton_captureManagerWindow.setText(_translate("AnalysisManagerWindow", "Open Selected Packets in Wireshark"))
            self.convertPacketsButton_captureManagerWindow.setText(_translate("AnalysisManagerWindow", "Convert Selected Packets"))
            self.removePacketsButton_captureManagerWindow.setText(_translate("AnalysisManagerWindow", "Remove Selected Packets"))
            self.filtersButton_analysisManagerWindow.setToolTip(_translate("AnalysisManagerWindow", "New Project"))
            self.filtersButton_analysisManagerWindow.setText(
            _translate("AnalysisManagerWindow", "      Apply Filter      "))

            self.pcapsTabWidget_analysisManagerWindow.addTab(pcap, self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0))

            self.iterate_packets(self.test_capture, "",
                                self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0))


            self.pcapsTabWidget_analysisManagerWindow.setCurrentIndex(self.tab_index)

            self.packetsList_analysisManagerWindow.clicked.connect(self.selectedPacketCheckbox)

            self.filtersButton_analysisManagerWindow.clicked.connect(
            lambda: self.iterate_packets(self.test_capture, self.filterInput_analysisManagerWindow.text(),
                                         self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0)))

            self.openPacketWiresharkButton_captureManagerWindow.clicked.connect(lambda: self.openPacketWireshark(tab_name))
            self.convertPacketsButton_captureManagerWindow.clicked.connect(self.convertPackets)
            self.removePacketsButton_captureManagerWindow.clicked.connect(lambda: self.removePackets(tab_name, self.packetsList_analysisManagerWindow))

            self.tab_index += 1
                                

    def closeTab(self, currentIndex):
        self.pcapsTabWidget_analysisManagerWindow.removeTab(currentIndex)
        del self.tabs_opened[currentIndex]
        self.tab_index -= 1

    def merge(self):
        #self.test_capture.create_merged_file()
        merged_file, _ = QFileDialog.getSaveFileName(
        self.mergeButton_analysisManagerWindow, "Save pcap file", '', "pcap Files (*.pcap *.pcapng)")
        if merged_file:
            filename = merged_file.split('/')
            filename = filename[-1]
            filepath = merged_file.replace(filename, '')
            self.test_capture.merge_pcaps(merged_file, self.selected_pcaps, filename, filepath)
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


    def context_menu_pcaps(self, point):
        index = self.pcapsList_analysisManagerWindow.indexAt(point)
        if not index.isValid() or index.parent().isValid():
            return
        item = self.pcapsList_analysisManagerWindow.itemAt(point)
        name = item.text(0)
        menu = QtWidgets.QMenu()

        action_open_pcap = QAction("Open pcap in Wireshark")
        action_rename_pcap = QAction("Rename pcap")
        action_delete_pcap = QAction("Delete pcap")
        action_hier_stat = QAction("Protocol Stats")

        menu.addAction(action_open_pcap)
        menu.addAction(action_rename_pcap)
        menu.addAction(action_delete_pcap)
        menu.addAction(action_hier_stat)

        action_open_pcap.triggered.connect(lambda: self.open_pcap_wireshark(name))
        action_rename_pcap.triggered.connect(lambda: self.rename_pcap(name))
        action_delete_pcap.triggered.connect(lambda: self.delete_pcap(name))
        action_hier_stat.triggered.connect(lambda: self.hier_stat(name))

        menu.exec_(self.pcapsList_analysisManagerWindow.mapToGlobal(point))


    # # TODO: Implement
    # def rename_pcap(self, name):
    #     pass


    # # TODO: Implement
    # def delete_pcap(self, name):
    #     pass

    def hier_stat(self, name):
        print ("Wazzup")
        #os.system('cd "C:\\Program Files\\Wireshark\\" & tshark -r pcap1.pcap -q -z io,phs')
        os.system('cd "C:\\Program Files\\Wireshark\\" & tshark -r %s -z io,phs' % (self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0)))


    def open_pcap_wireshark(self, name):
        for pcap in self.test_capture.pcaps:
            if pcap.name == name:
                subprocess.Popen(["wireshark", "-r", pcap.path])

    def openPacketWireshark(self, name):
        packets = ''
        temp_cap = ''
        i_open_file = ''
        if os.path.exists("temp_cap.pcap"):
            os.remove("temp_cap.pcap")
        for pcap in self.test_capture.pcaps:
            if pcap.name == name:
                packets = self.test_capture.iterate_file('', pcap.name)
                temp_cap = PcapWriter("temp_cap.pcap", append=True)
                i_open_file = PcapReader(pcap.path)
                packet = i_open_file.read_packet()
        for p in packets:
            packet = i_open_file.read_packet()
            if str(p.no) in self.selected_packets:
                temp_cap.write(packet)
        subprocess.Popen(["wireshark", "-r", "temp_cap.pcap"])
        packets.close()

    def convertPackets(self):
        pass

    def removePackets(self, name, packets_list):
        packets = ''
        temp_cap = ''
        i_open_file = ''
        index = 0 
        for pcap in self.test_capture.pcaps:
            if pcap.name == name:
                path = pcap.path.replace(pcap.name,"temp_cap.pcap")
                if os.path.exists(path):
                    os.remove(path)
                packets = self.test_capture.iterate_file('', pcap.name)
                path = pcap.path.replace(pcap.name, "temp_cap.pcap")
                temp_cap = PcapWriter(path, append=True)
                i_open_file = PcapReader(pcap.path)
                packet = i_open_file.read_packet()
                break
            else:
                index += 1
        for p in packets:
            packet = i_open_file.read_packet()
            if str(p.no) not in self.selected_packets:
                temp_cap.write(packet)
        packets.close()
        path_new = path.replace("temp_cap.pcap", name)
        os.remove(path_new)
        os.rename(path, path_new)

        del self.test_capture.pcaps[index]

        new_pcap = Pcap(name, self.test_capture.path, name)
        self.test_capture.pcaps.insert(index, new_pcap)

        while True:
            if self.check(packets_list) is True:
                break
            
    def check(self, packets_list):
        for i in range(packets_list.topLevelItemCount()):
            top_item = packets_list.topLevelItem(i)
            if top_item.checkState(0) == 2:
                packets_list.takeTopLevelItem(i)
                return False
        return True
                