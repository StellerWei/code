def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b);

def main():
    num1 = 15
    num2 = 20
    print('最大公约数%d' % gcd(num1, num2))
    print('最小公倍数%d' % lcm(num1, num2))

if __name__ == '__main__':
    main()
