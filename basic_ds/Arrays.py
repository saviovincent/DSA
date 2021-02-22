# test python lists

if __name__ == '__main__':
    # test single array

    arr = ["a", "b", "c"]

    arr.append("d")
    print(arr.pop(0))
    arr.remove("b")
    print(arr)

    # init array with default values

    arr = [True] * 10
    print(arr)
    arr[0] = "Test"
    print(arr)

    # 2d arrays
    arr = [[True for i in range(0, 5)] for j in range(0, 5)]
    print(arr)
    arr[0][0] = False
    print(arr)

    # do not use this declaration
    arr = [[True] * True] * 5
    print(arr)
