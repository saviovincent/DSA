class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # brute force
        # end = len(nums)
        # index = []
        # my_map = {}

        # for i in range(end):
        #     for j in range(i+1, end):
        #         if nums[i] + nums[j] == target:
        #             index.append(i)
        #             index.append(j)
        # return index

        # hashmap 1 pass

        # for i in range(end):
        #     no_to_find = target - nums[i]
        #     if no_to_find in my_map:
        #         index.append(my_map[no_to_find])
        #         index.append(i)
        #     else:
        #         my_map[nums[i]] = i
        # return index

        maps = {}
        for i in range(len(nums)):
            if target - nums[i] in maps:
                return [i, maps[target - nums[i]]]
            else:
                maps[nums[i]] = i
        return []


if __name__ == '__main__':
    soln = Solution()
    arr = [2, 7, 9, 11]
    print(soln.twoSum(arr, 10))
