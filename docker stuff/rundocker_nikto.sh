#!/bin/sh
VBoxManage startvm "vmname" --type headless
VBoxManage guestcontrol "vmname" --username ubuntu --password ubuntu 
VBoxManage guestcontrol "vmname" start --exe ".\start_nikto.sh"
