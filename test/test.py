'''
f1 = open('1803_01.txt', 'w')
f2 = open('1803_02.txt', 'w')
f3 = open('1803_03.txt', 'w')
f4 = open('1803_04.txt', 'w')

f1.close()
f2.close()

import os
# os.rename('1803_01.txt', 'jsj1803_01.txt')
# os.remove('1803_02.txt')
# os.remove('jsj1803_01.txt')
'''

# import os
# os.mkdir("张三")


# import os
# path2 = os.getcwd()
# print(path2)


# # 获取目录列表
# import os
# os.listdir('../')
# cwd = os.getcwd()
# print(cwd)
# list_os = os.listdir('./')
# print(list_os)

# 删除文件夹
# import os
# os.rmdir('张三')

# # 批量修改文件名
# import os
# flag = 1    # 1表示添加标志  2表示删除标志
# folder_name = './'
# # 获取指定路径的所有文件名字
# dir_list = os.listdir(folder_name)
# # 遍历出所有文件名字
# for name in dir_list:
#     print(name)
#     if flag == 1:
#         new_name = ' ' + name
#     elif flag == 2:
#         number = len(' ')
#         new_name = name[number:]
#     print(new_name)
#     os.rename(folder_name + name, folder_name + new_name)

'''
try:
    print("-" * 30)
    filst_number = input("请输入第一个数:")
    second_number = input("请输入第二个数:")
    print(int(filst_number) / int(second_number))
    print("-" * 30)
except ZeroDivisionError:
    print("第二个数不能为0")
    print("-" * 30)
except ValueError:
    print("第二个数不能为字母")
    print("_" * 30)
    '''

'''
try:
    print("-" * 30)
    first_number = input("请输入第一个数:")
    second_number = input("请输入第二个数:")
    print(int(first_number) / int(second_number))
    print("-" * 30)
except (ZeroDivisionError,ValueError):
    print('第二个数既不能为0，也不能为字母')
'''
'''
try:
    print("-" * 30)
    first_number = input("请输入第一个数:")
    second_number = input("请输入第二个数:")
    print(int(first_number) / int(second_number))
    print("-" * 30)
except (ZeroDivisionError, ValueError) as result:
    print('捕获的异常为:%s' % result)
'''
'''
try:
    print("-" * 30)
    first_number = input("请输入第一个数:")
    second_number = input("请输入第二个数:")
    print(int(first_number) / int(second_number))
    print("-" * 30)
except ZeroDivisionError:
    print('第二个数字不能为0……')
except ValueError:
    print('第二个数字不能为字母……')
'''

'''
try:
    print("-" * 30)
    first_number = input("请输入第一个数:")
    second_number = input("请输入第二个数:")
    print(int(first_number) / int(second_number))
    print("-" * 30)
except (ZeroDivisionError, ValueError) as result:
    print('捕获的异常为:%s' % result)
else:
    print('程序运行正常，没有捕获到异常')
finally:
    print('程序终止')
'''

# with open('test.txt') as file:
#     print('with 开始了')
#     try:
#         file.write('hello9\n')
#     except Exception as result:
#         print('捕获的异常为:%s' % result)
#     for line in file:
#         print(line, end='')
#     print('with 结束了， 文件的关闭状态为:%s' % file.closed)
#
# # with语句结束后，会自动关闭打开的资源
# print('with 语句之后，文件的关闭状态时: %s' % file.closed)
# print('程序结束了')

'''
try:
    with open('test.txt') as file:
        print('with开始了')
        file.write('hello9\n')
        for line in file:
            print(line, end='')

except:
    print('处理异常')
print('with语句之后，文件的关闭状态为: %s'% file.closed)
'''
'''
# 断言语句
# 对条件进行判断，与其让程序在运行中崩溃，不如在遇到不满足的条件下就报出异常
age = int(input('请输入年龄:'))
try:
    assert age >= 18, '年龄要求大于18岁'
except Exception as result:
    print('捕获的异常为:%s' % result)
finally:
    print('程序终止')
'''
'''
class HeightException(Exception):
    pass
try:
    height = int(input("请输入您的身高："))
    if height<30 or height>250:
        raise HeightException
    weight = int(input("请输入您的体重："))
    weightS = height-100
    if weight > weightS and weight-weightS < 0.05*weightS:
        print("体重达标")
    elif weight < weightS and weightS-weight < 0.05*weightS:
        print("体重达标")
    else:
        print("体重不达标")
except HeightException:
    print("您输入的身高有误")
'''

'''
try:
    score = int(input("请输入学生的成绩："))
    if score >= 90 and score <= 100:
        print("A:优秀")
    elif score >= 80 and score < 90:
        print("B:良好")
    elif score >= 60 and score < 80:
        print("C:合格")
    else:
        assert score > 60, "D:不及格"
except Exception as result:
    print("低于60分：\n", result)
'''

# # 输入用户年龄
# age = int(input("请输入年龄："))
#
# # 判断用户输入的年龄是否18岁
# if age >= 18:
#     # 如果满18岁可以进入网吧
#     print("您已经满18岁，欢迎来网吧嗨皮")
# else:
#     # 如果没有满18岁回家写作业
#     print("回家写作业吧")


# # 确定数字的位数
# digits = input('请输入数字：',)
# if len(digits) > 5:
#     print('over length ！')
# else:
#     print('这是一个 ', len(digits), '位数')
# # 迭代求出每一位的数字
# intDigits = int(digits)
# intDigits = intDigits * 10
# for i in range(len(digits)):
#     intDigits = intDigits // 10
#     i = i + 1
#     print(intDigits % 10)

