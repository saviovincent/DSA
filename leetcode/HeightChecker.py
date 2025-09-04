class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        arr = sorted(heights)
        i = 0
        count = 0
        while i < len(heights):
            if arr[i] != heights[i]:
                count += 1
            i += 1
        return count


if __name__ == '__main__':
    soln = Solution()
    print(soln.heightChecker([5,1,2,3,4]))
