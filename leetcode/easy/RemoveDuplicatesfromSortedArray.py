class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums)

        if j == 0 or j == 1:
            return j

        while i < j and i+1 < j:
            if nums[i] == nums[i + 1]:
                tmp = nums.pop(i + 1)
                nums.append(tmp)
                j = j - 1
            else:
                i = i + 1

        return i+1

        # for j in range(1, len(nums)):
        #     if nums[i] != nums[j]:
        #         i = i+1
        #         nums[i] = nums[j]
        # return i +1 , nums


if __name__ == '__main__':
    soln = Solution()
    print(soln.removeDuplicates([1,1,2,2,3]))
