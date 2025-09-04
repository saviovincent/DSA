class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        j = 1
        count = 1

        while j < len(nums):

            if nums[j] == nums[i] and count < 2:
                count += 1
                j += 1
                i += 1

            elif nums[j] == nums[i] and count == 2:

                count = 0
                while nums[j] == nums[i]:
                    j += 1
                nums[i+1] = nums[j]
                j += 1
                i += 1
                count += 1

            elif nums[j] != nums[i]:
                count = 1
                j += 1
                i += 1

        print(nums)
        return i


if __name__ == '__main__':
    soln = Solution()
    # print(soln.removeDuplicates([1,1,1,2,2,3]))
    print(soln.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
