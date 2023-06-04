import turtle as tu 
import colorsys
tu.Screen().bgcolor('black')
t = tu.Turtle()
t.speed(-100)
h = 0.3
t.pensize(5)
def desin(set_ang,r):
    t.seth(set_ang)
    t.circle(200-r,120)
    t.seth(set_ang+180)
    t.circle(200-r,120)
for i in range(20):
    c = colorsys.hsv_to_rgb(h,0.8,1)
    t.pencolor(c)

    for j in range(30):
        desin(i*10,3+j)
    h += 0.1
tu.done()