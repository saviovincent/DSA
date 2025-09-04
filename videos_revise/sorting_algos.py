"""
best case - O(n)
"""


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    return arr


"""
good for small lists
"""


def select_sort(arr):
    for i in range(len(arr)):
        key = find_min(arr[i:])
        arr[i], arr[i + key] = arr[i + key], arr[i]
    return arr


def find_min(arr):
    minm = 999
    key = -1
    for i in range(len(arr)):
        if minm > arr[i]:
            minm = arr[i]
            key = i
    return key


"""
best for already sorted array
best case - O(n)
"""


def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, 0, -1):
            if j < len(arr) and arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    rslt = [-1] * (len(left) + len(right))  # array indexing would fail if array empty
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            rslt[k] = left[i]
            i += 1
        else:
            rslt[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        rslt[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        rslt[k] = right[j]
        j += 1
        k += 1

    return rslt


def quick_sort_3(arr, l, h):
    if l < h:
        # pivot = partition(arr)
        left_pivot, right_pivot = three_way_partition(arr)
        if left_pivot: quick_sort(arr, l, left_pivot - 1)
        if right_pivot: quick_sort(arr, right_pivot + 1, h)
    return arr


def quick_sort(arr, l, h):
    if l <= h:
        pivot = partition(arr, l, h)
        quick_sort(arr, l, pivot - 1)
        quick_sort(arr, pivot + 1, h)
    else:
        return []
    return arr


def custom_sort():
    a = [1, 3, 0]
    a.sort()

    b = {
        'name': "savio",
        'sal': '100'
    }
    c = {
        "name": "prachi",
        'sal': '200'
    }
    d = [b, c]
    d.sort(reverse=True, key=myfunc)
    print(d)


def myfunc(el):
    return el['sal']


def partition(arr, start, last):
    """
    this partition scheme is hoare. It uses 2 pointers from both ends
    lomuto uses 1 pointer and starts from 1st el as pivot

    this is trivial quick sort and breaks for duplicates.

    3 way partition is done DNF to handles duplicates
    """

    pivot = arr[last]  # make last element as pivot

    i = start  # keeps track of item < pivot
    j = last - 1  # keeps track of item > pivot

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1  # increment i till el < pivot
        while i <= j and arr[j] > pivot:
            j -= 1  # decrement j till el > pivot

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]  # swap when contradicting el found
            i += 1
            j -= 1

    arr[i], arr[last] = arr[last], arr[i]  # move pivot to correct index i
    return i


def three_way_partition(arr):
    if arr:
        lt = curr = 0
        gt = len(arr) - 1
        pivot = arr[0]

        while curr < gt:
            if arr[curr] < pivot:
                arr[lt], arr[curr] = arr[curr], arr[lt]
                curr += 1
                lt += 1
            elif arr[curr] > pivot:
                arr[gt], arr[curr] = arr[curr], arr[gt]
                gt -= 1
            else:
                curr += 1
        print("savio")
        return lt, gt
    return None


def quick_select(arr, start, end, k):
    if start < end:
        pivot = partition(arr, start, end)
        if pivot < k - 1:
            return quick_select(arr, pivot + 1, end, k)
        elif pivot > k - 1:
            return quick_select(arr, start, pivot - 1, k)
        else:
            return arr[pivot]


if __name__ == '__main__':
    arr = [1, 2, 1, 1, 1, 2, 2, 2]
    # print(bubble_sort(arr))
    # print(select_sort(arr))
    # print(insertion_sort(arr))
    # print(custom_sort())
    # print(merge_sort(arr))
    print(quick_sort(arr, 0, len(arr) - 1))
    # print(partition(arr))
    # print(quick_select(arr, 0, len(arr), 3))
    # print(three_way_partition(arr))
