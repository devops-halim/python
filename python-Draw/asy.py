import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.hideturtle()
t.width(1)
for i in range (190):
    t.color("green")
    t.begin_fill()
    t.circle(190-i/2,90)
    t.left(36)
s.exitonclick()