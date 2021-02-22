# recursion
def triple_step_rec(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return triple_step_rec(n - 1) + triple_step_rec(n - 2) + triple_step_rec(n - 3)

#dp
def triple_step_dp(n):
    arr = [0] * n
    arr[0] = 1
    arr[1] = 2
    arr[2] = 4

    for i in range(3, n):
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

    return arr[n-1]


if __name__ == '__main__':
    print(triple_step_rec(50))
    print(triple_step_dp(50))
