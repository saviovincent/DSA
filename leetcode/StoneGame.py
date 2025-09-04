class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return self.helper(piles, 0, 0)

    def helper(self, piles, alice_score, bob_score):
        if not piles:
            return alice_score > bob_score

        return self.helper(piles[1:], alice_score + piles[0], bob_score) or self.helper(piles[:-1], alice_score + piles[
            len(piles) - 1],
                                                                                        bob_score) or \
            self.helper(piles[1:], alice_score, bob_score + piles[0]) or self.helper(piles[:-1], alice_score,
                                                                                     bob_score + piles[
                                                                                         len(piles) - 1])


if __name__ == '__main__':
    soln = Solution()
    print(soln.stoneGame([3,7,2,3]))
    # arr = [1, 2, 3]
    # print(arr[:-1])
