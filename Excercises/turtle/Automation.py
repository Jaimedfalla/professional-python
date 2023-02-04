import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
i = 0

# for i in range(4):
#     t.forward(100)
#     t.right(90)

while i <= 100:
    t.circle(i)
    i +=10

turtle.done()