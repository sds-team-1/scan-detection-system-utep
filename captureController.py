import os

vimname = "ubuntu"


def startScenario():
    os.system(f"VBoxManage guestcontrol \"{vimname}\" run bash ~/core/Files/CoreStart")


def startService():
    os.system(f"VBoxManage guestcontrol \"{vimname}\" run bash ~/core/Files/StartServices")


def cleanup():
    os.system(f"VBoxManage guestcontrol \"{vimname}\" run core-cleanup")
    os.system(f"VBoxManage guestcontrol \"{vimname}\" run rm -r ~/core/Files/Captures/*")


def restoreScenario():
    cleanup()
    startScenario()
    startService()

def startVM():
    os.system(f"VBoxManage startvm \"{vimname}\"")

def startVM(virtual_machine_name):
    os.system(f"VBoxManage startvm \"{virtual_machine_name}\"")