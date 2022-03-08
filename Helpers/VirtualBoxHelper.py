import virtualbox

class VirtualBoxInstance:
    def __init__(self):
        print("Starting virtual box helper")

    def start(self):
        print("Starting virtual box")
        self.vbox = virtualbox.VirtualBox()
        print("Virtual box started")

    def stop(self):
        print("Stopping virtual box")
        self.vbox.close()
        print("Virtual box stopped")
