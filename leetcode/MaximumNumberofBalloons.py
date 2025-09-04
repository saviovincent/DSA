from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        my_map1 = Counter("balloon")
        my_map2 = Counter(text)

        can_be_found = True
        count = 0

        while can_be_found:
            for i in my_map1:
                if i in my_map2 and my_map2[i] >= my_map1[i]:
                    my_map2[i] -= my_map1[i]
                else:
                    can_be_found = False

            if can_be_found:
                count +=1

        return count

if __name__ == '__main__':
    soln = Solution()
    print(soln.maxNumberOfBalloons("loonbalxballpoon"))