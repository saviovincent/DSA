class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort(key=lambda x: (x[0]))

        count = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):

            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                count += 1
                end = min(intervals[i][1], end)  # remove interval which ends later
        return count


if __name__ == '__main__':
    soln = Solution()
    print(soln.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(soln.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(soln.eraseOverlapIntervals([[1, 2], [2, 3]]))
