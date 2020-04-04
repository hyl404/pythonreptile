#必须把测试我文件创建到当前文件夹下，r为读的意思
print("Opening a text")
text_file = open("test.txt","r")
#读取第一个字符
print(text_file.read(1))
#读取一行文件,有几个就读取几行,{这个与下面那个读成一个列表不能同时使用}
# print(text_file.readline())
# print(text_file.readline())
# print(text_file.readline())
#将所有的行读成一个列表
lins = text_file.readlines()
print(lins)
#也可以得到其长度
print(len(lins))
#也可以进行循环迭代
for line in lins:
    print(line)
text_file.close()

    
#写入文档,{这个可以直接写入，pyhon会直接创造一个你命名的文档，但是只读模式下不行}
print("开始编写文档")
text_file2 = open("writ.txt","w")
text_file2.write("lin 1\n")
text_file2.write("lin 2\n")
text_file2.write("lin 3\n")
text_file2.close()
#要读取文件，必须重新以只读模式打开
text_file2 = open("writ.txt","r")
print(text_file2.read())


#将字符串写入到文档当中,如果打开的是同一个文件会把原来的内容全部替换掉
text_write = open("writ.txt","w")
lins = ["this is 1\n","this is 2\n","this is 3\n","this is 4\n"]
text_write.writelines(lins)
text_write.close()
text_writeRead = open("writ.txt","r")
for i in text_writeRead:
    print(i)
text_writeRead.close()


#在文件当中储存复杂的数据：

#1.文件进行Pickle处理
import pickle,shelve
varity = ["sweet","hot","dill"]
shape = ["shole","spear","chip"]
brand = ["Claussen","HYL","Vlassicle"]
f = open("pickles1.dat","wb")
pickle.dump(varity,f)
pickle.dump(shape,f)
pickle.dump(brand,f)
f.close()

#2.读取文件数据并进行反Pickle处理
f = open("pickles1.dat","rb")
varity = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
f.close()
print(varity)

#通过shelf保存序列话对象
s = shelve.open("pickles2.dat")
s["varity"]=["sweet","hot","dill"]
s["shape"]=["shole","spear","chip"]
s.sync()
#通过shelf获取序列化对象
print("varity:",s["varity"])
print("shape",s["shape"])
s.close()
