import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 下载训练数据集
boston_housing = tf.keras.datasets.boston_housing
# 加载数据集，提取全部数据为训练集
(train_x, train_y), (test_x, test_y) = boston_housing.load_data(test_split=0)
x = np.array(train_x)
y = np.array(train_y)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
print("下载波士顿数据集，放在NumPy数组x、y中（x:属性，y:标记）")
print("变量x，类型：" + str(type(x)) + "，性状：" + str(x.shape) + ";\n \
    变量y，类型：" + str(type(y)) + "，形状：" + str(y.shape))

title_list = [
    "CRIM", "ZN", "INUDS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX",
    "PTRATIO", "B", "LSTAT"
]
print("波士顿房价数据集视化")
#设置画布的尺寸
plt.figure(figsize=(12, 12))
#执行循环体绘制子图
for i in range(13):
    #设置子图
    plt.subplot(4, 4, (i + 1))
    plt.scatter(x[:, i], y)
    #子图横坐标
    plt.xlabel(title_list[i])
    #子图纵坐标
    plt.ylabel("Price($1000's)")
    #设置标题
    plt.title(str(i + 1) + "." + title_list[i] + " - Price")
plt.tight_layout()
plt.suptitle("各个属性与房价的关系", x=0.5, y=1.02, fontsize=20)
plt.show()
#根据属性选择绘制属性-房价散点图
print("根据选择，输出对应属性的散点图")
for i in range(len(title_list)):
    print(str((i + 1)) + " -- " + title_list[i])
while True:
    num = input("请选择属性：")
    if str.isdigit(num) and 1 <= int(num) <= 13:
        num = int(num)
        plt.scatter(x[:, num - 1], y)
        plt.xlabel(title_list[num - 1])
        plt.ylabel("Price($1000's")
        plt.title(str(num) + "." + title_list[num - 1] + " - Price")
        plt.show()
        print("您选择的" + str(num) + "号属性" + title_list[num - 1] + "与房价的关系图如上")
        break
    else:
        print("您输入的不是数字或者范围不正确，请重新输入：")
