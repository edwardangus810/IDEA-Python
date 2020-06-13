# 用来保存学生的所有信息
stuInfos = []
# 全局变量
sno = ""
sName = ""
sAge = ""
sPhone = ""


# 打印功能提示
def print_menu():
    print("=" * 42)
    print("*" * 10 + "简单的学生信息管理系统" + "*" * 10)
    print("=" * 42)
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.给定学号查询学生信息")
    print("4.显示当前所有学生信息")
    print("5.保存系统")
    print("0.退出系统")
    print("=" * 42)


# （用户输入）获取一个学生的信息
def getInfo():
    global newSno
    global newSname
    global newSage
    global newSphone
    # 这三个是全局变量，要对其进行修改，则要先声明
    newSno = input("请输入学生的学号：")
    newSname = input("请输入学生的姓名：")
    newSage = input("请输入学生的性别(男/女)：")
    newSphone = input("请输入手机号码:")
    # 通过列表的形式把数据整合成一个整体，然后返回
    return [newSno, newSname, newSage, newSphone]


# 添加学生信息
def addStuInfo():
    result = getInfo()
    newInfo = {}
    newInfo['sno'] = result[0]
    newInfo['sName'] = result[1]
    newInfo['sAge'] = result[2]
    newInfo['sPhone'] = result[3]
    stuInfos.append(newInfo)


# # 删除学生信息
def deleteStuInfo():
    stuId = input("请输入要查询学生的学号：")
    print("=" * 30)
    print("学生的信息如下：")
    print("  学号      姓名     性别      手机号码")
    for tempInfo in stuInfos:
        if stuId == tempInfo['sno']:
            stuInfos.remove(tempInfo['sno'])
            stuInfos.remove(tempInfo['sName'])
            stuInfos.remove(tempInfo['sAge'])
            stuInfos.remove(tempInfo['sPhone'])


# 给定学号查询学生信息
def selectStuInfo():
    stuId = input("请输入要查询学生的学号：")
    print("=" * 30)
    print("学生的信息如下：")
    print("  学号      姓名     性别      手机号码")
    for tempInfo in stuInfos:
        if stuId == tempInfo['sno']:
            print("%d      %s       %s     %s         %s" % (
                tempInfo['sno'], tempInfo['sName'], tempInfo['sAge'], tempInfo['sPhone']))
            break


# 显示当前所有学生信息
def selectAllStuInfo():
    print("=" * 30)
    print("学生的信息如下：")
    print("序号   学号      姓名     性别       手机号码")
    i = 1
    for tempInfo in stuInfos:
        print("%d      %s       %s     %s         %s" % (
            i, tempInfo['sno'], tempInfo['sName'], tempInfo['sAge'], tempInfo['sPhone']))
        i += 1


# 保存当前所有的学生信息到文件中
def save_to_file():
    file = open("backup.data", "w")
    file.write(str(stuInfos))
    file.close()


# 数据恢复
def recover_data():
    global student_infos
    file = open("backup.data")
    content = file.read()
    student_infos = eval(content)
    file.close()


# 主函数程序
def main():
    recover_data()
    while True:
        # 打印提示信息
        print_menu()
        key = input("请输入你要选择的操作：")
        if key == '1':
            # 添加学生信息
            addStuInfo()
        elif key == "2":
            deleteStuInfo(stuInfos)
        elif key == "3":
            # 给定学号查询学生信息
            selectStuInfo()
        elif key == '4':
            # 显示当前所有学生信息
            selectAllStuInfo()
        elif key == '5':
            save_to_file()
        elif key == '0':
            quit_confirm = input("退出了(Yes  or No): ")
            if quit_confirm == "Yes":
                break
            else:
                print("输入有误")

    recover_data()
