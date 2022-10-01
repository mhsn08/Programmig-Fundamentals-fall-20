### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###

def calculateArea(width, length):
    return width*length

#### End OF MARKER



### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###

def checkTilesFit(plot_width, plot_length, tile_width, tile_length):
    aP = plot_width*plot_length
    aT = tile_width*tile_length
    if aP%aT==0 and (plot_length%tile_length==0 or plot_length%tile_width==0) and (plot_width%tile_width==0 or plot_width%tile_length==0) and (plot_length>0 and plot_width>0 and tile_length>0 and tile_width>0) :
        return True
    else :
        return False
    return

    
    
#### End OF MARKER



### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###

def calculateTiles (plot_width, plot_length, tile_width, tile_length):
    if type (plot_width)==str or type(plot_length)==str or type(tile_width)==str or type(tile_length) == str:
        return "Invalid Input"
    elif plot_width==0 or plot_length==0 or tile_width==0 or tile_length == 0:
        return None
    else :
        if checkTilesFit(plot_width, plot_length, tile_width, tile_length) == True:
            aP = calculateArea(plot_width, plot_length)
            aT = calculateArea(tile_width, tile_length)
            no_of_tiles = aP/aT
            return round (no_of_tiles)
        else :
            return "Not Possible"
        return
    return




#### End OF MARKER



