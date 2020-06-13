'''def w1(func):
    def inner():                                # 闭包
        print("---验证权限---")
        func()

    return inner

@w1
def test():
    print("---test---")

# ret = w1(test)
# ret()
# test = w1(test)                                 #w1函数对test函数的装饰  8=14
test()
'''




print("="*30)

def func(functionName):
    print("---func---1---")
    def func_in():
        print("---func_in---1---")
        functionName()
        print("---func_in---2---")
    print("---func---2---")
    return func_in

def test():
    print("----test----")


test = func(test)


test()
