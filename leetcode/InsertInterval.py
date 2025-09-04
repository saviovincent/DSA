class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        ans = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        ans.append(newInterval)
        return ans


if __name__ == '__main__':
    soln = Solution()
    print(soln.insert([[1, 3], [6, 9]], [2, 5]))
    print(soln.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
