class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort(key=lambda x: (x[0], -x[1]))  # need interval ending later first so -1
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][0] <= intervals[i][0] and res[-1][1] >= intervals[i][1]:
                continue
            else:
                res.append(intervals[i])
        return len(res)


if __name__ == '__main__':
    soln = Solution()
    print(soln.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
