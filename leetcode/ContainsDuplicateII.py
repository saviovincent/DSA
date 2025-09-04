class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        maps = {}
        for i in range(len(nums)):

            if nums[i] in maps:
                j_idx = maps[nums[i]]
                if nums[i] == nums[j_idx] and abs(i - j_idx) <= k:
                    return True
                else:
                    maps[nums[i]] = i
            else:
                maps[nums[i]] = i
        return False


if __name__ == '__main__':
    soln = Solution()
    print(soln.containsNearbyDuplicate([1,0,1,1], 1))
