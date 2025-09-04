class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        i = j = 0
        summ = 0
        rslt = 0
        while j < len(nums):
            if summ + nums[j] < k:
                summ += nums[j]
            elif summ + nums[j] == k or nums[j] == k:
                rslt += 1
            elif summ + nums[j] > k:
                while summ > k:
                    summ -= nums[i]
                    i += 1

                summ += nums[j]
            j += 1
        return rslt


if __name__ == '__main__':
    soln = Solution()
    print(soln.subarraySum([1, 2, 1,2,1], 3))
