# 1~5的阶乘 即 5 x 4 x 3 x 2 x 1的结果是多少？
# def cal_num(num):
#     if num <= 1:
#         return 1
#     return num * cal_num(num - 1)
#
#
# result = cal_num(5)
# print('1~5的阶乘值为:%d' % result)

#  n的阶乘
# print("请输入你要计算的阶乘:")
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# n = int(input())
# print(fact(n))


# 匿名函数
#
# def test(a, b):
#     return a + b
#
# print(test(5, 6))
#
# result = lambda x, y: x + y
#
# print(result(33, 22))


# 将lamda作为参数进行传递
# def test(a, b, c):
#     return c(a, b)
#
#
# print(test(33, 22, lambda x, y: x + y))
# print(test(33, 22, lambda x, y: x - y))
# print(test(33, 22, lambda x, y: x * y))
# print(test(33, 22, lambda x, y: x / y))

# 对列表中的num进行排序!
# a = [
#     {'num': 6, 'age': 18},
#     {'num': 23, 'age': 16},
#     {'num': 16, 'age': 28}]
# a.sort(key=lambda x: x['age'], reverse=True)
# print(a)

#
# n = int(input('请输入一个整数：'))
# s = str(n)
# f = True
#
# for i in range(len(s)//2):
#     if s[i] != s[-1-i]:
#         f = False
#         break
# if f:
#     print('%d 是一个回文数' % n)
# else:
#     print('%d 不是一个回文数' % n)

#

n = int(input("请输入你要求多少项和: "))
sum = 0
for i in range(1,n+1):
    if i % 2 == 0:
        sum -= 1/(i * (i+1))
    else:
        sum += 1/(i * (i+1))
print(sum)

