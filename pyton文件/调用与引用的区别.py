# def test():
#     print("---1---")
#
#     def test_in():
#         print("---2---")
#         print()
#
#
# # 调用函数
# test()
# print("_"*30)
# # 引用函数
# b = test
# # 通过引用来调用函数
# b()



'''
def line_conf(a, b):
    def line(x):
        return a * x + b
    return line


line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5))
print(line2(5))
'''

'''
def funX():
    x = 5

    def funY():
        nonlocal x
        x += 1
        return x

    return funY


a = funX()
print(a())
print(a())
print(a())

'''

'''
def test(a, b, x):
    print(a*x + b)


A = 4
B = 5
x = 6
test(A, B, x)
'''

'''
def test(a, b):
    def test_in(x):
        print(a * x + b)

    return test_in


ret = test(4, 5)
print("_" * 30)
ret(3)
ret(6)
ret(12)
'''

'''
def w1(func):
    def inner():
        print("---权证权限---")
        func()
    return inner


@w1
def f1():
    # w1()
    print("---f1---")


def f2():
    # w1()
    print("---f2---")


def f3():
    w1()
    print("---f3---")


def f4():
    w1()
    print("---f4---")


# f1()
# f2()
# f3()
# f4()

# ret = w1(f1())
# ret()


# f1 = w1(f1)

'''


def w1(func):
    def inner():
        print("---权证权限---")
        func()
    return inner


@w1
def f1():
    # w1()
    print("---f1---")


def f2():
    # w1()
    print("---f2---")



f1()