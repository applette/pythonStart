"""
此为多行注释
本程序主要讲述基本的python语法，input输入，print输出，format格式化输出
string操作等
"""
stringInput = input("Please input some words:")
numInput = int(stringInput)
num2 = 2
num3 = 3
#此为单行注释，\可实现表达式跨行
sum1 = numInput + num2 + \
    num3
print("您输入的%s是:%d" % ("整数", numInput), end="!\n")
if numInput > 0:
    print("numInput是正数")
else:
    print("numInput可能是0或负数")

print("今天是%d 年%d 月%d 日" % (2019, 5, 18))
print('第一个数字是%.5f,第二个数字是%d' % (0.678, 10))
print("今天是{}年{}月{}日".format(2019, 5, 18))
print('{0} {1} {0}'.format('hello', 'world'))
print('她叫{name},今年{age}岁.'.format(age=10, name='Lucy'))

print("""
这是一个文档字符串
支持跨越多行
使用双重双引号或单引号
""")

print(7 / 2)
print(7 // 2)

print("重要的话说三遍！" * 3)
print("-" * 40)
print(" " * 15 + "这是分割线")
print("-" * 40)

a, b = 3, 4
print(a if a > b else b)

#in为成员运算符，以下2例用于序列对象或可迭代对象Iterable
str = "Hello"
print('H' in str)

for i in range(10):
    print(i)
