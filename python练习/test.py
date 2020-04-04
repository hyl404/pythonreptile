'''strs=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
day=eval(input("输入1到7之间的整数："))-1
#print(strs[day])

#字符串用指定的字符填充居中
s='aaa'.center(10,'*')
print(s)

#去掉字符串两边的字符
strs='a-bcd-a'
print(strs.strip('a'))

sums=0
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(i,j,i*j),end=" ")
        sums = sums+1
        if sums==i:
            print("\n")
    sums=0


sum1=0
sum2=0
for i in range(1,100,2):
    sum1 += i
for i in range(2,100,2):
    sum2 += i
result=sum1-sum2
print("最后值为：{}".format(result))

a=b=c=d=0
strs=""
strs=input("输入字符串：")
for i in strs:
    if i.isspace():
        a += 1
    elif i.isdigit():
        b += 1
    elif i.isalpha():
        c += 1
    else:
        d += 1
print("空格有:{}个,数字有:{}个,字母有:{}个,其他的字符有:{}个".format(a,b,c,d))

sum1=0
sum2=0
for i in range(1,100,2):
    sum1 += i
for i in range(2,100,2):
    sum2 += i
result=sum1-sum2
print("最后值为：{}-{}={}".format(sum1,sum2,result))

a=[]
for i in range(5):
    a.append(input("输入第{}个字符串:".format(i+1)))
print(a)
b="".join(a)
print(b)
'''

a=b=c=d=0
strs=""
strs=input("输入字符串：")
for i in strs:
    if i.isspace():
        a += 1
    elif i.isdigit():
        b += 1
    elif i.isalpha():
        c += 1
    else:
        d += 1
print("空格有:{}个,数字有:{}个,字母有:{}个,其他的字符有:{}个".format(a,b,c,d))

