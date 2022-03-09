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
        print(e)

    return

if __name__ == "__main__":
    command = sys.argv[1]

    if command == "start":
        start_virtual_box(sys.argv[2])
    elif command == "-h":
        print("Usage: python virtual_box_tool.py <command> <vm_name>")
        print("Commands:")
        print("\tstart <vm_name> - Start Virtual Box")
        print("\t-h - Show this help")
    else:
        print("Unknown command, use -h for help")
