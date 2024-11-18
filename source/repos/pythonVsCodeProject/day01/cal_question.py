"""
输入两个数，计算他们+, -, *, /的结果
"""

num1 = float(input("输入一个数"))
num2 = float(input("输入一个数"))

operate = input("输入一个运算符(+, -, *, /):")

resuin = 0.0

isShow = True

if(operate == "+"):
    result = num1 + num2
elif(operate == "-"):
    result = num1 - num2
elif(operate == "*"):
    result = num1 * num2
elif(operate == "/"):
    result = num1 / num2;
else:
    isShow = False
    print("输入的运算符不正确")

if(not isShow):
    pass
else:
    print("result = %.1f" % result)
        
