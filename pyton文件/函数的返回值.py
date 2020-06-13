'''def sum_2_num(num1, num2):
    result = num1 + num2
    print("计算的结果为:%d + %d = %d" % (num1, num2, result))


sum_2_num(10, 30)
'''

# def sum_2_num(num1, num2):
#     result = num1 + num2
#     return result
#     num = 100
#
#
# sum_result = sum_2_num(10, 20)
# print(sum_result)

# def calcuateNum(num):
#     result = 0
#     i = 1
#     while i <= num:
#         result += i
#         i += 1
#     return result
#
#
# calculate_result = calcuateNum(100)
# print("1~100 以内的和为: %d" % calculate_result)


# def testB():
#     print("- - - - tastB - - - -")
#     print("- - 这里是testB执行的代码- -")
#     print("- - - - testB - - - -")
#
#
# def testA():
#     print("- - - - tastA - - - -")
#     print("- - 这里是testA执行的代码- -")
#     print("- - - - testA - - - -")
#
#
# testA()
# testB()


# LEGB规则            查找一个符号对应的对象

# a = 100
# print(a)
# import test
# test.test()


'''A = 100
B = 200

def test():
    a = 11
    b = 22
    print(locals())

print(globals())'''

# num = 100               # G
# def test1():
#     num = 200           # E
#     def test2():
#         num = 300       # L
#         print(num)
#     return test2()
#
# test1()

num = 100
def test1():
    global num
    num = num + 2
    print(num)
def test2():
    print(num)

test1()
test2()