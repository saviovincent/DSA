class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        my_set = set()

        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue
            for j in range(0, 3):
                if i[j] == target[j]:
                    my_set.add((j,target[j]))
        return len(my_set) == 3


if __name__ == '__main__':
    soln = Solution()
    print(soln.mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]))
