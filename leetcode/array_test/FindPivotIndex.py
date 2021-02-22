class Solution(object):

    def pivotIndex(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        soln_arr = []

        for i, val in enumerate(nums):

            lsum = self.calcSum(nums, 0, i)
            rsum = self.calcSum(nums, i+1, len(nums))

            if lsum == rsum:
                soln_arr.append(i)

        if len(soln_arr):
            return soln_arr.pop(0)
        else:
            return -1

    def calcSum(self, arr, start, end):

        sum = 0
        for x in range(start, end):
            sum += arr[x]

        return sum
