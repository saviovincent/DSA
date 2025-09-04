import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # heapq.heapify(nums)
        # while len(nums) > k:
        #     heapq.heappop(nums)
        # return heapq.heappop(nums)

        return self.quick_select(nums, 0, len(nums) - 1, k - 1)

    def quick_select(self, arr, start, end, k):
        if start <= end:
            pivot = self.partition(arr, start, end)
            if pivot < k:
                return self.quick_select(arr, pivot + 1, end, k)
            elif pivot > k:
                return self.quick_select(arr, start, pivot - 1, k)
            return arr[pivot]

    def partition(self, arr, start, last):

        pivot = arr[last]  # make last element as pivot

        i = start  # keeps track of item < pivot
        j = last - 1  # keeps track of item > pivot

        while i <= j:
            while i <= j and arr[i] <= pivot:
                i += 1  # increment i till el < pivot
            while i <= j and arr[j] > pivot:
                j -= 1  # decrement j till el > pivot

            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]  # swap when contradicting el found
                i += 1
                j -= 1

        arr[i], arr[last] = arr[last], arr[i]  # move pivot to correct index i
        return i


if __name__ == '__main__':
    soln = Solution()
    print(soln.findKthLargest([3, 2, 3, 1, 2, 4, 2, 2, 5, 6], 4))
