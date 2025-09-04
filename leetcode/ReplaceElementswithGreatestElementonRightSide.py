class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        if arr:
            rslt = [-1]
            current_max = -1
            for i in range(len(arr)-1, 0,-1):
                if arr[i] > current_max:
                    rslt.append(arr[i])
                    current_max = arr[i]
                else:
                    rslt.append(current_max)

            rslt.reverse()
            return rslt
        else:
            return []


if __name__ == '__main__':
    soln = Solution()
    print(soln.replaceElements([-99,-98]))