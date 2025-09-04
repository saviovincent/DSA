from collections import Counter


class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if len(nums) % k != 0:
            return False

        maps = Counter(nums)
        maps = dict(sorted(maps.items()))

        for i in maps:

            while maps[i] > 0:
                min_el = i

                # try creating groups
                for j in range(min_el, min_el + k):
                    if j not in maps:
                        return False
                    else:
                        maps[j] -= 1
        return True


if __name__ == '__main__':
    soln = Solution()
    print(soln.isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], 4))
