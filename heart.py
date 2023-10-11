# Set up the turtle
import turtle


heart = turtle.Turtle()
heart.speed(1)  # Adjust the speed of drawing (1 = slowest)

# Draw the heart shape
heart.fillcolor('red')
heart.begin_fill()
heart.left(50)
heart.forward(133)
heart.circle(50, 200)
heart.right(140)
heart.circle(50, 200)
heart.forward(133)
heart.end_fill()

# Hide the turtle and display the heart shape
heart.hideturtle()
turtle.done()