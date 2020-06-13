#result = filter(lambda x:x % 2, [1, 2, 3, 4, 5])

#print(list(result))


sql = filter(lambda x:10 > x > 5,{12, 50, 8, 17, 65, 14, 9, 6, 14, 5})
print(tuple(sql))




# 求出列表的所有数字之和
'''
from functools import reduce
# func = lambda x, y:x + y
result = reduce(lambda x, y: x + y,[1, 2, 3, 4], 5)
print(result)
'''