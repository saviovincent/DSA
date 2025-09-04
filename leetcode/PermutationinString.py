from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        i = j = 0
        maps = Counter(s1)
        count = len(maps)

        while j < len(s2):

            if s2[j] in maps:
                maps[s2[j]] -= 1
                if maps[s2[j]] == 0:
                    count -= 1

            if j - i + 1 < len(s1):
                j += 1

            elif j - i + 1 == len(s1):

                if count == 0:
                    return True

                if s2[i] in maps:
                    if maps[s2[i]] == 0:
                        maps[s2[i]] += 1
                        count += 1
                    else:
                        maps[s2[i]] += 1

                i += 1
                j += 1
        return False


if __name__ == '__main__':
    soln = Solution()
    print(soln.checkInclusion("abc", "bbbca"))  # map - a   string - 'dcd' da
    print(soln.checkInclusion("adc", "dcda"))  # map - a   string - 'dcd' da
    print(soln.checkInclusion("ab", "eidboaoo"))
    print(soln.checkInclusion("hello", "leoooleh"))

    """
    anagram def - same chars + same quantity + continous
    This approach needs to fall to negative
    oooll
    """
