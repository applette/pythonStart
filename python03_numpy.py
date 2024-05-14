"""
NumPy:Numeric Python
提供了多维数组、矩阵的常用操作和一些高效的科学计算函数
底层运算通过C语言实现，处理速度快、效率高，适用于大规模多维数组
可以直接完成数组和矩阵运算，无需循环    
"""
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

boston_housing = tf.keras.datasets.boston_housing
(train_x, train_y), (test_x, test_y) = \
boston_housing.load_data(test_split=0) #提取出全部数据作为训练集
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

titles = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX",
    "PTRATIO", "B-1000", "LSTAT", "MEDV"
]

plt.figure(figsize=(5, 5))
for i in range(4):
    plt.subplot(2, 2, (i + 1))
    plt.scatter(train_x[:, i], train_y)
    plt.xlabel(titles[i])
    plt.ylabel("Price($1000's)")
    plt.title(str(i + 1) + "." + titles[i] + " - Price")

plt.tight_layout()
plt.suptitle("各个属性与房价的关系", x=0.5, y=1.02, fontsize=20)
plt.show()
