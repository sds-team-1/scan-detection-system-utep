#! /usr/bin/env python3

import os,sys,re,redirect,pipe
#import subprocess
from commands import execCommand
from read import getLine

# Method to execute piping. Seperated to allow for multiple pipes 
def piping(args): 
    leftHS,rightHS = pipe.getCommands(args) 
    pr,pw = os.pipe() # Create pipe 

    rc = os.fork() # Fork off children 

    if rc < 0:
        os.write(2,("fork failed, returning %d\n" %rc).encode())
        sys.exit(1)

    elif rc == 0: # Child who will run command 1
        
        os.close(1)
        os.dup(pw)
        os.set_inheritable(1,True)
        
        for fd in (pr,pw):
            os.close(fd)
            
        for dir in re.split(":",os.environ['PATH']):
            program = "%s/%s" % (dir, leftHS[0])
            try:
                os.execve(program,leftHS,os.environ)
            except FileNotFoundError:
                pass
        if leftHS[0] not in cmds:
            os.write(2,(leftHS[0] + ":command not found \n").encode())
            sys.exit(1)
        
    else: # Child who will run command 2
        
        os.close(0)
        os.dup(pr)
        os.set_inheritable(0,True)
        
        for fd in (pr,pw): # Disconnect extra connections to pipe 
            os.close(fd)
            
        if pipe.hasPipe(rightHS): # More than one pipe
            piping(rightHS)
            
        for dir in re.split(":",os.environ['PATH']):
            program = "%s/%s" % (dir,rightHS[0])
            try:
                os.execve(program,rightHS,os.environ)
            except FileNotFoundError:
                pass
            
        os.write(2,(rightHS[0] + ":command not found \n").encode())
        sys.exit(1)
                
        
while(1):
    os.write(1, "SDS: ".encode())

    input = getLine()
    args = input.split()
    
    while len(input) == 0:
        os.write(1, "SDS: ".encode())
        input = getLine()
        args = input.split()
    
    if input.lower() == "quit": # Quit console
        os.write(2,("SDS Terminated!\n\n".encode()))
        sys.exit(1)
        
    cmds = ['help','new-workspace','choose-directory','new-project','max-scenarios','new-scenario','log-traffic', 'view-scenario']
    
    if args[0] in cmds:
            execCommand(args)

    else:
        if args[0] == "cd": 
            if len(args) == 1:
                os.chdir("..")
            else:
                os.chdir(args[1])
            continue 

        rc = os.fork()
        backgroundTask = True

        if '&' in args:
            backgroundTask = False
            args.remove('&')

        if rc < 0: #Command fails
            os.write(2,("Program terminated with exit code" + rc +"\n").encode())
            sys.exit(1)
            
        elif rc == 0: # Child process
            if(redirect.hasRedirect(args)):
                if(redirect.isValid(args)):
                    if(redirect.hasOutput(args)):
                        outputIndex = redirect.output(args)
                        os.close(1)
                        os.open(args[outputIndex],os.O_CREAT | os.O_WRONLY)
                        os.set_inheritable(1,True)
                        args.remove('>') 
                        args.remove(args[outputIndex]) 
                    
                    if(redirect.hasInput(args)): 
                        inputIndex = redirect.input(args)
                        os.close(0) 
                        os.open(args[inputIndex],os.O_RDONLY); 
                        os.set_inheritable(0,True)
                        args.remove('<') 
                        args.remove(args[inputIndex])
                else:
                    os.write(2,("Invalid Redirection Syntax \n".encode()))
                    sys.exit(1)
            
                for dir in re.split(":",os.environ['PATH']):
                    program = "%s/%s" % (dir, args[0])
                    try:
                        os.execve(program,args,os.environ)
                    except FileNotFoundError:
                        pass
                os.write(2,(args[0] + ":command not found \n").encode())
                sys.exit(1)

            # Check for Pipe    
            elif(pipe.hasPipe(args)):
                if(pipe.isValid(args)):
                    piping(args) 
                else:
                    os.write(2,("Invalid Pipe syntax").encode())
                    sys.exit(1)
            # No Pipes or Redirections     
            else: 
                for dir in re.split(":",os.environ['PATH']):
                    program = "%s/%s" % (dir,args[0])
                    try:
                        os.execve(program,args,os.environ)  
                    except FileNotFoundError:
                        pass
                os.write(2,(args[0] + ":command not found \n").encode())
                sys.exit(1)
                                    
        else:
            if backgroundTask:
                childPidCode = os.wait()
