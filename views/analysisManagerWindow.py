import os
import platform as plat
import subprocess
from typing import Counter

# import qjsonmodel
import numpy as np
from Models.capture import Capture
from Models.pcap import Pcap
from PyQt5 import Qt, QtCore, QtWidgets
from PyQt5.QtWidgets import QAction, QFileDialog, QMessageBox, QTreeWidgetItem
from scapy.all import *

global counter
counter = 1

class Ui_AnalysisManagerWindow(object):


    def setupAnalysisManager(self, AnalysisManagerWindow, InitialWorkspaceWindow):

        # initialized values used by view
        self.InitialWorkspaceWindow = InitialWorkspaceWindow
        self.tabs_opened = []
        self.selected_pcaps = []
        self.tab_index = 0

        # Window attributes
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

        # Pcap Filee List
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

        self.centralSectionLayout_analysisManagerWindow.addLayout(self.scenariosLayout_analysisManagerWindow)

        self.gridLayout_2.addLayout(self.centralSectionLayout_analysisManagerWindow, 1, 0, 1, 1)

        # Export Button
        #self.exportButton_analysisManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
        #self.exportButton_analysisManagerWindow.setObjectName("exportButton_analysisManagerWindow")
        #self.buttonsLayout_analysisManagerWindow.addWidget(self.exportButton_analysisManagerWindow)

        # Pcaps Directory Line Edit
        self.layoutPcapsDirectory_analysisManagerWindow = QtWidgets.QHBoxLayout()
        self.layoutPcapsDirectory_analysisManagerWindow.setObjectName("layoutPcapsDirectory_analysisManagerWindow")
        
        # Merge Button
        self.mergeButton_analysisManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
        self.mergeButton_analysisManagerWindow.setObjectName("mergeButton_analysisManagerWindow")
        self.layoutPcapsDirectory_analysisManagerWindow.addWidget(self.mergeButton_analysisManagerWindow)
        
        self.inputPcapsDirectory_analysisManagerWindow = QtWidgets.QLineEdit(self.CentralLayout_analysisManagerWindow)
        self.inputPcapsDirectory_analysisManagerWindow.setObjectName("inputPcapsDirectory_analysisManagerWindow")
        self.layoutPcapsDirectory_analysisManagerWindow.addWidget(self.inputPcapsDirectory_analysisManagerWindow)

        # Browse Pcaps Button
        self.browsePcapsDirectory_analysisManagerWindow = QtWidgets.QPushButton(
            self.CentralLayout_analysisManagerWindow)
        self.browsePcapsDirectory_analysisManagerWindow.setObjectName("browsePcapsDirectory_analysisManagerWindow")
        self.layoutPcapsDirectory_analysisManagerWindow.addWidget(self.browsePcapsDirectory_analysisManagerWindow)
        
        # Close Analysis Manager Button
        self.closeAnalysisManager_analysisManagerWindow = QtWidgets.QPushButton(
        self.CentralLayout_analysisManagerWindow)
        self.closeAnalysisManager_analysisManagerWindow.setObjectName("closeAnalysisManager_analysisManagerWindow")
        self.layoutPcapsDirectory_analysisManagerWindow.addWidget(self.closeAnalysisManager_analysisManagerWindow)
        self.upperLayout_analysisManagerWindow.addLayout(self.layoutPcapsDirectory_analysisManagerWindow)

        self.gridLayout_2.addLayout(self.upperLayout_analysisManagerWindow, 0, 0, 1, 1)
        AnalysisManagerWindow.setCentralWidget(self.CentralLayout_analysisManagerWindow)
        self.closeAnalysisManager_analysisManagerWindow.clicked.connect(
            lambda: self.closeAnalysisManager(AnalysisManagerWindow))

        QtCore.QMetaObject.connectSlotsByName(AnalysisManagerWindow)

        # Setst title of window
        _translate = QtCore.QCoreApplication.translate
        AnalysisManagerWindow.setWindowTitle(
            _translate("AnalysisManagerWindow", "Scan Detection System - Analysis Manager"))
        self.pcapsList_analysisManagerWindow.headerItem().setText(0,
                                                                  _translate("AnalysisManagerWindow", "Pcap Files"))
        __sortingEnabled = self.pcapsList_analysisManagerWindow.isSortingEnabled()
        self.pcapsList_analysisManagerWindow.setSortingEnabled(False)
        self.pcapsList_analysisManagerWindow.setSortingEnabled(__sortingEnabled)

        # Sets text for buttons

        self.mergeButton_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "      Merge Pcaps      "))
        #self.exportButton_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "      Export Pcaps      "))
        self.browsePcapsDirectory_analysisManagerWindow.setText(_translate("AnalysisManagerWindow", "    Browse   "))
        self.closeAnalysisManager_analysisManagerWindow.setText(
            _translate("AnalysisManagerWindow", "Close Analysis Manager"))

        # Sets actions for buttons
        self.pcapsList_analysisManagerWindow.clicked.connect(self.selectedPcapCheckbox)
        self.pcapsList_analysisManagerWindow.doubleClicked.connect(lambda: self.open_tab(_translate))
        self.mergeButton_analysisManagerWindow.clicked.connect(lambda: self.merge())
        self.inputPcapsDirectory_analysisManagerWindow.setReadOnly(True)
        self.mergeButton_analysisManagerWindow.setEnabled(False)
        #self.exportButton_analysisManagerWindow.setEnabled(False)
        self.browsePcapsDirectory_analysisManagerWindow.clicked.connect(self.browsePcapDir)
        AnalysisManagerWindow.closeEvent = self.CloseEvent

        self.pcapsTabWidget_analysisManagerWindow.setTabsClosable(True)
        self.pcapsTabWidget_analysisManagerWindow.tabCloseRequested.connect(self.closeTab)
        self.pcapsList_analysisManagerWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pcapsList_analysisManagerWindow.customContextMenuRequested.connect(self.context_menu_pcaps)

    # closes analysis manager
    def closeAnalysisManager(self, AnalysisManagerWindow):
        AnalysisManagerWindow.close()
        self.InitialWorkspaceWindow.show()

    # reopens workspace window
    def CloseEvent(self, event):
        self.InitialWorkspaceWindow.show()

    # iterates through pcap file and returns packets
    def iterate_packets(self, capture, filter, pcap):
        try:
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
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("Opening Pcap")
            x = msg.exec_()

    #saves a new pcap file with the included display filter
    def save_filter(self, capture, filter, pcap):

        filtered_file, _ = QFileDialog.getSaveFileName(
            self.makeFilteredPcapButton_analysisManagerWindow, "Save pcap file", '', "pcap Files (*.pcap *.pcapng)")
        if filtered_file:
            # filename = filtered_file.split('/')
            # filename = filename[-1]
            # filepath = filtered_file.replace(filename, '')
            cap = capture.save_filter_file(filter, pcap, filtered_file)

            self.show_pcap_list(self.test_capture)

    # creates logic for buttons when pcaps are checked
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
            #self.exportButton_analysisManagerWindow.setEnabled(True)

        else:
            self.mergeButton_analysisManagerWindow.setEnabled(False)
            #self.exportButton_analysisManagerWindow.setEnabled(False)

    # creates logic for when packets are checked
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
            self.openInJsonButton_captureManagerWindow.setEnabled(True)

        else:
            self.openPacketWiresharkButton_captureManagerWindow.setEnabled(False)
            self.convertPacketsButton_captureManagerWindow.setEnabled(False)
            self.removePacketsButton_captureManagerWindow.setEnabled(False)
            self.openInJsonButton_captureManagerWindow.setEnabled(False)

    # Shows the pcaps in the capture
    def show_pcap_list(self, capture):
        self.pcapsList_analysisManagerWindow.clear()
        for pcap in capture.pcaps:
            x = QtWidgets.QTreeWidgetItem([pcap.name])
            x.setCheckState(0, QtCore.Qt.Unchecked)
            self.pcapsList_analysisManagerWindow.addTopLevelItem(x)

    # opens new tab based on double clicked pcap name in list
    def open_tab(self, _translate):

        # Opens new tab only if tab isnt already open
        if self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0) not in self.tabs_opened:
            self.selected_packets = []

            # New Tab
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

            # Apply Filter Button
            self.filtersButton_analysisManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
            self.filtersButton_analysisManagerWindow.setObjectName("filtersButton_analysisManagerWindow")
            self.filterPacketLayout_captureManagerWindow.addWidget(self.filtersButton_analysisManagerWindow)

            # Make Filtered Pcap Button
            self.makeFilteredPcapButton_analysisManagerWindow = QtWidgets.QPushButton(
                self.CentralLayout_analysisManagerWindow)
            self.makeFilteredPcapButton_analysisManagerWindow.setObjectName(
                "makeFilteredPcapButton_analysisManagerWindow")
            self.filterPacketLayout_captureManagerWindow.addWidget(self.makeFilteredPcapButton_analysisManagerWindow)

            self.gridLayout.addLayout(self.filterPacketLayout_captureManagerWindow, 0, 0, 1, 1)

            # table where packet info is located
            self.packetsList_analysisManagerWindow = QtWidgets.QTreeWidget()
            self.packetsList_analysisManagerWindow.setObjectName("packetsList_analysisManagerWindow")

            self.gridLayout.addWidget(self.packetsList_analysisManagerWindow, 1, 0, 1, 1)

            self.pcapsTabWidget_analysisManagerWindow.addTab(pcap, self.pcapsList_analysisManagerWindow.selectedItems()[
                0].text(0))

            # Sets table column names
            self.packetsList_analysisManagerWindow.headerItem().setText(0, "No.")
            self.packetsList_analysisManagerWindow.headerItem().setText(1, "Time")
            self.packetsList_analysisManagerWindow.headerItem().setText(2, "Source")
            self.packetsList_analysisManagerWindow.headerItem().setText(3, "Destination")
            self.packetsList_analysisManagerWindow.headerItem().setText(4, "Protocol")
            self.packetsList_analysisManagerWindow.headerItem().setText(5, "Length")
            self.packetsList_analysisManagerWindow.headerItem().setText(6, "Info")
            # self.packetsList_analysisManagerWindow.headerItem().setData()
            self.packetsList_analysisManagerWindow.setSortingEnabled(True)

            # Row of buttons
            self.buttonsPacketLayout_captureManagerWindow = QtWidgets.QHBoxLayout()
            self.buttonsPacketLayout_captureManagerWindow.setObjectName("buttonsPacketLayout_captureManagerWindow")

            # Open in Wireshark Button
            self.openPacketWiresharkButton_captureManagerWindow = QtWidgets.QPushButton(
            self.CentralLayout_analysisManagerWindow)
            self.openPacketWiresharkButton_captureManagerWindow.setObjectName(
                "openPacketWiresharkButton_captureManagerWindow")
            self.buttonsPacketLayout_captureManagerWindow.addWidget(self.openPacketWiresharkButton_captureManagerWindow)

            # Convert selected to new Pcap Button
            self.convertPacketsButton_captureManagerWindow = QtWidgets.QPushButton(
                self.CentralLayout_analysisManagerWindow)
            self.convertPacketsButton_captureManagerWindow.setObjectName("convertPacketsButton_captureManagerWindow")
            self.buttonsPacketLayout_captureManagerWindow.addWidget(self.convertPacketsButton_captureManagerWindow)

            # Open selected packets in Json Button
            self.openInJsonButton_captureManagerWindow = QtWidgets.QPushButton(self.CentralLayout_analysisManagerWindow)
            self.openInJsonButton_captureManagerWindow.setObjectName("openInJson_captureManagerWindow")
            self.buttonsPacketLayout_captureManagerWindow.addWidget(self.openInJsonButton_captureManagerWindow)

            # Remove selected packets Button
            self.removePacketsButton_captureManagerWindow = QtWidgets.QPushButton(
                self.CentralLayout_analysisManagerWindow)
            self.removePacketsButton_captureManagerWindow.setObjectName("removePacketsButton_captureManagerWindow")
            self.buttonsPacketLayout_captureManagerWindow.addWidget(self.removePacketsButton_captureManagerWindow)

            # Disables Row of buttons until there is a packet selected
            self.openPacketWiresharkButton_captureManagerWindow.setEnabled(False)
            self.convertPacketsButton_captureManagerWindow.setEnabled(False)
            self.removePacketsButton_captureManagerWindow.setEnabled(False)
            self.openInJsonButton_captureManagerWindow.setEnabled(False)

            self.gridLayout.addLayout(self.buttonsPacketLayout_captureManagerWindow, 2, 0, 1, 1)

            # Sets text for row of buttons
            self.openPacketWiresharkButton_captureManagerWindow.setText(
                _translate("AnalysisManagerWindow", "Open Selected in Wireshark"))
            self.convertPacketsButton_captureManagerWindow.setText(
                _translate("AnalysisManagerWindow", "New Pcap From Selected"))
            self.openInJsonButton_captureManagerWindow.setText(
                _translate("AnalysisManagerWindow", "Open Selected in Json"))
            self.removePacketsButton_captureManagerWindow.setText(
                _translate("AnalysisManagerWindow", "Remove Selected "))
            self.filtersButton_analysisManagerWindow.setToolTip(_translate("AnalysisManagerWindow", "New Project"))
            self.filtersButton_analysisManagerWindow.setText(
                _translate("AnalysisManagerWindow", "      Apply Filter      "))
            self.makeFilteredPcapButton_analysisManagerWindow.setText(
                _translate("AnalysisManagerWindow", "      New Pcap From Filter      "))

            self.pcapsTabWidget_analysisManagerWindow.addTab(pcap, self.pcapsList_analysisManagerWindow.selectedItems()[
                0].text(0))

            # reads the pcap
            self.iterate_packets(self.test_capture, "",
                                 self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0))

            self.pcapsTabWidget_analysisManagerWindow.setCurrentIndex(self.tab_index)


            # Sets actions of buttons when pressed
            self.packetsList_analysisManagerWindow.clicked.connect(self.selectedPacketCheckbox)

            self.filtersButton_analysisManagerWindow.clicked.connect(
                lambda: self.iterate_packets(self.test_capture, self.filterInput_analysisManagerWindow.text(),
                                             self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0)))
            self.makeFilteredPcapButton_analysisManagerWindow.clicked.connect(lambda: self.save_filter(
                self.test_capture, self.filterInput_analysisManagerWindow.text(), tab_name))
            self.openPacketWiresharkButton_captureManagerWindow.clicked.connect(
                lambda: self.openPacketWireshark(tab_name))
            self.convertPacketsButton_captureManagerWindow.clicked.connect(lambda: self.convertPackets(tab_name))
            self.removePacketsButton_captureManagerWindow.clicked.connect(
                lambda: self.removePackets(tab_name, self.packetsList_analysisManagerWindow))
            self.openInJsonButton_captureManagerWindow.clicked.connect(lambda: self.openPacketJson(tab_name))
            self.tab_index += 1

    # closes open pcap tab
    def closeTab(self, currentIndex):
        self.pcapsTabWidget_analysisManagerWindow.removeTab(currentIndex)
        del self.tabs_opened[currentIndex]
        self.tab_index -= 1

    # merges selected pcaps
    def merge(self):
        # self.test_capture.create_merged_file()
        merged_file, _ = QFileDialog.getSaveFileName(
            self.mergeButton_analysisManagerWindow, "Save pcap file", '', "pcap Files (*.pcap *.pcapng)")
        if merged_file:
            filename = merged_file.split('/')
            filename = filename[-1]
            filepath = merged_file.replace(filename, '')
            self.test_capture.merge_pcaps(merged_file, self.selected_pcaps, filename, filepath)
            self.show_pcap_list(self.test_capture)

    # takes user input to set the folder for reading pcaps
    def browsePcapDir(self):
        dialog = QFileDialog()
        directory = dialog.getExistingDirectory(self.inputPcapsDirectory_analysisManagerWindow,
                                                'Select Pcaps Directory')

        if directory:
            self.inputPcapsDirectory_analysisManagerWindow.setText(directory)
            self.test_capture = Capture("", directory)
            add_pcaps(self.test_capture)
            self.show_pcap_list(self.test_capture)

    # creates right click menu for pcaps
    def context_menu_pcaps(self, point):
        index = self.pcapsList_analysisManagerWindow.indexAt(point)
        if not index.isValid() or index.parent().isValid():
            return
        item = self.pcapsList_analysisManagerWindow.itemAt(point)
        name = item.text(0)
        menu = QtWidgets.QMenu()

        action_open_pcap = QAction("Open pcap in Wireshark")
        action_delete_pcap = QAction("Delete pcap")
        action_hier_stat = QAction("Protocol Stats")
        action_port_number = QAction("Port Number")
        action_statistics = QAction("Statistics Graph")
        action_toJson = QAction("Export To Json")

        menu.addAction(action_open_pcap)
        menu.addAction(action_delete_pcap)
        menu.addSeparator()
        menu.addAction(action_hier_stat)
        menu.addAction(action_port_number)
        menu.addAction(action_statistics)
        menu.addAction(action_toJson)

        action_open_pcap.triggered.connect(lambda: self.open_pcap_wireshark(name))
        action_delete_pcap.triggered.connect(lambda: self.delete_pcap(name))
        action_hier_stat.triggered.connect(lambda: self.hier_stat(name))
        action_port_number.triggered.connect(lambda: self.port_num(name))
        action_statistics.triggered.connect(lambda: self.show_statistics(name))
        action_toJson.triggered.connect(lambda: self.pcapToJson(name))


        menu.exec_(self.pcapsList_analysisManagerWindow.mapToGlobal(point))


    #creates context menu for packmets
    def context_menu_packets(self, point):
        index = self.packetsList_analysisManagerWindow.indexAt(point)
        if not index.isValid() or index.parent().isValid():
            return
        item = self.packetsList_analysisManagerWindow.itemAt(point)
        name = item.text(0)
        menu = QtWidgets.QMenu()

        action_port_number = QAction("Port Number")


      
        menu.addAction(action_port_number)


        action_port_number.triggered.connect(lambda: self.port_num(name))

        menu.exec_(self.packetsList_analysisManagerWindow.mapToGlobal(point))


    #deletes pcap from file system as well as pcaps list
    def delete_pcap(self, name):
        try:
            path = self.inputPcapsDirectory_analysisManagerWindow.text()
            # File name
            file = self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0)

            # File location
            location = self.inputPcapsDirectory_analysisManagerWindow.text()

            # Path
            path = os.path.join(location, file)

            # Remove the file
            self.test_capture.del_pcap(file)
            os.remove(path)


            print("%s has been removed successfully" %file)
            self.show_pcap_list(self.test_capture)
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Error Deleting File")
            x = msg.exec_()

    # retrieves statistics about ports form pcap file
    def port_num(self, name):
        # tshark -r pcap3.pcap -q -z conv,tcp -z conv,udp
        path = self.inputPcapsDirectory_analysisManagerWindow.text()
        output = subprocess.getoutput('cd %s && tshark -r %s -q -z conv,tcp -z conv,udp' % (path, self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0)))
        msg = QMessageBox()
        msg.setWindowTitle("Port Info")
        msg.setText(output)
        
        x = msg.exec_()

    # retrieves packet statistics for pcap file
    def hier_stat(self, name):

            path = self.inputPcapsDirectory_analysisManagerWindow.text()
            output = subprocess.getoutput('cd %s && tshark -r %s -q -z io,phs' % (
            path, self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0)))
            # print (output)
            # Modal PopUp
            msg = QMessageBox()
            msg.setWindowTitle("Hierarchy")
            msg.setText(output)
            x = msg.exec_()


    # opens selected pcap in wireshark
    def open_pcap_wireshark(self, name):
        for pcap in self.test_capture.pcaps:
            if pcap.name == name:
                subprocess.Popen(["wireshark", "-r", pcap.path])

    # shows procotol statitistic graph for the selected pcap
    def show_statistics(self, name):
        try:
            packets = ''
            temp_cap = ''
            i_open_file = ''

            for pcap in self.test_capture.pcaps:
                if pcap.name == name:
                    packets = self.test_capture.iterate_file('', pcap.name)
            pktlist = []
            file_list = []
            for pkt in packets:
                pktlist.append(pkt.protocol)
                file_list.append(str(pkt.no))
                file_list.append(str(pkt.time))
                file_list.append(str(pkt.source))
                file_list.append(str(pkt.destination))
                file_list.append(str(pkt.protocol))
                file_list.append(str(pkt.length))
                file_list.append(str(pkt.info))

            packets.close()
            counter = collections.Counter(pktlist)
            plt.title(name)
            plt.style.use('ggplot')
            y_pos = np.arange(len(list(counter.keys())))
            plt.bar(y_pos, list(counter.values()), align='center', alpha=0.5, color=['b', 'g', 'r', 'c', 'm'])
            plt.xticks(y_pos, list(counter.keys()))
            plt.ylabel("Frequency")
            plt.xlabel("Protocol Name")
            plt.savefig("ProtocolGraph.png")
            plt.show()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Cannot show statistics graph, please try again")
            x = msg.exec_()

    # exports selected pcap to a json file
    def pcapToJson(self, name):
        filtered_file, _ = QFileDialog.getSaveFileName(
            self.convertPacketsButton_captureManagerWindow, "Save pcap file", '', "json Files (*.json)")
        if filtered_file:
            print (self.test_capture.path + name)
            os.system('tshark -r %s -T json > %s' % (self.test_capture.path + name, filtered_file))

        pass

    # exports selected file to csv file ----------Not Working
    def pcapToCSV(self, name):
        filtered_file, _ = QFileDialog.getSaveFileName(
            self.convertPacketsButton_captureManagerWindow, "Save pcap file", '', "json Files (*.json)")
        if filtered_file:
            os.system('tshark -r %s -T json > %s' % (self.test_capture.path + name, filtered_file))
        pass

    # opens selected packets in wireshark
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

    # Opens selected packets in non modal json format ---------Not working
    def openPacketJson(self, name):
        # Gets the path of the two 
        path = self.inputPcapsDirectory_analysisManagerWindow.text()
        packets = ''
        temp_cap = ''
        i_open_file = ''
        # Temporary pcap file. Remove if there is already one
        if os.path.exists("%s\\temp_cap.pcap" % path):
            os.remove("%s\\temp_cap.pcap" % path)
        # Iterate through each loaded pcap model objects
        global counter
        counter += 1
        open_filename = f'{counter}.txt'
        for pcap in self.test_capture.pcaps:
            if pcap.name == name:
                packets = self.test_capture.iterate_file('', pcap.name)
                temp_cap = PcapWriter("%s\\temp_cap.pcap" % path, append=True)
                i_open_file = PcapReader(pcap.path)
                packet = i_open_file.read_packet()
        for p in packets:
            packet = i_open_file.read_packet()
            if str(p.no) in self.selected_packets:
                temp_cap.write(packet)
        # subprocess.Popen(["wireshark", "-r", "temp_cap.pcap"])
        output = subprocess.getoutput('cd %s && tshark -r %s -l -n -T json' % (
        path, self.pcapsList_analysisManagerWindow.selectedItems()[0].text(0)))
        f = open(open_filename, "w")
        f.write(output)
        f.close()
        packets.close()

        # Open with the right editor by OS. 
        the_os = plat.system()
        if the_os == 'Windows':
            os.system(f'{open_filename}')
        elif the_os == 'Darwin':
            os.system(f'open -a TextEdit {open_filename} &')
        else:
            os.system(f'gedit {open_filename} &')


    # Creates new pcap file based on the selected packets
    def convertPackets(self, name):

        filtered_file, _ = QFileDialog.getSaveFileName(
            self.convertPacketsButton_captureManagerWindow, "Save pcap file", '', "pcap Files (*.pcap *.pcapng)")
        if filtered_file:
            packets = ''
            temp_cap = ''
            i_open_file = ''
            index = 0
            for pcap in self.test_capture.pcaps:
                if pcap.name == name:
                    packets = self.test_capture.iterate_file('', pcap.name)
                    temp_cap = PcapWriter(filtered_file, append=True)
                    i_open_file = PcapReader(pcap.path)
            for p in packets:
                packet = i_open_file.read_packet()
                if str(p.no) in self.selected_packets:
                    temp_cap.write(packet)
            packets.close()
            filtered_file = filtered_file.split('/')
            filtered_file = filtered_file[-1]
            new_pcap = Pcap(filtered_file, self.test_capture.path, filtered_file)
            self.test_capture.add_pcap(new_pcap)

            self.show_pcap_list(self.test_capture)

    # Removes selected packets from pcap
    def removePackets(self, name, packets_list):
        packets = ''
        temp_cap = ''
        i_open_file = ''
        index = 0
        for pcap in self.test_capture.pcaps:
            if pcap.name == name:
                path = pcap.path.replace(pcap.name, "temp_cap.pcap")
                if os.path.exists(path):
                    os.remove(path)
                packets = self.test_capture.iterate_file('', pcap.name)
                path = pcap.path.replace(pcap.name, "temp_cap.pcap")
                temp_cap = PcapWriter(path, append=True)
                i_open_file = PcapReader(pcap.path)
                packet = i_open_file.read_packet()
            else:
                index += 1
        for p in packets:
            packet = i_open_file.read_packet()
            if str(p.no) not in self.selected_packets:
                temp_cap.write(packet)
        packets.close()
        temp_cap.close()
        i_open_file.close()
        path_new = path.replace("temp_cap.pcap", name)
        os.remove(path_new)
        os.rename(path, path_new)

        del self.test_capture.pcaps[index]

        new_pcap = Pcap(name, self.test_capture.path, name)
        self.test_capture.pcaps.insert(index, new_pcap)
        self.show_pcap_list(self.test_capture)
        self.browsePcapDir()

        while True:
            if self.check(packets_list) is True:
                break
    # Removes selected packets from GUI
    def check(self, packets_list):
        for i in range(packets_list.topLevelItemCount()):
            top_item = packets_list.topLevelItem(i)
            if top_item.checkState(0) == 2:
                packets_list.takeTopLevelItem(i)
                return False
        return True

def add_pcaps(capture):
    for filename in os.listdir(capture.path):
        f = os.path.join(capture.path, filename)
        if os.path.isfile(f):
            if '.pcap' in filename or '.pcapng' in filename:
                pcap = Pcap(filename, capture.path, filename)
                capture.add_pcap(pcap)
