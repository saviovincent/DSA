class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.merge_sort(nums)

    def merge(self, left, right):
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

    def merge_sort(self, arr):
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)


if __name__ == '__main__':
    soln = Solution()
    print(soln.merge_sort([1, 2, 2, 1]))
