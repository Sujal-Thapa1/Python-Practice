import turtle

def draw_heart():
    # Create a turtle object
    pen = turtle.Turtle()
    
    # Set the fill color to red
    pen.fillcolor('red')
    
    # Start filling the color
    pen.begin_fill()
    
    # Draw the left curve
    pen.left(140)
    pen.forward(113)
    for _ in range(200):
        pen.right(1)
        pen.forward(1)
    
    # Draw the right curve
    pen.left(120)
    for _ in range(200):
        pen.right(1)
        pen.forward(1)
    
    pen.forward(112)
    
    # End filling the color
    pen.end_fill()
    
    # Hide the turtle
    pen.hideturtle()
    
    # Keep the window open
    turtle.done()

# # Call the function to draw the heart
draw_heart()