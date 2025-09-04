import heapq

def heaptest():
    arr = [3, 1, 6, 9, 3, 4, 2]

    heapq.heapify(arr)
    heapq.heappush(arr, 10)

    while arr:
        print(heapq.heappop(arr))


class Heap:
    """
    min heap
    """

    def __init__(self):
        self.arr = []

    def add(self, no):
        self.arr.append(no)

        curr_idx = len(self.arr) - 1
        parent = (curr_idx - 1) // 2

        # trickle up
        while self.arr[parent] > self.arr[curr_idx]:
            self.arr[parent], self.arr[curr_idx] = self.arr[curr_idx], self.arr[parent]

    def heapify(self, idx):

        lc = idx * 2 + 1
        rc = idx * 2 + 2
        min_idx = idx

        # find min value btw root and both child
        if lc < len(self.arr) and self.arr[lc] < self.arr[idx]:
            min_idx = lc
        elif rc < len(self.arr) and self.arr[rc] < self.arr[idx]:
            min_idx = rc

        if min_idx != idx:
            self.arr[idx], self.arr[min_idx] = self.arr[min_idx], self.arr[idx]
            self.heapify(min_idx)

    def remove(self):

        # swap first and last element
        self.arr[0], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[0]

        # remove last el
        self.arr.pop()

        # call heapify()
        self.heapify(0)


def nth_largest(arr):
    pass


def sort_k_sorted(arr):
    pass


def closest_origin():
    pass


def frequency_sort():
    pass


def connect_ropes():
    pass


if __name__ == '__main__':
    heap = Heap()
    heap.add(2)
    heap.add(3)
    heap.add(1)

    heap.remove()

    print(heap.arr)
    # heaptest()
