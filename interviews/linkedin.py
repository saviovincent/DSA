def check(nums):

    # window_size = arr[0]  # 3
    # max_sum = arr[0]  # 3
    #
    # for i in range(1, len(arr) - 1):
    #     no = arr[i]  # 4
    #
    #     # if no < 0:
    #     #
    #     #     # if sum > current_no then i can keep negative element in my array
    #     #     window_size = arr[i]  # 3
    #     #     max_sum = arr[i]  # 3
    #     # else:
    #     window_size = max(no, window_size + no)  # 6
    #     max_sum = max(max_sum, window_size)  # 6
    #
    # return max_sum  # 4

    current_subarray = max_subarray = nums[0]

    # Start with the 2nd element since we already used the first one.
    for num in nums[1:]:
        # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)

    return max_subarray


if __name__ == '__main__':
    print(check([3, -1, 4]))
