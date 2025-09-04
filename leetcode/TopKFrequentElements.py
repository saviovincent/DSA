import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        my_map = {}
        my_heap = []
        heapq.heapify(my_heap)
        answer = []

        for i in nums:
            if i in my_map:
                my_map[i] += 1
            else:
                my_map[i] = 1

        for i in my_map:
            heapq.heappush(my_heap, my_map[i])
            if len(my_heap) > k:
                heapq.heappop(my_heap)

        for k, v in my_map.items():
            if v in my_heap:
                answer.append(k)

        return answer


if __name__ == '__main__':
    soln = Solution()
    print(soln.topKFrequent([1, 1, 1, 2, 2, 3], 2))
