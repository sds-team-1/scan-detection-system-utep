import os
import string
import sys
import subprocess
from xml.etree.ElementTree import XML
from xml_test import XML_Creator
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
        self.vm_initial_string_command = f"VBoxManage guestcontrol \"{self.vm_name}\" --username \"{self.vm_username}\" --password \"{self.vm_password}\" "
        pass

    def run_command(self, command, args=""):
        # VBoxManage guestcontrol CoreUbuntu --username cj --password 1386 run /bin/ls  
        os.system(f"VBoxManage guestcontrol {self.vm_name} --username {self.vm_username} --password {self.vm_password} run {command} {args}")

    def core_cleanup(self):
        '''
        Runs CoreCleanup
        '''
        self.run_command("bin/sh", "/home/ubuntu/core/Files/CoreCleanup.sh")

    def core_start_from_xml_file_path(self, xml_file_path):
        '''
        Runs CoreStart
        '''
        # Copy the xml file to the VM
        self.copy_to(xml_file_path, "/home/ubuntu/core/Files/")
        # Get the xml file name
        xml_file_name = xml_file_path.split("/")[-1]
        # Run the command
        self.run_command("bin/sh", "/home/ubuntu/core/Files/CoreStart.sh /home/ubuntu/core/Files/" + xml_file_name)


    def core_start_from_xml_string(self, xml_as_string):
        '''
        Runs CoreStart using the xml as a string
        '''

        # Create a file with the xml
        xml_file_path = "topology.xml"


        # if the file exists delete it
        if os.path.exists(xml_file_path):
            os.remove(xml_file_path)
            
        # Create the file
        with open(xml_file_path, "w") as f:
            f.write(xml_as_string)

        # Copy the xml file to the VM
        xml_file_path = os.path.abspath(xml_file_path)
        self.copy_to(xml_file_path, "/home/ubuntu/core/Files/")


        # run cleanup script
        self.core_cleanup()

        # Run Core Start command
        self.core_start_from_xml_file_path(xml_file_path)

    def core_start_from_dictionary(self, topology_dict):
        '''
        Runs CoreStart using the json db format
        '''
        # TODO: figure out how the topology_dict is going to be received
        # # rename 'nodes' to 'devices'
        # topology_dict['devices'] = topology_dict['nodes']

        # print(topology_dict)

        # # Create the xml file\
        # xml = XML_Creator.XmlHelper(XML_Creator.XmlHelper.test_input)
        # xml.format_dict()
        # xml.create_xml_string()

        # Create the xml file
        xml_creator = XML_Creator(topology_dict)
        xml_as_string = xml_creator.create_xml()
        # Run Core Start command
        self.core_start_from_xml_string(xml_as_string)


    def start_services(self, scenario_dict: dict):
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

    def copy_to(self, host_file_path, guest_path):
        '''
        Copies the file given in host_file path
        and copies it to the guest path
        self: the CaptureController object
        host_file_path: the path of the file to copy
        guest_path: the path to copy the file to
        '''
        command = self.vm_initial_string_command + f"copyto --target-directory {guest_path} {host_file_path}"
        os.system(command)

    def copy_from(self, host_path, guest_file_path):
        '''
        Copies the file given in host_file path
        and copies it to the guest path
        '''
        command = self.vm_initial_string_command + f"copyfrom --target-directory {host_path} {guest_file_path}"
        os.system(command)



    def test_(self):
        xml = XML_Creator.XmlHelper(XML_Creator.test_input)
        xml.format_dict()
        xml.create_xml_string()
        xml_as_string = xml.get_xml_str()

        self.core_start_from_xml_string(xml_as_string)




# add logic in case the file is ran from the command line


if __name__ == "__main__":
    cc = CaptureController()

    if len(sys.argv) == 1:
        print("Please provide a command, use -h for help")
    elif sys.argv[1] == "core-cleanup":
        cc.core_cleanup()
    elif sys.argv[1] == "core-start":
        cc.core_start_from_xml_file_path()
    elif sys.argv[1] == "start-services":
        cc.start_services()
    elif sys.argv[1] == "start":
        cc.start_vm()
    elif sys.argv[1] == "stop":
        cc.stop_vm()
    elif sys.argv[1] == "test":
        cc.test_()
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
    elif sys.argv[1] == "copy-to":
        cc.copy_to("/Users/erikmtz/Documents/GitProjects/scan-detection-system-utep/test.txt", "/home/ubuntu/core/Files/")
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
