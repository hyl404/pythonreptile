import turtle
x1,y1 = 400,0
x2,y2 = 400,-400
x3,y3 = 0,-400
x5,y5 = 0,0
turtle.setup(650,350,200,200)
turtle.color("red","yellow")
turtle.begin_fill()
turtle.goto(x1,y1)
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x5,y5)
turtle.end_fill()
