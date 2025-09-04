class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if n == 0:
            return True
        i = 0
        while n != 0 and i < len(flowerbed):
            if flowerbed[i] == 0:  # can place
                if i - 1 > 0 and i + 1 < len(flowerbed): # check boundaries
                    if flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                        flowerbed[i] = 1
                        n -= 1
                elif i == 0 and i + 1 < len(flowerbed) and flowerbed[i + 1] != 1:
                    flowerbed[i] = 1
                    n -= 1
                elif i == len(flowerbed) -1 and flowerbed[i -1] != 1:
                    flowerbed[i] = 1
                    n -= 1

            i += 1

        return n == 0


if __name__ == '__main__':
    soln = Solution()
    print(soln.canPlaceFlowers([0], 1))
