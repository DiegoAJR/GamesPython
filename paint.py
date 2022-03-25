"""
Paint Game

Python file that emulates a paint game. Game to draw shapes and lines.

Modified by: 
Diego Alejandro Juárez Ruiz
Luis Enrique Zamarripa Marín

"""

from turtle import *
import turtle

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down() # Start drawing
    goto(end.x, end.y)


def square(start, end):
    """Draw square by selecting two of the corners"""

    # Positions the turtle at the beginning of the square
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # For loop that makes the 4 lines of the square
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle with radius from start to end."""
    up()
    goto(start.x, start.y - (end.x-start.x)) # Start below to make the user input center
    down()
    begin_fill()
    turtle.circle(end.x -start.x) # Draw circle with radius
    end_fill()


def rectangle(start, end):
    """Draw rectangle by clicking on its top left and bottom right corners."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    goto(end.x, start.y) # Draw from the top left corner to the top right corner
    goto(end.x, end.y) # Draw from the top right corner to the botom right corner
    goto(start.x, end.y) # Draw from the bottom right corner to the bottom left corner
    goto(start.x, start.y) # Draw from the bottom left corner to the top left corner
    end_fill()


def triangle(start, end):
    """Draw triangle by selecting two of the corners."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # For loop that makes the remaining 2 lines and closes off the triangle
    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape when clicking the screen"""
    start = state['start']

    # If the click was the first one, you store the position
    if start is None:
        state['start'] = vector(x, y)
    # If the click was the second one, you draw the shape
    else:
        shape = state['shape'] # Retrieve the drawing mode
        end = vector(x, y)
        shape(start, end) # Draw the shape
        state['start'] = None


def store(key, value):
    """Stores the drawing mode in the state dictionary."""
    state[key] = value


state = {'start': None, 'shape': line} # Dictionary that stores the initial press and the drawing mode
setup(420, 420, 370, 0) # Open game window
onscreenclick(tap)
listen()
onkey(undo, 'u')

# Change colors by pressing the indicated capital letters
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P') # New color pink

# Select different drawing modes by pressing the indicated letters
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done()
