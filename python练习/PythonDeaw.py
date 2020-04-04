import turtle
#turtle.setup(width,height,startx,starty),
#(窗体的宽度，窗体的高度，窗体的起始X位置，窗体的起始Y位置)
turtle.setup(650,350,200,200)
#抬起画笔
turtle.penup()
#使得画笔向前(或者向后，负数为向后)行走
turtle.fd(-250)
#放下画笔开始画画
turtle.pendown()
#画笔的大小
turtle.pensize(10)
#画笔的颜色
turtle.pencolor("red")
#使得画笔转向角度
turtle.seth(-40)
#range表示循环次数（从零开始）
for i in range(4):
    #turtle.circle（半径，多少弧度）如果半径为正数圆心在海归的左侧、为负数就在右侧
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(50)
turtle.done()
