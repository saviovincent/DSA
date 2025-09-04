from collections import defaultdict
class Solution(object):
    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     maps = {}
    #     for i in range(len(nums)):
    #         if target - nums[i] in maps:
    #             return [i, maps[target - nums[i]]]
    #         else:
    #             maps[nums[i]] = i
    #     return []

    def two_sum(self, nums, target):
        maps = defaultdict(list)
        ans = []
        for i in range(len(nums)):
            if target - nums[i] in maps:
                ans.append([i, maps[target - nums[i]]])
                maps[nums[i]].append(i)
            else:
                maps[nums[i]].append(i)
        return ans

if __name__ == '__main__':
    soln = Solution()
    print(soln.two_sum([2, 7, 2, 7], 9))
    # print(soln.threeSum([-1, 0, 1, 2, -1, -4]))
