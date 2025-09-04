class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        return self.check(arr, start, set())

    def check(self, arr, start, my_set):

        if start in my_set:
            return False
        my_set.add(start)

        if start > len(arr) - 1 or start < 0:
            return False
        if arr[start] == 0:
            return True

        return self.check(arr, start + arr[start], my_set) or self.check(arr, start - arr[start], my_set)


if __name__ == '__main__':
    soln = Solution()
    print(soln.canReach([4, 2, 3, 0, 3, 1, 2], 5))
    print(soln.canReach([4, 2, 3, 0, 3, 1, 2], 0))
    print(soln.canReach([3, 0, 2, 1, 2], 2))
