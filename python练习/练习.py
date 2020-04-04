import turtle
import math
'''
#【输入三角形三个顶点的坐标】
x1,y1=eval(input("请输入第一个坐标，用逗号隔开："))
x2,y2=eval(input("请输入第二个坐标，用逗号隔开："))
x3,y3=eval(input("请输入第三个坐标，用逗号隔开："))
a1=round(math.sqrt((x1-x2)**2+(y1-y2)**2))
a2=round(math.sqrt((x1-x3)**2+(y1-y3)**2))
a3=round(math.sqrt((x3-x2)**2+(y3-y2)**2))
print("三边为：",a1,a2,a3)
if a1+a2>a3 or a1+a3>a2 or a2+a3>a1:
    res=(a1+a2+a3)/2
    final_result=math.sqrt((res*(res-a1)*(res-a2)*(res-a3)))
print("三角形的面积为：{:.2f}".format(final_result))





#【利用 while 循环，计算 1-100 之间数字的累加和】
j=1
sums=0
SumsEven=0
SumsOdd=0
while j <=100:
    sums += j
    if j%2==0:
        SumsEven += j
    else:
        SumsOdd +=j
    j += 1
print(sums)   
print(SumsEven)
print(SumsOdd)
print("\n")



    
#【打印如下图案】
for i in range(5):
    for k in range(5):
        print(i, end=""),
    print("\n")





#【打印九九乘法表】
sums=0
for i in range(1,10):
    for j in range(1,i+1):
        print("{0}*{1}={2}".format(i,j,i*j),end=" ")
        sums = sums+1
        if sums==i:
            print("\n")
    sums=0#注意一定要让其重新计数 

 

#【用列表和字典存储下表信息】，      
d1=dict(name="高小一",age=18,wage=30000)
d2=dict(name="高小二",age=19,wage=20000)
d3=dict(name="高小三",age=20,wage=10000)
d4=[d1,d2,d3]
for i in d4:
    if i.get("wage")>15000:
        print(i)
【列表法】
a=[
    ["高小一",18,30000,"北京"],
    ["高小二",19,20000,"上海"],
    ["高小五",20,10000,"深圳"]
    ]

【方法一】
for i in range(3):
    #print(a[i][2])
    if a[i][2]>15000:
        print(a[i])
【方法二】
for i in a:
    if i[2]>15000:
        print(i)




#【要求输入员工的薪资】
empnum=0
wage=0
wageinformation=[]
while True:
    s = input(" 请输入员工工资，输入完成后输入Over结束：")
    if s == "Over":
        print("Over")
        break
    if eval(s)<=0:
        continue
    empnum += 1
    wage +=eval(s)
    wageinformation.append(eval(s))
print("员工数：",empnum)
print("工资明细：",wageinformation)
print("平均工资:{0}".format(wage/empnum))




#【员工一共 4 人】.
wage=0
wageinformation=[]
for i in range(4):
    s = input()
    if s=="Over":
        break
    if eval(s)<=0:
        print("格式错误，重新输入")
        continue
    wageinformation.append(eval(s))
    wage += eval(s)
if i!=3:
    print("您未能全部录入所有员工的工资，您录入了 {0}名员工的薪资，分别为{1}：".format(i,wageinformation))
    print("平均工资:{0}".format(wage/1))
else:
    print("您已经全部录入4名员工的薪资，分别为：",wageinformation)
    print("平均工资:{0}".format(wage/4))




#【同心圆】
turtle.pencolor("red")
for t in range(10,200,10):
    turtle.circle(t)
    turtle.penup()
    turtle.right(90)
    turtle.fd(10)
    turtle.left(90)
    turtle.pendown()
turtle.done()





#【棋盘18*18】                        
turtle.speed(0)                          
for y in range(0,360,20):
    turtle.penup()
    turtle.goto(-350,y)
    turtle.pendown()                     
    turtle.forward(340)
turtle.penup()
turtle.goto(-350,0)
turtle.left(90)
turtle.pendown()
for z in range(-350,0,20):
    turtle.penup()
    turtle.goto(z,0)
    turtle.pendown()                     
    turtle.forward(340)




#【通过sort()逆序排列后再输出】
number = input("输入任意数字并用空格隔开：")
resut=number.split()
FinallyResut = sorted(resut,reverse=True)
print(FinallyResut)




#【输入一个分数】
v = int(input("输入分数："))
if v>100 or v<0:
    print("格式错误")
elif   100> v >=90:
    grade = "A"
elif  90> v >=80:
    grade = "B"
elif 80> v >=70:
    grade = "C"
elif 70 > v >=60:
    grade = "D"
else:
    grade = "E"
print("分数是{0}，等级是{1}".format(v,grade))
【输入一个分数 法二 】
degree='ABCDE'
number=0
if v>100 or v<0:
    print("格式错误")
else:
    number=v//10
    if number<6:
        numb er=5
    print(degree[9-number])





【输入一个毫秒数，将该数字换算成小时数，分钟数、秒数】
time=float(input("时间："))
seconds=time/1000
minutes=seconds/60
hours=minutes/60
print(seconds)
print(minutes)
print(hours)



#【使用海龟绘图。输入多个点，将这些点都两两相连】
a = [(10,20),(80,100),(30,5),(100,60)]
n = len(a)
for i in range(n):
    for j in range(i,n):
        turtle.penup()
        turtle.goto(a[i])
        turtle.pendown()
        turtle.goto(a[j])


        

【输出100内前5个可以被3整除的数】
number=0
for i in range(100):
    if i%3==0:
        print(i)
        number += 1
    if number==5:
        break


        
【输出100~200内是素数】
for i in range(100,200):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)

【1！+2！+3！+… +10!】
sums=0
a=1
for i in range(1,11):
   a*=i
   sums+=a
print(sums)

【斐波那契数列】
def shulie(n):
   if n <= 1:
       return n
   else:
       return(shulie(n-1) + shulie(n-2))
 
number = int(input("您要输出几项？(填写正整数):"))
 
print("数列为:")
for i in range(number):
   print(shulie(i),end=' ')

【进度条】
#\r 表示将光标的位置回退到本行的开头位置
import time
scale = 100
start=time.perf_counter()
for i in range(scale+1):
    a="*"*i
    b=" "*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print("\r{:.1f}% {}->{} ".format(c,a,b ),end=' ')
    time.sleep(0.1)
print(dur)
input("\n\nPress the enter key to exit.")


'''
