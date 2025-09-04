class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j = j - 1
            else:
                i = i + 1
        return -1


if __name__ == '__main__':
    soln = Solution()
    print(soln.twoSum([-1, 0], 9))
