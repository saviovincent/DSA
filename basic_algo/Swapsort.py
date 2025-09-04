# used to find multiple duplicates and multiple missing from 1..N

def find(arr):
    i = 0
    while i < len(arr):
        if arr[i] != i + 1 and arr[arr[i] - 1] != arr[i]:
            swap(i, arr[i] - 1, arr)
        else:
            i += 1

    missing = []
    duplicates = []
    for i in range(0, len(arr)):
        if i != arr[i] - 1:
            missing.append(i + 1)
            duplicates.append(arr[i])
    return missing, duplicates


def swap(i1, i2, arr):
    arr[i1], arr[i2] = arr[i2], arr[i1]


if __name__ == '__main__':
    print(find([2, 3, 1, 5, 1]))
