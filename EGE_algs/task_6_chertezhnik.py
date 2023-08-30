from turtle import *

screensize(10000, 10000)
tracer(0)
size = 25

for _ in range(3):
    goto(xcor() + 90 * size, ycor() + 90 * size)
    goto(xcor() + -60 * size, ycor() + 0 * size)
    goto(xcor() + -30 * size, ycor() + -90 * size)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*size, y*size)
        dot(5, "red")
update()
exitonclick()