'''import turtle
import math
x1,y1 = 100,100
x2,y2 = 100,-100
x3,y3 = -100,-100
x4,y4 = -100,100
x5,y5 = 0,0

turtle.goto(x1,y1)
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)
turtle.goto(x5,y5)

计算两点之间距离
distance = math.sqrt((x1-x4)**2 + (y1-y4)**2)
turtle.write(distance)
'''
sums=0
for i in range(1,10):
    for j in range(1,i+1):
        print("{0}*{1}={2}".format(i,j,i*j),end=" ")
        sums = sums+1
        if sums==i:
            print("\n")
    sums=0#注意一定要让其重新计数

