import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.hideturtle()
t.width(4)
ci=0
cis=2
c = ["sandybrown","orange","darkorange",
"chocolate","firebrick"]
for i in range (190):
    t.color(c[cis])
    t.begin_fill()
    t.circle(190-i/2,90)
    t.left(90)
    t.circle(190-i/2,90)
    t.color(c[ci])
    t.fillcolor(c[ci])
    t.end_fill()
    ci=ci+1
    cis=cis+1
    if cis ==5:
        cis=0
    if ci==5:
        ci=0
    t.left(36)

s.exitonclick()