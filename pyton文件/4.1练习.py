# s = input('请输入一行字符串: \n')
# letters = 0
# space = 0
# digit = 0
# others = 0
# for c in s:
#     if c.isalpha():
#         letters += 1
#     elif c.isspace():
#         space += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         others += 1
# print('char=%d,apace=%d,digit=%d,others=%d' % (letters, space, digit, others))


# num = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != j and i != k and i != k:
#                 s = i + j * 10 + k * 100
#                 if s >=100 and s <= 999:
#                     num += 1
#                     print(s)
# print('总数:', num, "个")


# numberList = [1, 2, 3, 4]
# complexLost=[]
# def permutationNum():
#     for i in numberList:
#         for j in numberList:
#             for k in numberList:
#                 if i!=j and k != j and i!=k:
#                     complexLost.append(str(i)+str(j)+str(k))
#     print("共有{}种组合，分别为".format(len(complexLost),complexLost))
# permutationNum()


num_list = [1, 2, 3, 4]
num_count = 0
for a in num_list:
    for b in num_list:
        for c in num_list:
            if a == b or b == c or a == c:
                continue
            print("{}{}{}".format(a, b, c))
            num_count += 1
print("一共有: %d" %num_count +"个")
