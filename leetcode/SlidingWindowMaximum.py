class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        i = j = 0
        que = []
        ans = []

        while j < len(nums):

            if not que:
                que.append(nums[j])
            elif nums[j] > que[0]:
                que = [nums[j]]
            else:
                que.append(nums[j])

            if j - i + 1 < k:
                j += 1

            elif j - i + 1 == k:
                ans.append(que[0])
                if nums[i] == que[0]:
                    que.pop(0)
                i += 1
                j += 1

        return ans


if __name__ == '__main__':
    soln = Solution()
    # print(soln.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(soln.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
