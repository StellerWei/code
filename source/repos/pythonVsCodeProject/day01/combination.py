"""
求 x1 + x2 + x3 + x4 = 8有多少组正数解 利用排列组合

"""

m = 7
n = 3

fm = 1
for num in range(1, m+1):
    fm*=num
fn = 1
for num in range(1, n+1):
    fn*=num

fm_n = 1
for num in range(1, m-n+1):
    fm_n*=num
print(fm // fn // fm_n)

# 使用函数来封装计算阶乘的过程
def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num+1):
        result *= n
    return result

num1 = 7
num2 = 3
print(fac(num1) // fac(num2) // fac(num1-num2))
