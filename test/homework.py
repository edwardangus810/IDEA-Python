students = [{"name": "阿土"},
            {"name": "小美"},
            {"name": "张三"}]


find_name = "阿土"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 %s" %find_name)
        break
else:
    print("抱歉，找不到 %s" %find_name)
print("循环结束")