class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        if not intervals or not intervals[0]:
            return 0

        times = []
        for i in range(len(intervals)):
            times.append((intervals[i][0], 1))
            times.append((intervals[i][1], -1))

        times.sort(key=lambda x: (x[0], x[1]))  # this is imp here

        count = 0
        maxm = float('-inf')

        for i in times:
            count += i[1]
            maxm = max(maxm, count)
        return maxm


if __name__ == '__main__':
    soln = Solution()
    # print(soln.minMeetingRooms([[0,30],[5,10],[15,20]]))
    print(soln.minMeetingRooms([[13, 15], [1, 13]]))
