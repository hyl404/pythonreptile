'''import time
#拼接符的效率更低，循环一次就要创建一个对象
time01 = time.time()
a = ''
for i in range(100000):
    a = a +"he"
time02 = time.time()
print("运算时间为：",(time02-time01))

#join效率更高，始终只有一个对象
time03 = time.time()
li=[]
for i in range(100000):
    li.append("Test")
b = "".join(li)
time04 = time.time()
指定保留小数点后面几
print("运算时间为：",format(time04-time03,'.5f'))'''


score = int(input("请输入一个在0-100 之间的数字："))
grade = ""
while score>100 or score<0:
    score = int(input("输入错误！请重新输入一个在0-100 之间的数字："))
if score>=90:
    grade = "A"
elif score>=80:
    grade = 'B'
elif score>=70:
    grade = 'C'
elif score>=60:
    grade = 'D'
else:
    grade = 'E'
print("分数为{0},等级为{1}".format(score,grade))
