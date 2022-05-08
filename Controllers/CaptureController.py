import os
import string
import time
import sys
import subprocess
from xml.etree.ElementTree import XML
from Helpers import XmlHelper
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
class CaptureControllerService:

    scenario_dict:dict = None

    def __init__(self):
        self.state = "stopped"
        self.vm_name = "UbuntuDefault"
        self.vm_username = "ubuntu"
        self.vm_password = "ubuntu"
        self.vm_initial_string_command = f"VBoxManage guestcontrol \"{self.vm_name}\" --username \"{self.vm_username}\" --password \"{self.vm_password}\" "
        pass

    def run_command(self, command, args=""):
        '''
        Runs the command in a new subprocess
        '''

        # Example commands
        # VBoxManage guestcontrol UbuntuDefault --username ubuntu --password ubuntu run "/bin/sh" "/home/ubuntu/core/Files/CoreStart.sh"
        # VBoxManage guestcontrol CoreUbuntu --username cj --password 1386 run /bin/ls  
        # VBoxManage guestcontrol UbuntuDefault --username ubuntu --password ubuntu run /bin/ls  

        # subprocess.call(f"VBoxManage guestcontrol {self.vm_name} --username {self.vm_username} --password {self.vm_password} run {command} {args}", shell=True)
        command_string = f"VBoxManage guestcontrol {self.vm_name} --username {self.vm_username} --password {self.vm_password} run {command} {args}"
        # subprocess.call(command_string, shell=True)
        
        subprocess.Popen(command_string, shell=True, close_fds=True)

    def run_command_using_name_username_password_command_and_args(self, vm_name, username, password, command, args=""):
        '''
        Runs the command in a new subprocess
        '''
        command_string = f'VBoxManage guestcontrol {vm_name} --username {username} --password {password} run "{command} {args}"'
        subprocess.Popen(command_string, shell=True, close_fds=True)
        
        # VBoxManage guestcontrol Scanner --username ubuntu --password ubuntu run nmap --system-dns 172.19.203.179"
    def start_vm_by_name(self, vm_name):
        '''
        Starts the vm by name
        '''
        command_string = f"VBoxManage startvm {vm_name}"
        subprocess.Popen(command_string, shell=True, close_fds=True)
    

    def core_cleanup(self):
        '''
        Runs the CoreCleanup.sh script
        '''
        print("Running CoreCleanup...")
        self.run_command("bin/sh", "/home/ubuntu/core/Files/CoreCleanup.sh")

        # self.copy_from("pcaps", "/tmp/pcaps/*")
        
        try:
            # get the nodes object from scneario dict
            nodes_array = self.scenario_dict["devices"]
            scenario_folder = self.scenario_dict["name"]
            print(f"scenarion_name {scenario_folder}")
            if not os.path.isdir(f"pcaps/{scenario_folder}"):
                os.mkdir(f"pcaps/{scenario_folder}")
            self.copy_from_recursive(f"pcaps/{scenario_folder}/", f"/tmp/pcaps/")

            #self.copy_from_recursive(f"pcaps/", f"/tmp/pcaps/")

                


        except Exception as e:
            print("Could not copy files")

        # TODO: Fix this to get all the pcap files, use the tmp directory as mentioned by Dr.Acosta
        # self.copy_from("pcaps", "/home/ubuntu/core/Files/pcaps/hello1.pcap")
        # self.copy_from("pcaps", "/home/ubuntu/core/Files/pcaps/hello2.pcap")

    def core_start(self):
        '''
        Runs CoreCleanup.sh the calls CoreStart.sh
        '''
        # Run Core Cleanup, a sleep will run for 10 seconds
        # self.core_cleanup()

                # get the sacnner node name
        if self.scenario_dict["networks"][0] is not None:
            external_vm_dictionary = self.scenario_dict["networks"][0]

        if external_vm_dictionary is not None:
            self.start_vm_by_name(external_vm_dictionary["name"])

        # Run the CoreStart.sh script
        self.run_command("bin/sh", "/home/ubuntu/core/Files/CoreStart.sh")

        # wait 15 seconds for the core to start
        for i in range(15):
            print("Waiting for core to start..." + str(i))
            time.sleep(1)

        self.run_command("bin/sh", "/home/ubuntu/core/Files/CopyServices.sh")

        # wait 5 seconds for the core to start
        for i in range(5):
            print("Waiting for core to start..." + str(i))
            time.sleep(1)


        try:
            external_vm_dictionary["vm_node_name"]
            # wait 10 seconds for the vm to start
            for i in range(30):
                print("Waiting for vm to start..." + str(i) + "/30")
                time.sleep(1)
        except Exception as e:
            print("No external vm")


        try:
            #  start the other vm
            if external_vm_dictionary is not None and external_vm_dictionary["vm_node_name"] is not None:
                print("Found vm dictionary")
                print(external_vm_dictionary)
                self.run_command_using_name_username_password_command_and_args(
                    external_vm_dictionary["vm_node_name"],
                    external_vm_dictionary["vm_node_username"],
                    external_vm_dictionary["vm_node_password"],
                    external_vm_dictionary["vm_binary_path"],
                    external_vm_dictionary["vm_args"]
                )
        except Exception as e:
            print("Could not start vm")

        # run the command to start the services





        # Decide wether we need to wait or not
        # # wait 15 seconds
        # for i in range(15):
        #     print(f"Waiting 15 seconds -> {i} seconds")
        #     time.sleep(1)



    def core_start_from_xml_file_path(self, xml_file_path):
        '''
        Runs copies the file provided to the VM and then calls core_start
        '''
        # # if vm is not running, return
        if self.state != "running":
            print("Cannot start, vm is not powered on")
            return
        
        # Copy the xml file to the VM
        self.copy_to(xml_file_path, "/home/ubuntu/core/Files/")

        # Run the command
        self.core_start()

    def core_start_from_xml_string(self, xml_as_string):
        '''
        Creates a file on the host machine then copies to vm
        Calls core_start
        '''

        # # if vm is not running, return
        if self.state != "running":
            print("Cannot start, vm is not powered on")
            return

        
        # Create a file name with the xml
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

        # Run Core Start command
        self.core_start()


    def core_start_from_dictionary(self, topology_dict):
        '''
        Converts the dictionary to xml string then calls core_start_from_xml_string
        Will return if the vm is not running
        '''

        # Store the dictionary
        self.scenario_dict = topology_dict

        # # if vm is not running, return
        if self.state != "running":
            print("Cannot start, vm is not powered on")
            return
    

        # if 'networks' key is not in the dict, set it to empty list
        if 'networks' not in topology_dict:
            topology_dict['networks'] = []

        xml = XmlHelper.XmlHelper(topology_dict)
            
        # Run Core Start command
        self.core_start_from_xml_string(xml.get_xml_str())


    def start_services(self):
        '''
        Starts services on the VM
        This method also deletes everything in the PCAPs directory
        If it doesnt exists it will create it
        '''
        
        print("THe services method has been ran, yet to be implemnted....")
        print("Scenario dict: ", self.scenario_dict)
        
        # Check if PCAPs folder exists, if not create it
        if not os.path.exists("pcaps"):
            os.makedirs("pcaps")

        # TODO: This is hardcoded, figure out how to do this dynamically
        # self.run_command("bin/sh", "/home/ubuntu/core/Files/StartServices.sh");
        # run this command sudo bash /home/ubuntu/core/Files/StartServices.sh hello1 hello2 0.0.0.0
        # self.run_command("bin/sh", "/home/ubuntu/core/Files/StartServices.sh hello1 hello2 0.0.0.0")

        # # wait 35 seconds
        # for i in range(30):
        #     print(f"Waiting 40 seconds -> {i} seconds")
        #     time.sleep(1)
        
        # self.core_cleanup()


        # TODO: Decide whether this to be ran during core cleanup or during core start services ends
        # A file will be generated called /home/ubuntu/core/Files/pcaps/pcap1.pcap
        # use copy_from and store on host machine
        # self.copy_from("/home/ubuntu/core/Files/pcaps/pcap1.pcap", "PCAPs")
        # self.copy_from("pcaps", "/home/ubuntu/core/Files/pcaps/hello1.pcap")
        # self.copy_from("pcaps", "/home/ubuntu/core/Files/pcaps/hello2.pcap")




    def start_vm(self) -> bool:
        '''
        Starts the VM with the name 'UbuntuDefault'
        Returns True if the VM was started successfully
        Returns False if the VM was already runnning
        '''
        print("Starting VM")

        if  self.state == "running":
            print("VM is already running")
            return False
        command_string = f"VBoxManage startvm {self.vm_name}"
        subprocess.Popen(command_string, shell=True, close_fds=True)
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

    # def start_vm_headless(self):
    #     os.system(f"VBoxManage startvm \"{self.vm_name}\" --type headless")

    def emergency_stop(self):
        os.system(f"VBoxManage startvm \"{self.vm_name}\" --type emergencystop")

    def shutdown_vm(self):
        # FIXME this doesnt work due to strange error with VBoxManage wtf is going on
        # os.system(f"VBoxManage startvm \"{self.vm_name}\" --type shutdown")
        # vboxmanage controlvm Ubuntu poweroff soft
        # use the above command to shutdown the VM
        print("Shutting down VM")
        command_string = f"VBoxManage controlvm {self.vm_name} poweroff soft"
        subprocess.Popen(command_string, shell=True, close_fds=True)
        self.state = "stopped"
    
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

    def copy_from_recursive(self, host_path, guest_file_path):
        '''
        Copies the file given in host_file path
        and copies it to the guest path
        '''

        # Use --R for recursive
        command = self.vm_initial_string_command + f"copyfrom -R --target-directory {host_path} {guest_file_path}"
        os.system(command)
