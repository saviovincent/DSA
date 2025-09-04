class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        if n == 1:
            return 0
        no_list = {
            0: 0
        }

        for i in range(1, n + 1):
            no_list[i] = (self.generate(no_list[i - 1]))

        no = no_list[n][k-1]
        return int(no)

    def generate(self, no):
        rslt = ""
        for i in str(no):
            if i == '0':
                rslt += "01"
            if i == '1':
                rslt += "10"
        if rslt:
            return rslt
        return 0


if __name__ == '__main__':
    soln = Solution()
    print(int(not 101))
    # print(soln.kthGrammar(30,434991989))

