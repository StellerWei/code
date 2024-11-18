# 打印直角三角形
for i in range(1, 6):
    print('*' * i)

# 打印等腰三角形
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2 * i - 1))

# 打印倒立直角三角形
for i in range(5, 0, -1):
    print('*' * i)

# 打印倒立等腰三角形
for i in range(5, 0, -1):
    print(' ' * (5 - i) + '*' * (2 * i - 1))
