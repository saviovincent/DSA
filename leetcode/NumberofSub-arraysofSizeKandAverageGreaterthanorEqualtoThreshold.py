class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """

        i = j = ans = cur_sum = 0

        while j < len(arr):
            cur_sum = cur_sum + arr[j]

            if j - i + 1 < k:
                j += 1

            elif j - i + 1 == k:
                if cur_sum / k >= threshold:
                    ans += 1
                cur_sum -= arr[i]
                i += 1
                j += 1

        return ans


if __name__ == '__main__':
    soln = Solution()
    print(soln.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))
