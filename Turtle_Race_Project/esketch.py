from turtle import Turtle, Screen #remeber both classes are from turtle module

tim = Turtle()  #remember you can create multiple objects that function independently of each other
screen = Screen()




def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10 #this code line is needed so everytime the key "a" is pressed the turtle moves a bit more that direction
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup() #this is needed because when we clear the turtle draws a line all the way back so we need to clear that with pen up
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(key="w",fun=move_forward)  #this sreen.onkey says what key to push and what function that key wil perform based on the function you made as the input for the screen.onkey
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear)
screen.exitonclick()
