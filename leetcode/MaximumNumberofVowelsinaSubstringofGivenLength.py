class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        i = j = vowels = 0
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = 0

        while j < len(s):
            if s[j] in vowel_set:
                vowels += 1

            if j - i + 1 < k:
                j += 1

            elif j - i + 1 == k:
                max_vowels = max(max_vowels, vowels)

                if s[i] in vowel_set:
                    vowels -= 1
                i += 1
                j += 1

        return max_vowels


if __name__ == '__main__':
    soln = Solution()
    print(soln.maxVowels("leetcode", 3))
