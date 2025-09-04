import math

if __name__ == '__main__':

    # print(math.log(10))
    a = 14380843
    b = 7
    # print(a & b)
    # print(a | b)
    # print(a ^ b)
    # print(a >> 1)
    # print(a << 1)
    # print(b & 1 == 0)
    # a = a ^ b
    # b = a ^ b
    # a = a ^ b
    # print(a)
    # print(b)

    count = 0
    while a != 0:
        a = a & (a - 1)
        count += 1
    print(count)
