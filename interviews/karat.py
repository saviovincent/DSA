def populate(arr):
    my_map = {}
    for i in range(0, len(arr)):
        if arr[i][0] in my_map:
            my_map[arr[i][0]].append(int(arr[i][1]))
        else:
            my_map[arr[i][0]] = [int(arr[i][1])]

    for i in my_map:
        tmp = my_map[i]
        my_map[i] = sorted(tmp)
    print(my_map)

    for i in my_map:
        if len(my_map[i]) < 3:
            continue
        else:
            count = 0
            for i in range(0000,2400,100):


if __name__ == '__main__':
    badge_times = [
        ["Paul",     "1355"],
        ["Jennifer", "1910"],
        ["John",      "835"],
        ["John",      "830"],
        ["Paul",     "1315"],
        ["John",     "1615"],
        ["John",     "1640"],
        ["Paul",     "1405"],
        ["John",      "855"],
        ["John",      "930"],
        ["John",      "915"],
        ["John",      "730"],
        ["John",      "940"],
        ["Jennifer", "1335"],
        ["Jennifer",  "730"],
        ["John",     "1630"],
        ["Jennifer",    "5"]
    ]

    """
    Expected output (in any order)
  John:  830  835  855  915  930
  Paul: 1315 1355 1405
    """
    print(populate(badge_times))
