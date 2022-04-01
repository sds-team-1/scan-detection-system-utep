import os
import string
import sys
import subprocess

'''
Temp notes
To run core cleanup
python3 captureController.py run "bin/sh" "/home/ubuntu/core/Files/CoreCleanup.sh"
To run core start
python3 captureController.py run "bin/sh" "/home/ubuntu/core/Files/CoreStart.sh"
To run services
python3 captureController.py run "bin/sh" "/home/ubuntu/core/Files/StartServices.sh"
'''

'''
TODO: Use enums to keep track of capture controller
'''
class CaptureController:


    def __init__(self):
        self.state = "stopped"
        self.vm_name = "LuisVM"
        self.vm_username = "ubuntu"
        self.vm_password = "ubuntu"
        pass

    def run_command(self, command, args=""):
        # VBoxManage guestcontrol CoreUbuntu --username cj --password 1386 run /bin/ls  
        os.system(f"VBoxManage guestcontrol {self.vm_name} --username {self.vm_username} --password {self.vm_password} run {command} {args}")

    def core_cleanup(self):
        '''
        Runs CoreCleanup
        '''
        self.run_command("bin/sh", "/home/ubuntu/core/Files/CoreCleanup.sh")
    
    def core_start(self):
        '''
        Runs CoreStart
        '''
        self.run_command("bin/sh", "/home/ubuntu/core/Files/CoreStart.sh /media/sf_new-shared-folder/research/xml-json-problem/julio_xml_test.xml")

    def start_services(self):
        '''
        Starts services on the VM
        This method also deletes everything in the PCAPs directory
        If it doesnt exists it will create it
        '''
        
        # Check if PCAPs folder exists, if not create it, if it does, delete everything in it
        if not os.path.exists("PCAPs"):
            os.makedirs("PCAPs")
        else:
            for the_file in os.listdir("PCAPs"):
                file_path = os.path.join("PCAPs", the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)

        self.run_command("bin/sh", "/home/ubuntu/core/Files/StartServices.sh /media/sf_new-shared-folder/PCAPs/capture.pcap");

    def start_vm(self) -> bool:
        '''
        Starts the VM with the name 'CoreUbuntu'
        Returns True if the VM was started successfully
        Returns False if the VM was already runnning
        '''
        print("Starting VM")

        if  self.state == "running":
            print("VM is already running")
            return False

        os.system(f"VBoxManage startvm \"{self.vm_name}\"")
        self.state = "running"

    def stop_vm(self) -> bool:
        '''
        Stops the VM with the name 'CoreUbuntu'
        Returns True if the VM was stopped successfully
        Returns False if the VM was already stopped
        '''
        print("Stopping VM")

        if self.state == "stopped":
            print("VM is already stopped")
            return False

        self.emergency_stop()
        self.state = "stopped"
        return

    def open_wireshark(path):
        os.system(f"wireshark -r /Users/erikmtz/Documents/GitProjects/scan-detection-system-utep/PCAPs/capture.pcap")

    def add_shared_folder(self, name, hostpath):
        os.system(f"VBoxManage sharedfolder add \"{self.vm_name}\" --name {name} --hostpath {hostpath} --automount")

    # def start_vm_headless(self):
    #     os.system(f"VBoxManage startvm \"{self.vm_name}\" --type headless")

    def emergency_stop(self):
        os.system(f"VBoxManage startvm \"{self.vm_name}\" --type emergencystop")

    def shutdown_vm(self):
        os.system(f"VBoxManage startvm \"{self.vm_name}\" --type shutdown")
    
    def restart_vm(self):
        # VBoxManage controlvm <vm> reset
        os.system(f"VBoxManage controlvm \"{self.vm_name}\" reset")





# add logic in case the file is ran from the command line


if __name__ == "__main__":
    cc = CaptureController()


    if len(sys.argv) == 1:
        print("Please provide a command, use -h for help")
    elif sys.argv[1] == "core-cleanup":
        cc.core_cleanup()
    elif sys.argv[1] == "core-start":
        cc.core_start()
    elif sys.argv[1] == "start-services":
        cc.start_services()
    elif sys.argv[1] == "start":
        cc.start_vm()
    elif sys.argv[1] == "stop":
        cc.stop_vm()
    elif sys.argv[1] == "open-wireshark":
        cc.open_wireshark()
    elif sys.argv[1] == "add-shared-folder":
        cc.add_shared_folder(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "emergency-stop":
        cc.emergency_stop()
    elif sys.argv[1] == "shutdown-vm":
        cc.shutdown_vm()
    elif sys.argv[1] == "restart-vm":
        cc.restart_vm()
    elif sys.argv[1] == "run":
        print("Attempting to run command: " + sys.argv[2])
        if len(sys.argv) == 3:
            cc.run_command(sys.argv[2])
        else:
            cc.run_command(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("""
        Usage:
        captureController.py [command] [args]
        Commands:
        core-cleanup
        core-start
        start-services
        start
        stop
        open-wireshark
        add-shared-folder
        run [command] [args]
        """)
    else:
        print("Command not recognized, please use -h or --help for help")
