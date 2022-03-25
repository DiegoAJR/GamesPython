"""
Memory Game

Puzzle grid to have fun finding and remembering number pairs.

Modified by: 
Diego Alejandro Juárez Ruiz
Luis Enrique Zamarripa Marín

"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif') # Sets the background picture
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64 # All tiles start hidden until discovered
writer = Turtle(visible=False)
taps = {'Taps': 0} # Counter of number of taps


def square(x, y):
    """Draw white squares with a black outline at (x, y) to represent the tiles."""

    # Positions the turtle at the beginning of the square
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()

    # For loop that makes the 4 lines of the square
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Converts the tile number to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Checks if you found/did not find a pair, as well as recognizing if you clicked the first tile of the turn."""
    spot = index(x, y)
    mark = state['mark']
    taps['Taps'] += 1  # Add 1 tap
    print("Number of taps: "+ str(taps['Taps'])) # Print in console number of taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]: # Didn't find a pair
        state['mark'] = spot
    else: # Found a pair
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    
    if True not in hide: # Checks whether there are still any hidden tiles
        print("The game is over, your bravery is unmatched.")

def draw():
    """Function that draws the background and all the tiles in the game."""
    clear() # Every frame the grid is updated
    goto(0, 0)
    shape(car) # Add the image as a background
    stamp()

    for count in range(64):
        if hide[count]: # For every square in the gird
            x, y = xy(count) #Take every coordinates to square tiles
            square(x, y) # Make the white square

    mark = state['mark'] #Take the status of a tile

    if mark is not None and hide[mark]: 
        x, y = xy(mark) # Take the coordinates of the selection 
        up() 

        if(tiles[mark] < 10): #If mark has 1 number to center add to x 15
            goto(x + 15, y)
        else: #If mark has 2 number to center add to x 3
            goto(x + 3, y)

        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal')) # Display the mark number of the selecction

    update() 
    ontimer(draw, 100)


shuffle(tiles) # Shuffle the number in the tiles
setup(420, 420, 370, 0) # Open the game window
addshape(car) # Add the background 
hideturtle() 
tracer(False) 
onscreenclick(tap)
draw()
done()
