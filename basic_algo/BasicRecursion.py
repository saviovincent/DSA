def count(no):
    if no <= 0:
        return 0
    a = no % 10

    if a == 8 and no // 10 % 10 == 8:
        return 2 + count(no // 10)
    elif a == 8:
        return 1 + count(no // 10)
    else:
        return 0 + count(no // 10)


def countX(strl):
    if len(strl) == 0:
        return ""
    elif strl[0] == 'x':
        return "" + countX(strl[1:])
    else:
        return strl[0] + countX(strl[1:])


def index(arr, ind):
    if len(arr) == ind:
        return False
    elif arr[ind] == arr[0] * 10:
        return True
    else:
        return index(arr, ind + 1)
    return False


def add(strl, var, tar):
    if len(strl) == 0:
        return tar + var
    elif strl[0] == 'x':
        var = var + 'x'
    else:
        tar = tar + strl[0]
    return add(strl[1:], var, tar)


if __name__ == '__main__':
    # print(add("xxhixx", "", ""))

    arr = [100, 80, 60, 70, 60, 75, 85]
    my = []

    for i in range(len(arr)):
        count = 0
        for j in range(i, 0, -1):
            if arr[j - 1] < arr[i]:
                count = count + 1
            else:
                break
        my.append(count)
    print(my)
