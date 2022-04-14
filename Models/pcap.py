import os
import shutil
import platform


class Pcap:

    def __init__(self, name: str, path: str, file: str, metadata="") -> None:
        try:
            self.name = name
            self.directory = path
            self.path = os.path.join(path, self.name) # joining directory with pcap file name
            self.pcap_file = file
            self.total_packets = 0
            self.protocols = {}
            self.metadata = metadata
            self.json_file = None
            #if not self.pcap_file == self.path:
            #    shutil.copy(self.pcap_file,self.path) # copy test input into directory
            #self.create_json_file()
            #self.to_json()

        except:
            print("Error when reading pcap file")
            self.name = None

    def create_json_file(self):
        filename = self.name + ".json"
        path = os.path.join(self.directory, filename)
        self.json_file = path
        fp = open(path, 'a')
        fp.close()

    def to_json(self):
        if platform.system() == 'Windows':
            os.system('cd "C:\\Program Files\\Wireshark" & tshark -r' + self.directory + self.pcap_file + ' -T json > ' + self.json_file)
        else:
            os.system('tshark -r' + self.pcap_file + ' -T json > ' + self.json_file)



    def remove(self) -> bool:
        return self.__del__()

    def __del__(self) -> bool:
       try:
           shutil.rmtree(self.path)
           return True
       except:
           return False


#test_pcap = Pcap("testing", "C:\\Users\\Luis\\Downloads\\", "200722_tcp_anon.pcapng")
#test_pcap.create_json_file()
#test_pcap.to_json()
#print(test_pcap.name)
#print(test_pcap.path)
#print(test_pcap.pcap_file)