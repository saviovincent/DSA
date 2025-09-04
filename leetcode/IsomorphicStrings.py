class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        my_map = {}

        if len(s) != len(t):
            return False

        for i in zip(s, t):
            if i[0] in my_map:
                if i[1] != my_map[i[0]]:
                    return False
            else:
                if i[1] not in my_map.values():
                    my_map[i[0]] = i[1]
                else:
                    return False
        return True

if __name__ == '__main__':
    soln =Solution()
    print(soln.isIsomorphic("paper","title"))