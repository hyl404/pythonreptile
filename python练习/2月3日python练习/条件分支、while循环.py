import random
#random.randint与random.randrange都是创建随机数的方法，可以根据自己的需要选择。
die = random.randint(1,6)
die2 =  random.randrange(6)+1
total = die + die2
print("your die:",die,"your die2:",die2,"finaly total:",total)

#if 条件语句
#注意的是if与else的位置
print("输入密码")
password = input("这里输入请:")
if  password=="321":
    print("YES YOU RIGHT")
else:
    print("FUCK YOU")

#while循环
name="test"
test=""
while test!="爸爸":
    test=input("你是谁啊")
print("ok")

#while的无限循环（没有改变哨兵的值）
name="test"
test=0
while test<=10:
   # test=test+1 要改变哨兵的值
    print(test)
