#Team Members
#Anthony Urbina 
#Github Repository: https://github.com/magikflowz/tank_gaming
from turtle import Turtle, Screen
import math
scrn = Screen()
scrn.title("Tank Gaming")
scrn.tracer(0)  #update screen
scrn.bgcolor('white')

vx = 20.0
vy = 88.0




#CREATING MOVING OBJECT CONTROLS 
def moving_object(tank, color):
    """moving_objects is a function that creates the moving objects
    
        Args:
            tank (turtle object) : Object name that is going to be created
            color (string):  color of the moving object
    """
    tank.fillcolor(color) # to fill the color in ball
    tank.begin_fill() # start color filling
    tank.circle(20)  # draw circle
    tank.end_fill() # end color filling     
    tank.shape('triangle')

def draw_triangle(tank,length=30):
    """draw triangle on top of tank
    
        Args:
            tank (turtle object) : Object name that is going to be created
            length (int): length of the triangle
    """
    tank.shape('triangle')
    for i in range(3):
        tank.forward(length)
        tank.left(120)
        
def get_tank_one_coordinates(object):
    """get coordinates

      Args:
           Object (turtle object) : Object
    """
    tank_one_x = object.xcor()
    tank_one_y = object.ycor()
    return tank_one_x, tank_one_y

def get_tank_two_coordinates(object):
    """get coordinates

      Args:
           Object (turtle object) : Object
    """
    tank_two_x = object.xcor()
    tank_two_y = object.ycor()
    return tank_two_x, tank_two_y
     
#direcrions controls 
#-------TANK ONE CONTROLS--------------
def tank_one_up():
    """tank one up controls
        Args:
            xy: y velocity value
    """
    tank_one.setheading(90) 
    tank_one.forward(100)

def tank_one_down():
    """tank one down controls
        Args:
            None
    """
    tank_one.setheading(270)
    tank_one.forward(100)
    
def tank_one_left():
    """tank one left controls
        Args:
            None
    """
    tank_one.setheading(180)
    tank_one.forward(100)

def tank_one_right():
    """tank one right controls
        Args:
            None
    """
    tank_one.setheading(0)
    tank_one.forward(100)

#-------TANK TWO CONTROLS-------------
def tank_two_up():
    """Tank two up controls
        Args:
            None
    """
    tank_two.setheading(90) 
    tank_two.forward(100)

def tank_two_down():
    """Tank two down controls
        Args:
            None
    """
    tank_two.setheading(270)
    tank_two.forward(100)

def tank_two_left():
    """Tank two left controls
        Args:
            None
    """
    tank_two.setheading(180)
    tank_two.forward(100)

def tank_two_right():
    """Tank two right controls
        Args:
            None
    """
    tank_two.setheading(0)
    tank_two.forward(100)

#Setting up tank objects 
#Tank One object
tank_one = Turtle() # create a turtle object object   
tank_one.color('green') # set a turtle object color
tank_one.speed(5) # set turtle object speed
tank_one.width(2) # set turtle object width
tank_one.hideturtle() # hide turtle object         
tank_one.penup() # turtle object in air              
tank_one.goto(-250, 0) # set initial position
tank_one.pendown()  # move turtle object to surface

#Tank Two Object 
tank_two = Turtle() # create a turtle object object   
tank_two.color('red') # set a turtle object color
tank_two.speed(0) # set turtle object speed
tank_two.width(2) # set turtle object width
tank_two.hideturtle() # hide turtle object         
tank_two.penup() # turtle object in air              
tank_two.goto(250, 0) # set initial position
tank_two.pendown()  # move turtle object to surface 

get_tank_one_coordinates(tank_one) #grabs the coordinates of tank one 
tank_one_coordinates_values = get_tank_one_coordinates(tank_one)
tank_one_x_value = tank_one_coordinates_values[0]
tank_one_y_value = tank_one_coordinates_values[1]
tank_two_coordinates_values = get_tank_two_coordinates(tank_two)
tank_two_x_value = tank_two_coordinates_values[0]
tank_two_y_value = tank_two_coordinates_values[1]

tank_one_velocity = math.cos(tank_one_x_value + vx)
tank_two_velocity = math.cos(tank_two_x_value + vx)

#while loop to keep the objects loaded 
while True:         
    tank_one.clear()  # clear turtle work
    tank_two.clear() # clear turtle work
    moving_object(tank_one, 'red') #Creating tank one moving object 
    draw_triangle(tank_one) #creates turrent for tank one drawing
    moving_object(tank_two, 'blue') #Creating tank two moving object 
    draw_triangle(tank_two) #creates turret  for tank two drawing
    scrn.update()  #update screen
    scrn.listen() #listen for key presses 
    
#-------------On button press controls ----------------------------------
    """scrn.onkey() parameters
        args: 
            direcrions controls: points the tank object to right angle
            "": maps the function to the button press
    """
    scrn.onkey(tank_one_up, "Up") 
    scrn.onkey(tank_one_down, "Down")
    scrn.onkey(tank_one_left*tank_one_velocity, "Left")
    scrn.onkey(tank_one_right*tank_one_velocity, "Right")
    
    scrn.onkey(tank_two_up, "w") 
    scrn.onkey(tank_two_down, "s")
    scrn.onkey(tank_two_left, "a")
    scrn.onkey(tank_two_right, "d")