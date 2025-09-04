class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        arr = s.strip().split()

        i = 0
        j = len(arr) -1

        while i <j:
            arr[i],arr[j] = arr[j].strip(),arr[i].strip()
            j-=1
            i+=1
        return " ".join(arr)

if __name__ == '__main__':
    soln = Solution()
    print(soln.reverseWords("a good   example"))
