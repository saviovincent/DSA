class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        maps = {}
        ans = []
        partition_idx = part_size = 0

        for i in range(len(s)):
            maps[s[i]] = i

        for i in range(len(s)):
            part_size += 1
            partition_idx = max(partition_idx, maps[s[i]])

            if i == partition_idx:
                ans.append(part_size)
                part_size = 0
        return ans


if __name__ == '__main__':
    soln = Solution()
    print(soln.partitionLabels("a"))
    print(soln.partitionLabels("eccbbbbdec"))
