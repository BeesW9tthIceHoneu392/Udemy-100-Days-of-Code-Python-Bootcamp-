from turtle import Turtle, Screen #remeber both classes are from turtle module

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward) #this method requires you to make a function as an input which we will make called move forward
#the space key is binded and  is needed to trigger the function
#a function within a function as an arguement like the screen.onkey does not require parenthesis at the end
screen.exitonclick()

