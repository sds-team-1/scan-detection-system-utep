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