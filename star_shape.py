# # making star 

import turtle
star_turtle=turtle.Turtle()
star_turtle.fillcolor("red")
star_turtle.begin_fill()
for i in range(5):
    star_turtle.color("Green")
    star_turtle.forward(200)
    star_turtle.right(144)

star_turtle.end_fill()

turtle.done()