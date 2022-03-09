from .Python27Helper import Functions as python27_functions
import os

class VirtualBoxHelper:
    def start_virtual_box(vm_name):
        directory_path = os.getcwd()
        folder_name = os.path.basename(directory_path)
        print("Current folder is " + folder_name)
        python27_functions.call_python_version(
            "2.7",
            "py_27_virtual_box_tool",
            "start_virtual_box",
            [vm_name]
        )