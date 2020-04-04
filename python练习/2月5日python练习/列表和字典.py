'''inventory = ["sword","armor","shield","healing potion"]
print("Your items:")
for item in inventory:
    print(item)
print("You have",len(inventory),"in your ass")

#对列表进行检索
index = int((input("选择你想要的角色：")))
print("这是你选择的角色：",inventory[index])

#对列表进行切片
start = int(input("选择你的角色从："))
finish = int(input("到这里结束："))
print("你的角色从",start,"开始","在",finish,"结束")
print(inventory[start:finish])

#对列表进行连接
chest =["gold","gems"]
print("你又发现两个ass")
print("你想要把他加入到你的队伍当中")
inventory= inventory+chest
print("现在你的队伍为：",inventory)

#通过切片对列表进行赋值
print("现在你需要对一些队员进行更改")
inventory[4:6] = ["you fire"]
print("现在你的队伍已经改变了：")
print(inventory)

#删除列表元素,其列表长度会减一，元素都会往前走
#[del与remove不一样，del是根据位置来删除元素而remove是根据值]
print("需要移除一些队员：")
# del inventory[2]
# print("你已经成功移除2号")
print(inventory)

#删除切片 删除的元素后，列表长度会缩短，剩下的元素会形成一个连续的、从零开始的列表
del inventory[:2]
print(inventory)




#创建字典
geek={
    "404":"fuck q assoul",
    "Googling":"you batter don't do that",
    "Link rot":"the process by web whinch lins is ok ",
    }
 print("获得键值是：",geek["404"])
test=input("你想访问的键值是：")
if test in geek:
    print(geek[test])
else:
    print("FUCK Q ,I DONT KONW WHAT IS FACK WITH THAT")
'''
inventory = ["sword","armor","shield","healing potion"]
start = int(input("选择你的角色从："))
finish = int(input("到这里结束："))
print("你的角色从",start,"开始","在",finish,"结束")
print(inventory[start:finish])
