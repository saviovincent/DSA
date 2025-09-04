class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # maps = {}
        # for i in range(len(wordsDict)):
        #     if wordsDict[i] in maps:
        #         maps[wordsDict[i]].append(i)
        #     else:
        #         maps[wordsDict[i]] = [i]
        #
        # minm = float('inf')
        #
        # for i in maps[word1]:
        #     for j in maps[word2]:
        #         minm = min(minm, abs(i - j))
        # return minm

        w1 = w2 = -1
        minm = float('inf')
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                w1 = i
            elif wordsDict[i] == word2:
                w2 = i

            if w1 != -1 and w2 != -1:
                minm = min(minm, abs(w1 - w2))
        return minm


if __name__ == '__main__':
    soln = Solution()
    print(soln.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))
