'''
a_list = [1, 2, 3, 4, 5]

def square(num):
    return num**2


print(list(map(square, a_list)))
'''

# 方法二
result_list = map(lambda X: X**2,[1, 2, 3, 4, 5])
print(list(result_list))


# 2.求a_list = [4, 8, 15] 和 b_list = [5, 8, 9, 12]之和
a_list = [4, 8, 15]
b_list = [5, 8, 9, 12]
c_list = map(lambda x, y:x + y,[4, 8, 15],[5, 8, 9, 12])
print(list(c_list))