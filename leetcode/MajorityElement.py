class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        me = None
        count = 0
        for i in nums:
            if i == me:
                count += 1
            else:
                if count == 0:
                    me = i
                else:
                    count -= 1
        return me


if __name__ == '__main__':
    soln = Solution()
    print(soln.majorityElement([2,2,1,1,1,2,2]))
