import math


def magic():
    n = 3

    ans = 0
    power = 5
    while n > 0:
        last = n & 1
        ans += power * last
        n = n >> 1
        power = power * 5

    print(ans)


def single_no2():
    pass


def prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def sieve(n):
    arr = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n))):
        if arr[i]:
            for j in range(i * 2, n + 1, i):
                arr[i] = False

    for i in range(2, n + 1):
        if arr[i]:
            print(i)


def sqrt(n):
    root = 0
    prec = 2
    incr = 0.1
    s = 0
    e = n
    while s < e:
        mid = (s + e) // 2
        root = mid
        if mid * mid == n:
            return root
        if mid * mid > n:
            e = mid - 1
            root = e
        else:
            s = mid + 1
            root = s

    for i in range(0, prec):
        while root * root <= n:
            root = root + incr
        root = root - incr
        incr = incr // 10

    return root


def factors(no):
    ans = []
    for i in range(1, int(math.sqrt(no))):
        if no % i == 0:
            ans.append(i)
            ans.append(no // i)
    print(sorted(ans))


def xor_0ton(no):
    if no % 4 == 0:
        return no
    elif no % 4 == 1:
        return 1
    elif no % 4 == 2:
        return no + 1
    elif no % 4 == 3:
        return 0


def clear_range_of_bits(no, i, j):
    pass


if __name__ == '__main__':
    print(xor_0ton(10044354))
    # magic()
    # print(prime(37))
    # print(sieve(40))
    # print(sqrt(34))
    # print(factors(50))
