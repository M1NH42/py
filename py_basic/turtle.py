import turtle

wn = turtle.Screen()
bgc = input("Enter background for the canvas")
wn.bgcolor(bgc)        # set the window background color

tess = turtle.Turtle()
tc = input("Enter turtle color")

tess.color(tc)              # make tess blue

p_size = input("Enter width of the turtle")
p_size = int(p_size)
tess.pensize(p_size)             # set the width of her pen


tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas