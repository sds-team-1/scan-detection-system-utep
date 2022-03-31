import os
import sys

vimname = "CoreUbuntu"
vim_username = "cj"
vim_password = "1386"


'''
TODO: Use enums to keep track of capture controller
'''

class CaptureController:

    state = "stopped"

    def __init__(self):
        pass

    def startScenario(self):
        '''
        Runs the 'run bash ~/core/Files/CoreStart' this should cause a merge conflict
        '''
        os.system(f"VBoxManage guestcontrol run --username \"{vim_username}\" --password \"{vim_password}\" bash ~/core/Files/CoreStart")


    def startService(self):
        '''
        Runs the 'run bash ~/core/Files/StartServices' command on the VM
        '''
        os.system(f"VBoxManage guestcontrol \"{vimname}\" run --username \"{vim_username}\" --password \"{vim_password}\" bash ~/core/Files/StartServices")


    def cleanup(self):
        '''
        Runs the 'core-cleanup' command on the VM
        and the
        'rm -r ~/core/Files/Captures/*' command on the VM
        '''
        os.system(f"VBoxManage guestcontrol \"{vimname}\" run --username \"{vim_username}\" --password \"{vim_password}\" core-cleanup")
        os.system(f"VBoxManage guestcontrol run --username \"{vim_username}\" --password \"{vim_password}\" rm -r ~/core/Files/Captures/*")


    def run_command(self, command, args=""):
        # VBoxManage guestcontrol CoreUbuntu --username cj --password 1386 run /bin/ls  
        os.system(f"VBoxManage guestcontrol \"{vimname}\" --username \"{vim_username}\" --password \"{vim_password}\" run \"{command}\" {args}")

    def run_scenario(self, xml_as_string):
        '''
        Receives an xml string and runs the commands in the scenario
        '''
        pass

    def add_shared_folder(self, name, hostpath):
        os.system(f"VBoxManage sharedfolder add \"{vimname}\" --name {name} --hostpath {hostpath} --automount")

    def startVM(self) -> bool:
        '''
        Starts the VM with the name 'CoreUbuntu'
        Returns True if the VM was started successfully
        Returns False if the VM was already runnning
        '''
        print("Starting VM")

        if  self.state == "running":
            print("VM is already running")
            return False

        os.system(f"VBoxManage startvm \"{vimname}\"")
        state = "running"
        return True

        
    def stopVM(self) -> bool:
        '''
        Stops the VM with the name 'CoreUbuntu'
        Returns True if the VM was stopped successfully
        Returns False if the VM was already stopped
        '''
        print("Stopping VM")

        if self.state == "stopped":
            print("VM is already stopped")
            return False

        '''
        TODO: finish this
        '''
        
        pass
    
    def restoreScenario(self):
        '''
        Runs commands that allows virtual machine to transition to ready state to run scenario
        '''
        print("Restoring Scenario")
        # cleanup()
        # startScenario()
        # startService()
        pass


    
    def startVMHeadless(self):
        os.system(f"VBoxManage startvm \"{vimname}\" --type headless")

    def emergency_stop(self):
        os.system(f"VBoxManage startvm \"{vimname}\workspace_collection --type emergencystop")


    # add logic in case the file is ran from the command line
    if __name__ == "__main__":
        if len(sys.argv) == 1:
            print("Please provide a command, use -h for help")
        elif sys.argv[1] == "start":
            startVM()
        elif sys.argv[1] == "start-headless":
            startVMHeadless()
        elif sys.argv[1] == "start-scenario":
            startScenario()
        elif sys.argv[1] == "start-service":
            startService()
        elif sys.argv[1] == "cleanup":
            cleanup()
        elif sys.argv[1] == "restore":
            restoreScenario()
        elif sys.argv[1] == "emergency-stop":
            emergency_stop()
        elif sys.argv[1] == "add-shared-folder":
            add_shared_folder(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "run":
            print("Attempting to run command: " + sys.argv[2])
            if len(sys.argv) == 3:
                run_command(sys.argv[2])
            else:
                run_command(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print("""
            Usage:
            start-scenario - starts the scenario
            start-service - starts the services
            cleanup - cleans up the scenario
            restore - restores the scenario
            """)
        else:
            print("Command not recognized, please use -h or --help for help")
