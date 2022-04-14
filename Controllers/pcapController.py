import pyshark

class PcapController:
    def __init__(self):
        pass

    def read_pcap(self,path):

        return pyshark.FileCapture(path)

    def apply_filter(self,path,filter):
        return pyshark.FileCapture(path, display_filter=filter)
    def merge_pcap(self):
        return
    def to_json(self):
        return