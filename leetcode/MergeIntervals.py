class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        if not intervals or not intervals[0]:
            return intervals

        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]

        for i in range(1, len(intervals)):

            last_end = ans[len(ans) - 1]
            curr = intervals[i]

            if last_end[1] >= curr[0]:
                ans[len(ans) - 1] = [min(last_end[0], curr[0]), max(last_end[1], curr[1])]
            else:
                ans.append(curr)

        return ans


if __name__ == '__main__':
    soln = Solution()
    print(soln.merge([[1, 4], [4, 5]]))
    print(soln.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
