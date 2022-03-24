"""
Snake Game

Python file to play the classic snake game. Move through the map to
collect food and make your snake bigger

Modified by:
Diego Alejandro Juárez Ruiz
Luis Enrique Zamarripa Marín

"""

from random import randrange, sample
from turtle import *

from freegames import square, vector

food = vector(0, 0) # Position of the food
snake = [vector(10, 0)] # List of snake path
aim = vector(0, -10) #Direction


def change(x, y):
    """Function that changes the direction of the snake"""
    aim.x = x
    aim.y = y


def inside(head):
    """Funciton that return True if the given coordinates are in the boundries of the map"""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake and food one space every frame"""
    head = snake[-1].copy() #Take the last position of the snake
    head.move(aim) # Move snake to the next positiion in the direction

    if not inside(head) or head in snake: #If the snake is out of boundries or in the same position of a snake
        # draw red squere and game over
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head) # Append to the path of the snake the new head


    if head == food: # If the snake is in the same position as the food
        print('Snake:', len(snake)) 
        food.x = randrange(-15, 15) * 10 # Place more food in a random place
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0) #Delete the tail 

    clear()

    for body in snake: # Draw every squere of the snake
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, foodColor) # Draw squere of the food

    movesFood = [vector(0,10),vector(0,-10),vector(10,0),vector(-10,0)] #Possible moves of the food
    movedFood = food.copy() # Temporary food
    movedFood.move(movesFood[randrange(0,3)]) #Move the temporary food to a posible position

    while not inside(movedFood): # If the last moved was not possible
        movedFood = food.copy() # Move the temporary food again to another position
        movedFood.move(movesFood[randrange(0,3)])

    food.x = movedFood.x #Uptade the coordinates of food
    food.y = movedFood.y

    update()
    ontimer(move, 100)

snakeColor, foodColor = sample(["black", "green", "blue", "pink", "orange"], 2) #Possible colors for food
setup(420, 420, 370, 0) # Open the game window
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right') # Listen every input to change direction
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
