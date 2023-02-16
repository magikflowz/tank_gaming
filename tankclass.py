from turtle import Turtle, Screen
scrn = Screen()
scrn.tracer(0)  #update screen
scrn.bgcolor('white')

speed = 5
size = 30

def moving_object(tank):

    tank.fillcolor('orange') # to fill the color in ball
    tank.begin_fill() # start color filling
    tank.circle(20)  # draw circle
    tank.end_fill() # end color filling     
    
#direcrions controls 
def up():
    Turtle.setheading(90) 
    Turtle.orward(100)

def down():
    Turtle.setheading(270)
    Turtle.forward(100)

def right():
    Turtle.setheading(0)
    Turtle.forward(100)

def left():
    Turtle.setheading(180)
    Turtle.forward(100)

tank_one = Turtle() # create a turtle object object   
tank_one.color('orange') # set a turtle object color
tank_one.speed(0) # set turtle object speed
tank_one.width(2) # set turtle object width
tank_one.hideturtle() # hide turtle object         
tank_one.penup() # turtle object in air              
tank_one.goto(-250, 0) # set initial position
tank_one.pendown()  # move turtle object to surface

tank_two = Turtle() # create a turtle object object   
tank_two.color('red') # set a turtle object color
tank_two.speed(0) # set turtle object speed
tank_two.width(2) # set turtle object width
tank_two.hideturtle() # hide turtle object         
tank_two.penup() # turtle object in air              
tank_two.goto(250, 0) # set initial position
tank_two.pendown()  # move turtle object to surface 
   
while True:         
    tank_one.clear()  # clear turtle work
    tank_two.clear() # clear turtle work
    moving_object(tank_one) # call function to draw ball
    moving_object(tank_two)
    scrn.update()  #update screen
    tank_one.forward(0.5)  
    tank_two.backward(0.5) 

# def travel():
#     tank_one.forward(speed)
#     scrn.ontimer(travel, 10)
    
#scrn.listen()
#travel()

scrn.mainloop()

