# # 在函数内部定义一个函数，并且这个函数用到了外边函数的变量，那么将这个甘薯以及用到的一些变量称之为
#
# def test(number):
#     print("---1---")
#
#     def test_in(number2):
#         print("---2---")
#         print(number + number2)
#
#     print("---3---")
#     return test_in
#
#
# ret = test(100)
# print(" -"*30)
# ret(1)
# ret(100)
# ret(200)



def test(a, b):
    def test_in(x):
        print(a * b + x)

    return test_in



ret = test(4, 5)
print("_" * 30)
print("当x等于3，6，10依次如下(a * b + x):")
ret(3)
ret(6)
ret(10)