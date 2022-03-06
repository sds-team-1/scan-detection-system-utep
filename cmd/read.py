from os import read

next = 0
limit = 0

# Method that calls read to fill a buffer, and gets one character at a time. 
def getChar():
    global next
    global limit
    
    if next == limit:
        next = 0
        limit = read(0,1000)
        
        if limit == 0:
            return None
        
    if next < len(limit) -1: # Check to make sure limit[next] wont go out of bounds. 
        c = chr(limit[next]) # convert from ascii to character 
        next +=1
        return c   
    else:
        return None

    
# Method that returns the next line obtained from file descriptor 0 as a String or an empty String if an EOF is reached.
    
def getLine():
    global next
    global limit
    line = ""
    char = getChar()
    while (char != '' and char != None): # Check to see if we have a character to append.
        line += char
        char = getChar()
    next = 0 # reset next and limit after we have have finished a line. 
    limit = 0
    return line
