#Team Members
#Anthony Urbina
from turtle import Turtle, Screen
scrn = Screen()
scrn.bgcolor('white')

vx, vy = 20.0, 88.0
speed = 1

tank_one = Turtle() # create the first tank
tank_one.penup()
scrn.onscreenclick(tank_one.goto) # set up the callback for moving the first turtle

# tank_two = Turtle() # create the second tank
# tank_two.penup()
# scrn.onscreenclick(tank_two.goto) # set up the callback for moving the first turtle

#def tank_one_controls(): # the function to move the second turtle
    
scrn.onkey(lambda: tank_one.setheading(180), 'Up')
scrn.onkey(lambda: tank_one.setheading(180), 'Left')
scrn.onkey(lambda: tank_one.setheading(0), 'Right')
scrn.onkey(lambda: tank_one.setheading(270*20.0*88.0), 'Down') # which sets itself up to be called again


def travel():
    tank_one.forward(speed)
    #tank_two.forward(speed)
    scrn.ontimer(travel, 10)
    
scrn.listen()
travel()

scrn.mainloop()