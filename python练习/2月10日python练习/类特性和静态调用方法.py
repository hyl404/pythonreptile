class Critter(object):
    total = 0
    @staticmethod
    def status():
        print("这里的小动物有：",Critter.total)
    def __init__(self,name):
        print("一个动物诞生了")
        self.name = name
        Critter.total += 1
#这个是通过属性来访问，静态方法都是通过类来访问的，所以status方法才没有self
#self是通过对象来访问时才用的
print(Critter.total)

crit1 = Critter("This is 1")
crit2 = Critter("This is 2")
crit3 = Critter("This is 3")
#通过类访问
Critter.status()
#通过对象访问
print(crit3.total)


#创建私有属性
class Critters(object):
    def __init__(self,name,mood):
        print("一个小动物诞生了！")
        self.name = name
        #创造一个私有属性
        self.__mood = mood
        #在方法内部就可以访问私有属性
        #print(self.__mood)
        
crit4 = Critters("shit","happy")
print(crit4.name)

#对对象进行修改
#crit4.name = "fucks"


#也可以强行访问，但是因该记住“总结”
#print(crit4._Critters__mood)

#这里就表示不能访问私有属性
print(crit4.mood)
#总结：客户端永远不应该访问到对象的私有属性



