from collections import Counter


class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False

        maps = Counter(hand)
        maps = dict(sorted(maps.items()))

        for i in maps:

            while maps[i] > 0:
                min_el = i

                # try creating groups
                for j in range(min_el, min_el + groupSize):
                    if j not in maps:
                        return False
                    else:
                        maps[j] -= 1
        return True


if __name__ == '__main__':
    soln = Solution()
    print(soln.isNStraightHand([8,6,5,7,9], 5))
