def test(arr, target):
    maps = {}
    rslt = []
    for i in range(len(arr)):
        if maps[arr[i]] in maps:
            maps[arr[i]] = maps[arr[i]] + 1
        else:
            maps[arr[i]] = 1

    for i in range(len(arr)):
        if target - arr[i] in maps:
            rslt


def add(arr, target):
    maps = {}
    rslt = []
    for i in range(0, len(arr)):
        if target - arr[i] in maps:
            rslt.append((i, maps[target - arr[i]]))
        else:
            maps[arr[i]] = i
    return rslt


if __name__ == '__main__':
    print(add([2, 4, 1, 3, 7], 5))
