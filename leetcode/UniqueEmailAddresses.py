class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        my_map = {}
        for i in emails:
            tmp = i.split("@")
            local = tmp[0]
            domain =tmp[1]
            tmp1 = local.replace("+",".")
            tmp2 = tmp1.split(".")

            local_updated = "".join(tmp2)

            if local_updated in my_map:

if __name__ == '__main__':
    soln = Solution()
    print(soln.numUniqueEmails(["ab@leetcode.com","a.b@leetcode.com","a+b@leetcode.com"]))