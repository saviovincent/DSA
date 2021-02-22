class Solution(object):
    output = list()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.power_set(nums, [])
        return self.output

    def power_set(self, ip, op):
        if not ip:
            self.output.append(op)
            return

        op1 = list(op)
        op2 = list(op)
        op2.append(ip[0])

        ip1 = list(ip)
        ip1.pop(0)

        self.power_set(ip1, op1)
        self.power_set(ip1, op2)


if __name__ == '__main__':
    soln = Solution()
    print(soln.subsets([0]))

