def instructions():
    print("welcom to my hous Can i ask you some questions??")
print("Tady my frined to my home")
instructions()

#参数和返回值
def display(message):
    print(message)
def give():
    five = 5
    return five
def ask(question):
    "Ask a yes or no questions"
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

display("这里有几个数字要给您看看")
number = give()
print("这个数字是：",number)
answer = ask("请按y 或者N")
print("谢谢您的答案： ",answer)

#全局变量的控制 global对six的绝对控制，代表可以在函数内部修改全局变量
def test():
    # global six
    six = -6
    return six
name="six"
six = 5
test()
print(six)
