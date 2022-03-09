import virtualbox

def start_virtual_box(vm_name):
    vbox = virtualbox.VirtualBox()
    session = virtualbox.Session()

    try:
        print("Attempting to start Virtual Box")
        progress = vbox.find_machine(vm_name).launch_vm_process(session, "gui", [])
        progress.wait_for_completion()
        print("Virtual Box started!")
    except Exception as e:
        print("Virtual Box already running")