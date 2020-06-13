# a = 100
# # print(a)
# # import test
# # test.test()


# char = input("请输入一个需要判断的字符串:")
# lenght = len(char)
# j = 0
# a = 0
# while j <= lenght:
#     for i in char:
#         num = ord(i)
#         if num  >=  48  and  num  <=  57 or num >= 97 and num <= 122:
#             a += 1
#         j += 1
# if a == j:
#     print("该字符串由小写字母和数字组成")
# else:
#     print("该字符串包含大写字母或是符号!")

# c = input("请输入数字");
# a = c[::2]
# b = c[1::2]
# print(a+b)


# arr = []
# length = int(input("请输入一个数的个数："))
# i = 0
# while i < length:
#     num = input("第 %d 字符是:" % (i+1))
#     arr.append(num)
#     i += 1
# arr.sort()
# index = int(length/2)
# print("中间的字符是:" + arr[index])


# arr=[]
# r = ""
# m = input("请输入字符串:")
# for string in m:
#     arr.append(string)
# last = arr[-1]
# arr.insert(0, last)
# arr.pop()
# for str in arr:
#     r=r+str
# print(r)

# message=print()
# count={}
# for character in message:
#     count.setdefault(character,0)
#     count[character]=count[character]+1
#
# print(count)

# import operator
# def count_each_char_sort_value(string):
#     res = {}
#     for i in string:
#         res[i] = res.get(i,0) + 1
#         res =sorted(res.items(),key= operator.itemgetter(1),reverse=True)
#         return res
#
# print(count_each_char_sort_value('dfgdfg'))

# content = input("请输入一个字符串:")
# res = {}
# for i in content:
#     res[i] = content.count(i)
# print(res)


# arr = []
#
# def count():
#     my_Str = input("请输入只包含字母的字符串：")
#     if my_Str.isalpha():
#         newStr = my_Str.lower()
#         for string in newStr:
#             arr.append(string)
#         a = {}
#         for i in arr:
#             if arr.count(i) >= 1:
#                 a[i] = arr.count(i)
#         print(a)
#     else:
#         print("输入的内容有误")
#
#
# count()
#
# x = str(input('请输入字符串:'))
# a = x[::2]
# b = x[1::2]
# print(a+b)
