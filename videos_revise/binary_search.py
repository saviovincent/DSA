import math


def digits():
    return int(math.log10(1234) + 1)


def search2d(arr, target):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == target:
                return (i, j)
    return -1


def bin_search(arr, target):
    i = 0
    j = len(arr)

    while i < j:

        mid = (i + j) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            j = mid - 1
        else:
            i = mid + 1

    return -1


def ceil_floor():
    pass


def smallest_ltr():
    pass


def first_last():
    pass


def infinite():
    pass


def peak_el_bitonic():
    pass


def find_in_bitonic():
    pass


def rotated_sorted():
    pass


def split_array_largest_sum():  # allocate no of pages
    pass


#####################

def count_el_in_sorted():
    pass


def times_array_is_rotated():
    pass


def peak_element():
    pass


def row_col_wise_sorted():
    pass


def search_in_sorted_matrix():
    pass


if __name__ == '__main__':
    print(bin_search([1, 2, 3, 4, 5], 1))
    # print(digits())
    # print(search2d([[1, 2, 3, 4], [1, 3, 5, 6]], 6))
