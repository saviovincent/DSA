class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = n
        seen = set()
        while tmp != 1:
            seen.add(tmp)
            tmp = self.square(tmp)
            if tmp in seen:
                return False

        return True

    def square(self, no):
        tmp = 0
        while no > 0:
            a = no % 10
            tmp += a * a
            no = no // 10
        return tmp

if __name__ == '__main__':
    soln = Solution()
    print(soln.isHappy(19))
