import turtle as t

t.Screen().bgcolor("maroon")
t.Screen().setup(400,300)

pen=t.Turtle()


for i in range(3):
    pen.forward(100)
    pen.right(120)
pen.up()
for j in range(1):
    pen.right(90)
    pen.forward(50)
    pen.left(150)
pen.down()
for k in range(3):
    pen.forward(100)
    pen.right(120)
    



t.done()