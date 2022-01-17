import turtle
import colorsys

turtle.title("star")
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(5)
n = 150
h = 0
t.left(180)
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(144)
    t.forward(i*5) 

# Python program to draw square
# # using Turtle Programming
# import turtle
# skk = turtle.Turtle()

# for i in range(4):
# 	skk.forward(50)
# 	skk.right(90)
	
# turtle.done()

# Python program to draw star
# using Turtle Programming
# import turtle
# star = turtle.Turtle()

# star.right(75)
# star.forward(100)

# for i in range(4):
# 	star.right(144)
# 	star.forward(100)
	
# turtle.done()

# Python program to draw hexagon
# using Turtle Programming
# import turtle
# polygon = turtle.Turtle()

# turtle.bgcolor('black')
# turtle.color('white')
# num_sides = 6
# side_length = 100
# angle = 360.0 / num_sides

# for i in range(num_sides):
# 	polygon.forward(side_length)
# 	polygon.right(angle)
	
# turtle.done()
