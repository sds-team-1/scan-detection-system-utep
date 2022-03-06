
def hasPipe(args): # A method that checks if there is a | in the args list
    if '|' in args:
        return True
    return False

def isValid(args): 
    if args[0] == '|' or args[len(args) -1] == '|': 
        return False
    
    for i in range(len(args)):
        if(args[i] == '|'):
    
            if(i+1 >= len(args)): 
                return False
            
            if(args[i+1] == '|'): 
                return False
            
    return True 

# Splits the args list into the left and right of the pipe symbol
def getCommands(args): 
    for i in range(len(args)):
        if args[i] == "|":
            leftHS = args[0:i]
            rightHS = args[i+1:]
    return leftHS,rightHS

        
        

