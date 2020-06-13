'''
def Fun1():
    x = 5
    def Fun2():
        nonlocal x                              # 在嵌套函数中声明调用外部函数的局部变量x
        x = 9
        x *= x
        return x
    return Fun2()
print(Fun1())
'''


'''
def outside():
    var = 5
    def inside():
        nonlocal var
        print(var)
        var = 3

    inside()


outside()
'''

'''
def funOut():
    def funIn():
        print("宾果!你成功访问到我了！")
    return funIn()
funOut()
'''

'''
def funOut():
    def funInt():
        print("宾果!你成功访问到我了！")
    return funInt
a = funOut()
a()
funOut()()
'''


'''
def foo():
    a = 1
    def bar():
        a = a + 1
        return a
    return bar
print(foo()())
'''

def funX():
    x = 5
    def funY():
        nonlocal x
        x += 1
        return x
    return funY
a = funX
print(a()())
print(a()())
print(a()())