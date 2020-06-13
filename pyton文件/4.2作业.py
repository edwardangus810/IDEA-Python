# def getMax():
#     n1 = int(input("请输入第1个数:"))
#     n2 = int(input("请输入第2个数:"))
#     n3 = int(input("请输入第3个数:"))
#     t = 0
#     if n1 > n2:
#         t = n1
#     else:
#         t = n2
#     if t > n3:
#         return "其中最大值为:" + str(t)
#     else:
#         return "其中最大值为:" + str(n3)
#
#
# maxValue = getMax()
# print(maxValue)



# def ispositive(numb):
#     try:
#         float(numb)
#     except:
#         return False
#     else:
#         if float(numb) <= 0:
#             return False
#         else:
#             return True
# #直角三角形判断
# def ispythagoras(a,b,c):
#     if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#         return True
#     else:
#         return False
#
# num1 = input("请输入第一条边:")
# while not ispositive(num1):
#     num1 = input("这不是一个正数，请再次输入:")
#
# num2 = input("请输入第二条边:")
# while not ispositive(num2):
#     num2 = input("这不是一个正数，请再次输入:")
#
# num3 = input("请输入第三条边:")
# while not ispositive(num3):
#     num3 = input("这不是一个正数，请再次输入:")
#
# num1 = float(num1)
# num2 = float(num2)
# num3 = float(num3)
#
# if num1 + num2 > num3 and num2 + num3 > num1 and num1 + num3 > num2:
#     if num1 == num2 == num3:
#         print("%.2f\n%.2f\n%.2f\n可以组成等边三角形" % (num1,num2,num3))
#     elif num1 == num2 or num2 == num3 or num1 == num3:
#         if ispythagoras(num1,num2,num3):
#             print('%.2f\n%.2f\n%.2f\n可以组成等腰直角三角形' % (num1,num2,num3))
#         else:
#             print('%.2f\n%.2f\n%.2f\n可以组成等腰三角形' % (num1,num2,num3))
#     elif ispythagoras(num1,num2,num3):
#         print('%.2f\n%.2f\n%.2f\n可以组成直角三角形' % (num1,num2,num3))
#     else:
#         print('%.2f\n%.2f\n%.2f\n可以组成普通三角形' % (num1,num2,num3))
# else:
#     print('%.2f\n%.2f\n%.2f\n不能组成三角形' % (num1,num2,num3))


