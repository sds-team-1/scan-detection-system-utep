# Method that checks if there is either a < or > in the args list
def hasRedirect(args): 
    if '<' in args or '>' in args:
        return True
    return False

# Method that determines if the redirect syntax is used correctly 
def isValid(args): 
    numIn = 0
    numOut = 0
    for i in range(len(args)):
        if args[i] == '<':
            numIn += 1
            
        if args[i] == '>':
            numOut +=1
            
        if (args[i] == '<' or args[i] == '<'):
            if(i+1 >= len(args)):
               return False
           
            elif(args[i+1] == '<' or args[i+1] == '<'):
                return False
        
    if numIn > 1 or numOut > 1:
        return False
    else:
        return True
    
# Method that determines if there is an input redirection
def hasInput(args): 
    if '<' in args:
        return True
    return False

# Method that determines if there is an Output redirection 
def hasOutput(args): 
    if '>' in args:
        return True
    return False 
    
# Method that returns the index of the Input redirect, -1 if none 
def input(args): 
    for i in range(len(args)):
        if args[i] == '<' and i+1 < len(args):
            return i+1
        else:
            return -1

# Method that returns the index of the Output redirect, -1 if none
def output(args): 
    for i in range(len(args)):
        if args[i] == '>' and i+1 < len(args):
            return i+1
        else:
            return -1
