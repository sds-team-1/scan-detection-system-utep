
import os
import shutil
import platform
import pyshark
import collections
import matplotlib.pyplot as plt
import numpy as np
from Models.pcap import Pcap
class Capture:
    def __init__(self, name: str, parentPath:str) -> None:
        self.name = name
        self.pcaps = []
        self.mergeFilePath = None
        self.jsonFilePath = None
        self.path = os.path.join(parentPath, self.name)
        self.totalPackets = 0
        self.protocols = None
        self.create_folder()
        #self.create_merge_file()

    def add_pcap(self, new: Pcap) -> list:
        self.pcaps.append(new)
        #self.merge_pcaps()
        return self.pcaps

    def del_pcap(self, old:Pcap)-> list:
        self.pcaps.remove(old)
        if self.pcaps:
            self.merge_pcaps()
        os.remove(old.path)
        old.remove()
        return self.pcaps

    def merge_pcaps(self):
        pcap_paths = ""
        for pcap in self.pcaps:
            pcap_paths += pcap.path + " "
        if platform.system() == 'Windows':
            os.system('cd "C:\\Program Files\\Wireshark\\" & mergecap -w %s %s' % (self.mergeFilePath, pcap_paths))
        else:
            os.system('mergecap -w %s %s' % (self.mergeFilePath, pcap_paths))

    def create_folder(self)-> str:
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
        return self.path

    def create_merged_file(self):
        filename = self.name + ".pcap"
        path = os.path.join(self.path, filename)
        self.mergeFilePath = path
        fp = open(path, 'a')
        fp.close()

    def save(self, f)-> None:
        f.write('{"name": "%s", "totalPackets": %s, "pcaps": [' % (self.name, self.totalPackets))
        for a in self.pcaps:
            a.save(f)
            if a != self.pcaps[-1]:
                f.write(',')
        f.write(']}')
    def iterate_file(self, filter:str, file:Pcap):

        cap = pyshark.FileCapture(file.path, display_filter=filter ,
                                  only_summaries=True)
        pktlist= []
        file_list = []
        # for pkt in cap:
        #     pktlist.append(pkt.protocol)
        #     file_list.append(str(pkt.no))
        #     file_list.append(str(pkt.time))
        #     file_list.append(str(pkt.source))
        #     file_list.append(str(pkt.destination))
        #     file_list.append(str(pkt.protocol))
        #     file_list.append(str(pkt.length))
        #     file_list.append(str(pkt.info))


        # counter = collections.Counter(pktlist)
        #
        # plt.style.use('ggplot')
        # y_pos = np.arange(len(list(counter.keys())))
        # plt.bar(y_pos, list(counter.values()), align='center', alpha=0.5, color=['b', 'g', 'r', 'c', 'm'])
        # plt.xticks(y_pos, list(counter.keys()))
        # plt.ylabel("Frequency")
        # plt.xlabel("Protocol Name")
        # plt.savefig("ProtocolGraph.png")
        #plt.show()
        return cap






# test_pcap = pcap.Pcap("test_pcap.pcapng", "C:\\Users\\Luis\\Downloads\\", "test_pcap.pcapng")
# test_pcap.create_json_file()
# test_pcap.to_json()
# test_pcap_2 = pcap.Pcap("test_pcap_2.pcapng", "C:\\Users\\Luis\\Downloads\\", "test_pcap_2.pcapng")
# test_pcap.create_json_file()
# test_pcap.to_json()
# test_capture = Capture("scenario", "C:\\Users\\Luis\\Downloads\\")
# test_capture.add_pcap(test_pcap)
# test_capture.add_pcap(test_pcap_2)
# test_capture.create_merged_file()
# test_capture.merge_pcaps()
# test_capture.iterate_file("ip.src == 192.168.200.21")
