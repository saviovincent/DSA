import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heapdata = nums
        heapq.heapify(self.heapdata)
        self.size = k

        while len(self.heapdata) > self.size:
            heapq.heappop(self.heapdata)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heapdata, val)
        while len(self.heapdata) > self.size:
            heapq.heappop(self.heapdata)
        return self.heapdata[0]


if __name__ == '__main__':
    soln = KthLargest(3, [2, 1, 4, 6])
    print(soln.add(3))
    print(soln.add(4))
    print(soln.add(5))
    print(soln.add(6))

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
