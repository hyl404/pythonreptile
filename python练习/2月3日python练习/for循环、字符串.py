# 通过range迭代数子，这里默认传入的是字符串，要改为数字
numbe =int( input("输入要迭代的数字：\n"))
for i in range(numbe):
    print(i)
    
#以5五为单位进行计数
for i in range(0,50,5):
    print(i)
    
#向后计数 end表示不换行
for i in range(10,-3,-1):
    print(i,end="")
    
#通过len（）统计输入的字符串有多少个，在输入的字符串内进行查找
masage = input("\n输入你想要输入的内容：")
print("你输入的内容有",len(masage),"个字符")
find=input("查找你的字符:")
if find in masage:
    print("YES")
else:
    print("NO")
    
#演示字符串的索引
import random
word = "HelloWord"
#长度为正或者长度为负
high = len(word)
low = -len(word)
for i in range(15):
    #总共为15个字符（倒着数和正着数），使用随机数在其中抽取一个，并看他对应的字符
    position = random.randrange(low,high)
    print("第",position,"个字符是",word[position])

#根据条件构造新的语句
message = input("输入字符")
newmeage = ""
Wore = "这不的"
for letter in message:
    if letter.lower() not in Wore:
       newmeage=newmeage+letter
print("新的语句：",newmeage)

#对字符串进行切片
word = "pizza"
start = None
while start!="":
    start=input("Start:")
    if start:
        start = int(starts)
        finish = int(input("finish"))
        print("从",starts,"开始","到",finish,"结束")
        print("切成",word[starts,finish])
    

        
