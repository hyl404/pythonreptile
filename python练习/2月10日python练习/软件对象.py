#这个是一个简单的类及其对象
class Critter(object):
    def talk(self):
        print("hi,i am your father")
crit = Critter()
crit.talk()

#构造器
class Test(object):
    def talks(self):
        print("Don't tach me ok??")
te1 = Test()
te2 = Test()
te1.talks()
te2.talks()

#使用其特性
class Tests(object):
    def __init__(self,name):
        print("A few peat is death")
        self.name = name

#这个方法是当对象被打印时直接被显示出来
    def __str__(self):
        rep = "Critter object\n"
        rep += "name:"+self.name+"\n"
        return rep
    
    def talk(self):
        print("Hi,",self.name)
        
crit1 = Tests("PPPPP")
crit1.talk()

crit2 = Tests("sssss")
crit2.talk()

print(crit1)


class Critter(object):
    def __init__(self,name):
        print("一个小动物诞生了！！")
        self.__name = name
    
    #这个就是对私有属性进行合法访问，如果么有将不能访问私有属性
    @property
    def name(self):
        return self.__name
    
    #对私有属性的合法写入方式
    #name.setter表示的时name的setter属性，用修饰符告诉pyhon，下面这个方法时修改name属性的
    #创建其他设置器也是这个方法（前提时修改的这个方法得有哈），都是先@符号+属性名称+.+setter
    @name.setter
    def name(self,new_name):
        if new_name == "":
            print("操作不成功，重新输入")
        else:
            self.__name = new_name
            print("名字更改成功")

    
crit = Critter("dog")
print(crit.name)
crit.name=""
print(crit.name)
