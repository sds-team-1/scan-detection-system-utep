import pcap
import os
import shutil
import platform

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

    def add_pcap(self, new: pcap) -> list:
        self.pcaps.append(new)
        #self.merge_pcaps()
        return self.pcaps

    def del_pcap(self, old:pcap)-> list:
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


test_pcap = pcap.Pcap("test_pcap.pcapng", "C:\\Users\\Luis\\Downloads\\", "test_pcap.pcapng")
test_pcap.create_json_file()
test_pcap.to_json()
test_pcap_2 = pcap.Pcap("test_pcap_2.pcapng", "C:\\Users\\Luis\\Downloads\\", "test_pcap_2.pcapng")
test_pcap.create_json_file()
test_pcap.to_json()
test_capture = Capture("test scenario", "C:\\Users\\Luis\\Downloads\\")
test_capture.add_pcap(test_pcap)
test_capture.add_pcap(test_pcap_2)
test_capture.create_merged_file()
test_capture.merge_pcaps()