class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # for i in range(1, len(height)):
        #     for j in range(i + 1, len(height)):
        #         area = (j - i) * min(height[i], height[j])
        #         if max < area:
        #             max = area
        # return max

        max = 0
        height.insert(0, 0)
        i = 1
        j = len(height) - 1

        while i < j:
            area = (j - i) * min(height[i], height[j])
            if max < area:
                max = area

            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1

        return max


if __name__ == '__main__':
    soln = Solution()
    print(soln.maxArea([1,8,6,2,5,4,8,3,7]))
