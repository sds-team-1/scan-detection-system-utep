import execnet

class Functions:
    
    '''
    This method runs "python python27code/virtual_box_tool.py start <vm_name>" on the remote host.
    '''
    def call_python_version(Version, Module, Function, ArgumentList):
        gw = execnet.makegateway("popen//python=python%s" % Version)
        channel = gw.remote_exec("""
            import sys
            sys.path.insert(0, '../')
            print('test')
            from %s import %s as the_function
            channel.send(the_function(*channel.receive()))
        """ % (Module, Function))
        channel.send(ArgumentList)
        return channel.receive()

    def call_code_as_string():
        gw = execnet.makegateway("popen//python=python")
        channel = gw.remote_exec("""
            import virtualbox

            vbox = virtualbox.VirtualBox()
            session = virtualbox.Session()

            try:
                progress = vbox.find_machine(vm_name).launch_vm_process(session, "gui", [])
                progress.wait_for_completion()
            except Exception as e:
                print(e)

            channel.send(True)
        """)
        return channel.receive()