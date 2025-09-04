from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        sets = set()
        counter = Counter(arr)
        for i in counter:
            if counter[i] in sets:
                return False
            else:
                sets.add(counter[i])
        return True

if __name__ == '__main__':
    soln = Solution()
    print(soln.uniqueOccurrences([1,2]))