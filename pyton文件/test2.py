'''# 1、定义变量和列表
arr = []
length = int(input("请输入字符串的长度："))
# 2、遍历元素并追加到列表中
i = 0
while i < length:
    num = input("第 %d 字符是:" % (i + 1))
    arr.append(num)
    i += 1
arr.sort()
# 3、对列表进行操作
index = int(length/2)
print(arr[index])
'''

# number = input("请输入数字:")
# index = number[int(len(number)/2)]
# print(index)

# info = [1, 2, 3, 4, 5]
# info.sort(reverse=True)
# print(info)
#
# b = sorted(info, reverse=True)
# print(b)


# str = 'Training Project'
# print(str.upper())  # 将所有字符串中的小写字母转换为大写字母
# print(str.lower())  # 把所有字符中的大写字母转为小写字母
# print(str.capitalize())  # 把第一个字母转化为大写字母，其余小写
# print(str.title())  # 把每个单词的第一个字母转化为大写，其余小写


# a = float(input('第一条边长:'))
# b = float(input('第二条边长:'))
# c = float(input('第三条边长:'))
# p = (a + b + c) / 2
# s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(p)        # 三角形半周长
# print(s)        # 三角形面积


s = print('请输入一行字符串: \n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters = 1
    elif c.isalpha():
        space += 1
    elif c.isalpha:
        digit += 1
    else:
        others += 1
print('char=%d,apace=%d,digit=%d,others=%d' % (letters, space, digit, others))