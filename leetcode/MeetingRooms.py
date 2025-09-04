class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """

        if not intervals or not intervals[0]:
            return True

        intervals.sort(key=lambda x: x[0])

        end = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < end:
                return False
            else:
                end = intervals[i][1]
        return True


if __name__ == '__main__':
    soln = Solution()
    print(soln.canAttendMeetings([[]]))
