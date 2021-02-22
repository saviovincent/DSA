class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append(str("FizzBuzz"))
            elif i % 3 == 0:
                result.append(str("Fizz"))
            elif i % 5 == 0:
                result.append(str("Buzz"))

            else:
                result.append(str(i))
        return result


if __name__ == '__main__':
    soln = Solution()
    print(soln.fizzBuzz(15))
