class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        if not s:
            return

        # iterative process
        # i = 0
        # j = len(s) - 1
        # while i < j:
        #     s[i], s[j] = s[j], s[i]
        #     i = i + 1
        #     j = j - 1

        self.recur(s, 0, len(s) - 1)
        return s

    # def reverse_recur(self, arr):
    #     return self.helper(0, len(arr) - 1, arr)
    #
    # def helper(self, start, end, arr):
    #     if start >= end:
    #         return
    #     arr[start], arr[end] = arr[end], arr[start]
    #
    #     return self.helper(start + 1, end - 1)

    def recur(self, s, start, end):
        if start > end:
            return
        s[start], s[end] = s[end], s[start]
        self.recur(s, start + 1, end - 1)

    # basic recurse and print in reverse
    def reverse(self, strl, index):
        if len(strl) == index + 1:
            print(strl[index])
            return
        self.reverse(strl, index + 1)
        print(strl[index])


if __name__ == '__main__':
    soln = Solution()
    print(soln.reverseString(["s", "a", "v"]))
    # soln.reverse("savio", 0)
