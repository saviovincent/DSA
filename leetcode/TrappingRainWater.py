class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        maxL = [0] * len(height)
        maxR = [0] * len(height)
        water = [0] * len(height)

        maxL[0] = height[0]
        maxR[len(maxR) - 1] = height[len(height) - 1]

        for i in range(1, len(height)):
            if height[i] > maxL[i - 1]:
                maxL[i] = height[i]
            else:
                maxL[i] = maxL[i - 1]
        for i in range(len(height) - 2, -1, -1):
            if height[i] > maxR[i + 1]:
                maxR[i] = height[i]
            else:
                maxR[i] = maxR[i + 1]

        for i in range(0, len(height)):
            water[i] = min(maxL[i], maxR[i]) - height[i]
        return sum(water)


if __name__ == '__main__':
    soln = Solution()
    print(soln.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(soln.trap([2]))
