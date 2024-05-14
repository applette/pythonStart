"""
Python中序列数据类型有字符串、列表list、元组tuple
列表和元组可存放不同类型的数据
序列的长度使用内置函数len()
"""
t1 = (1)
t2 = (1, )
print("t1=", t1, type(t1))
print("t2=", t2, type(t2))

print(len(t2))

list_stud = [160612, "张明", 18, [92, 76, 85]]
print(list_stud, "的长度是", len(list_stud), sep="")

# 列表的插入和删除
lst_1 = [1, 2, 3]
lst_1.append(4)
lst_1.insert(1, 5)
del lst_1[1]  #删除小标为1的元素

# 合并列表，可用extend()或+运算符
lst_2 = [5]
lst_1.extend(lst_2)
print(lst_1)

lst_1.reverse()  #将lst_1的元素原地逆序
lst_1.sort()  #将lst_1中的元素从小到大的顺序排列
"""
字典：keys()、values()、items()
和集合
"""
dic_student = {'name': '张明', 'sex': '男', 'age': 18}
for key in dic_student.keys():
    print(key, end=" ")

dic_student.pop('sex')  #删除字典中的指定元素
dic_student.clear()

set_2 = set("Python")
#集合中的元素是无序的，因此不能通过下标来访问
print(set_2)

set_3 = frozenset("Python")
print(set_3)  #创建不可变集合

# 函数，Python3.6 共提供了68个内置函数
# 自定义函数


def add_mul(a, b):
    add = a + b
    mul = a * b
    return add, mul


x, y = add_mul(1, 2)
