import virtualbox
vbox = virtualbox.VirtualBox()
session = virtualbox.Session()

print("Searching for machines")
for machine_name in vbox.machines:
    print(machine_name)

# this machine name input must be the same as the name you give it in virtualbox
machine = vbox.find_machine("ubuntu")
try:
    print("Starting machine")
    progress = machine.launch_vm_process(session, "gui", [])
    progress.wait_for_completion()
except Exception as e:
    print("Virtual machine already running")
