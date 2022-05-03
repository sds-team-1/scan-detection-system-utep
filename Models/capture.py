import os
import shutil
import platform
import pyshark
import collections
import matplotlib.pyplot as plt
import numpy as np
from Models.pcap import Pcap


class Capture:
    def __init__(self, name: str, parentPath: str) -> None:
        self.name = name
        self.pcaps = []
        self.mergeFilePath = None
        self.jsonFilePath = None
        self.path = os.path.join(parentPath, self.name)
        self.totalPackets = 0
        self.protocols = None
        self.create_folder()
        # self.create_merge_file()

    # adds pcap to pcap list
    def add_pcap(self, new: Pcap) -> list:
        self.pcaps.append(new)
        # self.merge_pcaps()
        return self.pcaps

    # removes pcap from pcaps list
    def del_pcap(self, pcapName) -> list:
        for pcap in self.pcaps:
            if pcap.name == pcapName:
                self.pcaps.remove(pcap)
        return self.pcaps

    # merges selected pcap files
    def merge_pcaps(self, merged_file, selected_pcaps, filename, filepath):
        pcap_paths = ""
        for pcap in self.pcaps:
            if pcap.name in selected_pcaps:
                pcap_paths += pcap.path + " "
        if platform.system() == 'Windows':
            os.system('cd "C:\\Program Files\\Wireshark\\" & mergecap -w %s %s' % (merged_file, pcap_paths))
        else:
            os.system('mergecap -w %s %s' % (merged_file, pcap_paths))

        new_pcap = Pcap(filename, filepath + "pcaps", filename)
        self.add_pcap(new_pcap)

    # creates folder
    def create_folder(self) -> str:
        if not os.path.isdir(self.path):
            os.mkdir(self.path)
        return self.path

    # creates initial new merged file
    def create_merged_file(self):
        filename = "merged_pcap" + ".pcap"
        path = os.path.join(self.path, filename)
        self.mergeFilePath = path
        fp = open(path, 'a')
        fp.close()

    # creates new pcap based on inputted display filter
    def save_filter_file(self, filter:str,name:str, new_name:str):
        if any(x.name == name for x in self.pcaps):
            print("reached here")
            cap = pyshark.FileCapture(self.path + name, display_filter=filter,
                                      output_file= new_name)
            cap.load_packets()
            cap.close()
            new_name = new_name.split('/')
            new_name = new_name[-1]
            new_pcap = Pcap(new_name, self.path + "pcaps", new_name)
            self.add_pcap(new_pcap)

    def iterate_file(self, filter: str, name: str):
        ''' Opens pcap and returns iterable object of packets'''
        if any(x.name == name for x in self.pcaps):
            cap = pyshark.FileCapture(self.path + name, display_filter=filter,
                                      only_summaries=True)
            return cap

