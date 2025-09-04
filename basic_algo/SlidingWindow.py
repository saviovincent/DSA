class SlidingW:

    # fix window size
    def MaximumSumSubarrayofsizeK(self, arr, k):
        i = j = sum_el = max_sum = 0

        while j < len(arr):
            sum_el = sum_el + arr[j]

            # need to reach correct window size
            if j - i + 1 < k:
                j = j + 1

            # once reached perform calc.
            elif j - i + 1 == k:
                max_sum = max(max_sum, sum_el)
                sum_el = sum_el - arr[i]
                i = i + 1
                j = j + 1
        return max_sum

    def FirstNegativeNumberineveryWindowofSizeK(self, arr, k):
        i = j = 0
        my_list = []
        result = []

        while j < len(arr):
            if arr[j] < 0:
                my_list.append(arr[j])

            if j - i + 1 < k:
                j = j + 1

            elif j - i + 1 == k:
                if not my_list:
                    result.append(None)
                else:
                    result.append(my_list[0])
                    if arr[i] == my_list[0]:
                        my_list.pop(0)

                i = i + 1
                j = j + 1

        return result

    # variable size window
    # only works with positive integers
    def LargestSubarrayofsumK(self, arr, sum):
        i = j = 0
        ws = 0
        total = 0

        while j < len(arr):
            total = total + arr[j]

            if total < sum:
                j = j + 1

            elif total == sum:
                ws = max(ws, j - i + 1)

            elif total > sum:
                while total > sum:
                    total = total - arr[i]
                    i = i + 1
        return ws


if __name__ == '__main__':
    sw = SlidingW()
    print(sw.MaximumSumSubarrayofsizeK([1, 2, 3, -1, 0, -2, 1], 2))
    print(sw.FirstNegativeNumberineveryWindowofSizeK([1, 2, 3, -1, 0, -2, 1], 3))
    print(sw.LargestSubarrayofsumK([3, 2, 1, 1, 1, 1, 5], 5))
