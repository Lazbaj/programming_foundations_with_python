import turtle

def draw_square(tarta,side):
    i=0
    while i<4:
        tarta.forward(side)
        tarta.right(90)
        i=i+1

def draw_circle(tarta,radius):
    tarta.circle(radius)

def draw_triangle(tarta,side):
    i=0
    while i<3:
        tarta.forward(side)
        tarta.right(120)
        i=i+1

# Create a new window with background
window = turtle.Screen()
window.bgcolor('lightblue')

# Create a new turtle
tarta1 = turtle.Turtle()
tarta1.shape('turtle')
tarta1.shapesize(1,1)
tarta1.color('blue','purple') #Colore della linea e della tartaruga
tarta1.speed(20)
tarta1.begin_fill()

# Draw a circle with n square
n=50
for i in range(1,n+1):
    draw_square(tarta1,100)
    tarta1.right(360./n)

tarta1.end_fill()

# Create a second turtle and draw a circle
# tarta2 = turtle.Turtle()
# tarta2.shape('arrow')
# tarta2.color('blue')
# tarta2.speed(3)
# draw_circle(tarta2,100)

# Create a third turtle and draw a flower with triangles
# tarta3 = turtle.Turtle()
# tarta3.shape('turtle')
# tarta3.color('white')
# tarta3.speed(20)

# tarta3.left(90)
# tarta3.back(200)
# tarta3.forward(300)

# n=50
# for i in range(1,n+1):
#     draw_triangle(tarta3,50)
#     tarta3.right(360./n)
# n=15
# for i in range(1,n+1):
#     draw_triangle(tarta3,100)
#     tarta3.right(360./n)

window.exitonclick()
