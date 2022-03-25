"""
Pacman Game

Python file that emulates a pacman game. The objective is to eat the small white balls in the map while avoiding the ghosts

Modified by: 
Diego Alejandro Juárez Ruiz
Luis Enrique Zamarripa Marín

"""

from random import choice
from turtle import *

from freegames import floor, vector

state = {'score': 0}
path = Turtle(visible=False) # Turtle object that draws the map
writer = Turtle(visible=False) # Turtle object that writes the score
aim = vector(5, 0) # Vector that represents Pacman's movement
pacman = vector(-40, -80) # Vector that represents Pacman's position
ghosts = [      # List with vectors representing the ghosts's positions
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
# fmt: off

# Matrix representing the game map. 1 = path, 0 = wall
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]
# fmt: on

def square(x, y):
    """Draws a square in the given X and Y coordinates."""
    
    # Positions the turtle at the beginning of the square
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    # For loop that draws the 4 lines of the square
    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """Draws the map layout using the path object. Uses the tiles matrix to know where to draw."""
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y) # Draws a blue square on the calculated X and Y positions

            # If the tile has a 1, as an addition to it being a blue square, it'll have a white ball to eat
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


def move():
    """Move pacman and all ghosts."""

    # Score writer
    writer.undo()
    writer.write(state['score'])

    clear()

    # Checks if pacman can move to where he's aiming. If he can, he moves
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2 # Removes the indicator of white ball
        state['score'] += 1 # Adds to your score when you eat a white ball
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y) # Draws the new square

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow') # Draw pacman in its new position

    for point, course in ghosts: # Movement for every ghost
        #Check position of pacman and valid movements to get closer
        if(point.x < pacman.x and valid(point + vector(10,0))): 
            point.move(vector(10,0))
        elif(pacman.y < point.y and valid(point + vector(0,-10))):
            point.move(vector(0,-10))
        elif(point.x > pacman.x and valid(point + vector(-10,0))):
            point.move(vector(-10,0))
        elif(pacman.y > point.y and valid(point + vector(0,10))):
            point.move(vector(0,10))
        else: #If none of movements are valid, move randomly
            options = [
                vector(5,0),
                vector(-5,0),
                vector(0,5),
                vector(0,-5)
            ] #Options of movements
            plan = choice(options)
            # Change course of ghosts
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)


def change(x, y):
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


setup(420, 420, 370, 0)
hideturtle()
tracer(False)

# Turtle object that writes the player score at the right of the map
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])

listen()

# Set up movement keys
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')

world()
move()
done()
