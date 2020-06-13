# 新建一个列表，用来保存学生所有的信息
student_infos = []
sName = " "
sSex = " "
sPhone = " "
# 定义一个打印功能菜单的函数
def print_menu():
    print("=" * 30)
    print("学生管理系统  V1.0")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.显示所有学生信息")
    print("0.退出系统")
    print("=" * 30)



# 添加一个学生信息

def add_info():
    global  new_name
    
    new_name = input("请输入学生的名字:")
    new_sex = input("请输入新学生的性别: (男/女)")
    new_phone = input("请输入新学生的手机号码:")
    new_infos = {}
    new_infos["name"] = new_name
    new_infos["sex"] = new_sex
    new_infos["phone"] = new_phone
    # print(new_infos)
    student_infos.append(new_infos)
    print(student_infos)


add_info()


# 删除一个学生信息

def del_info(student):
    del_number = int(input("请输入要删除的序列号:")) - 1
    del student[del_number]
    print(student_infos)


del_info(student_infos)




# 修改一个学生信息

def modeify_info():
    student_id = int(input("请输入需要修改的学生序号:")) - 1
    new_name = input("请输入学生的名字:")
    new_sex = input("请输入新学生的性别: (男/女)")
    new_phone = input("请输入新学生的手机号码:")
    student_infos[student_id]["name"] = new_name
    student_infos[student_id]["sex"] = new_sex
    student_infos[student_id]["phone"] = new_phone
    print(student_infos)


modeify_info()


# 显示一个学生

def show_infos():
    print("=" * 30)
    print("学生的信息如下:")
    print("=" * 30)
    print("序号    姓名   性别  手机号码     ")
    i = 1
    for temp in student_infos:
        print("%d     %s    %s    %s" %(i, temp["name"], temp["sex"], temp["phone"]))
        i += 1


show_infos()


def main():
    while True:
        print_menu()
        key = input("请输入功能对应的数字:")
        if key == '1':
            add_info()
        elif key == '2':
            del_info(student_infos)
        elif key == '3':
            modeify_info()
        elif key == '4':
            show_infos()
        elif key == '0':
            quit_confirm = input("亲，真的要退出吗？(Yes or No):")
            if quit_confirm == "Yes":
                break
            else:
                print("输入有误，请重新输入！")


