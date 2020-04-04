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



# sum1=0
# sum2=0
# for i in range(1,100,2):
#     sum1 += i
# for i in range(2,100,2):
#     sum2 += i
# result=sum1-sum2
# print("最后值为：{}-{}={}".format(sum1,sum2,result))
