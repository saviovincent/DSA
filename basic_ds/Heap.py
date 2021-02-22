# min heap

class Heap:

    def __init__(self):
        self.heap = []

    def get_parent(self, index):
        return (index - 1) / 2

    def get_children(self, index):
        return (index * 2) + 1, (index * 2) + 2

    def add(self, node):
        self.heap.append(node)
        self.trickleUp(len(self.heap) - 1)

    def trickleUp(self, pos):
        if pos is 0:
            return

        parent = self.get_parent(pos)

        if self.heap[parent] > self.heap[pos]:
            self.swap(parent, pos)
            self.trickleUp(parent)

    def printHeap(self):
        print("Heap Contents")
        print(self.heap)

    def swap(self, no1, no2):
        temp = self.heap[no1]
        self.heap[no1] = self.heap[no2]
        self.heap[no2] = temp

    def remove(self):

        if self.heap:
            self.heap[0] = self.heap[len(self.heap) - 1]
            self.heap.pop(len(self.heap) - 1)

            self.trickleDown(0)

    def trickleDown(self, pos):

        if (2*pos)+1 >= len(self.heap):
            return

        left, right = self.get_children(pos)

        #handle 1 child case here

        if right >= len(self.heap):
            smallest = left
        elif self.heap[left] < self.heap[right]:
            smallest = left
        else:
            smallest = right

        if self.heap[pos] > self.heap[left] or self.heap[pos] > self.heap[right]:
            self.swap(pos, smallest)
            self.trickleDown(smallest)


if __name__ == '__main__':
    heap = Heap()
    heap.add(50)
    heap.add(110)
    heap.add(20)
    heap.add(5)
    heap.add(200)
    heap.add(50)
    heap.add(3)

    heap.remove()
    heap.remove()

    heap.printHeap()
