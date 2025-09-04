class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """

        if not firstList or not secondList:
            return []

        i = j = 0
        ans = []

        while i < len(firstList) and j < len(secondList):

            front = max(firstList[i][0], secondList[j][0])
            back = min(firstList[i][1], secondList[j][1])
            if back - front >= 0:
                ans.append([front, back])

            if firstList[i][1] > secondList[j][1]:  # discard event ending first
                j += 1
            else:
                i += 1

        return ans


if __name__ == '__main__':
    soln = Solution()
    print(soln.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
