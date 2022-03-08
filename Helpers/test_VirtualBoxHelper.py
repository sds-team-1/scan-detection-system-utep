import virtualbox
print("TESTING")
vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
print("TESTING")
machine = vbox.find_machine("ubuntu")
progress = machine.launch_vm_process(session, "gui", []);
print("TESTING")
progress.wait_for_completion()