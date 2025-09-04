class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        if not points or not points[0]:
            return 0

        points.sort(key=lambda x: x[0])
        merged = [points[0]]

        for i in range(1, len(points)):
            prev = merged[-1]
            if prev[1] >= points[i][0]:
                merged[-1] = [max(points[i][0], prev[0]), min(points[i][1], prev[1])]
            else:
                merged.append(points[i])

        return len(merged)


if __name__ == '__main__':
    soln = Solution()
    print(soln.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
    print(soln.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
    print(soln.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
