"""Cannon Game

Python file to play a game where the objective is hitting targets with projectiles. Use the mouse pointer to throw a ball
to hit the blue balls

Modified by: 
Diego Alejandro Juárez Ruiz
Luis Enrique Zamarripa Marín

"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200) #Position where the projectile will start
speed = vector(0, 0) #Speed of the balls
targets = [] # List of created targets
speedProjectile = 250 #Speed of the projectile


def tap(x, y):
    """Function that will throw the projectile if the ball is not on screen when there is a click"""
    if not inside(ball): # If the ball is not in screen
        ball.x = -199
        ball.y = -199
        speed.x = (x + speedProjectile) / 25 # Move projectile
        speed.y = (y + speedProjectile) / 25


def inside(xy):
    """Return True if coordinates are inside of the game boundaries"""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw projectile and target balls"""
    clear()

    for target in targets: # Draw as blue balls all the targets
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball): # If the projectile is inside of the boundries, draw it as a red ball
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Function that moves all the targets and the projectile every frame"""
    if randrange(40) == 0: # Add randomly a target
        y = randrange(-150, 150) # Random position in y
        target = vector(200, y) 
        targets.append(target) # Add new target to list of targets

    for target in targets: 
        target.x -= 0.8 # Every target moves 0.8 in x every frame

    if inside(ball): # If the projectile is in the screen, move it
        speed.y -= 0.35 # Decrese projectiles speed in y to emulate gravity
        ball.move(speed)

    dupe = targets.copy() 
    targets.clear() # Clear list of targets

    for target in dupe: 
        if abs(target - ball) > 13: # If projectile is not near one of the targets, append it again to the list of targets
            targets.append(target)

    draw()
    deletes = [] # List of targets to be deleted
    for i in range(len(targets)):
    #for target in targets:
        if not inside(targets[i]):
            deletes.append(i) #If targets are not in the boundries, append it to list of delete

    for idx in deletes: # For every delete targets create a new target in start boundries
        targets.append(vector(200, randrange(-150, 150)))
        targets.pop(idx) # Delete original target out of boundries
    
    deletes = []

    ontimer(move, 20)


setup(420, 420, 370, 0) # Open window game
hideturtle()
up()
tracer(False)
onscreenclick(tap) # User click
move()
done()
