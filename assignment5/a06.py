## IMPORTS GO HERE
import os
## END OF IMPORTS


#### YOUR CODE FOR text_count FUNCTION GOES HERE ####

def text_count(directory,filename,c = False,d = False):
    if d:
        a = os.path.join(directory,filename)
        f = open(a,"r")
        length = 0
        for line in f:
            length += len(line)
        return length
    if c == False:
        a = os.path.join(directory,filename)
        f = open(a,"r")
        a = f.read()
        a = a.split()
        return len(a)
    if c == True:
        a = os.path.join(directory,filename)
        f = open(a,"r")
        length = 0
        for line in f:
            line = line.strip()
            l_st = line.split(" ")
            for i in l_st:
                if i.islower():
                    length += 1
        return length
    

#### End OF MARKER

#### YOUR CODE FOR copy_lines FUNCTION GOES HERE ####

def copy_lines(inp,out,x):
    imp_fle = open(inp,"r")
    out_fle = open(out,"w")
    line_no = 0
    for line in imp_fle:
        line = line.strip()
        out_fle.write(line)
        line_no += 1
        if line_no==x:
            break
        out_fle.write("\n")
    return

#### End OF MARKER



