"""
函数基本介绍

1. 为完成某一功能的程序指令(语句)的集合，称为函数。
2. 在python中，函数分为：系统函数、自定义函数(见python文档)。

函数的好处
1. 提高代码的复用性
2. 可以将实现的细节封装起来，然后供其他用户来调用
"""


def funMax(a, b):
    return a if a > b else b

c =funMax(1, 2)

print(c)
