#     cmds = ['help','new-workspace','choose-directory','new-project','max-scenarios','new-scenario','log-traffic', 'view-scenario']

def execCommand(command):
    check = len(command) > 1
    if command[0] == 'help':
        print("\n\
                              SDS HELP\n\
**********************************************************************\n\n\
command: [command] [attribute]\n\n\
run: Runs an instance of care using the the given file name.\n\n\
new-workspace [workspace name]: Create a new worksapce.\n\n\
choose-directory [directory]: Choose desired location of the workspace\n\n\
new-project [project name]: Closes the current SDS session.\n\n\
max-scenarios [int]: Closes the current SDS session.\n\n\
log-traffic [on/off]: Option to log traffic (on or off).\n\n\
view-scenario: Prints all nodes and scenario attributes.\n\n\
quit: Closes the current SDS session.\n\n\
help: Prints help dialog.\n")
        
    elif command[0] == 'new-workspace' and check is True:
        print('Command Selected: ', command[0], '\nAttribute Selected: ', command[1])
    elif command[0] == 'choose-directory' and check is True:
        print('Command Selected: ', command[0], '\nAttribute Selected: ', command[1])
    elif command[0] == 'new-project' and check is True:
        print('Command Selected: ', command[0], '\nAttribute Selected: ', command[1])
    elif command[0] == 'max-scenarios' and check is True:
        print('Command Selected: ', command[0], '\nAttribute Selected: ', command[1])
    elif command[0] == 'new-scenario' and check is True:
        print('Command Selected: ', command[0], '\nAttribute Selected: ', command[1])
    elif command[0] == 'log-traffic' and check is True:
        print('Command Selected: ', command[0], '\nAttribute Selected: ', command[1])
    elif command[0] == 'view-scenario':
        print('Command Selected: ', command[0])
    else:
        print("Invalid Attribute")
        