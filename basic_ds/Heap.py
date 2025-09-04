# max heap

"""
go to new implementation in videos_revise. This is too complicated...
"""
class Heap:

    def __init__(self):
        self.arr = []

    def add(self, el):

        if len(self.arr) == 0:
            self.arr.append(el)
            return

        self.arr.append(el)
        i = len(self.arr) - 1

        # trickle up
        while i >= 1:
            if self.arr[i // 2] < self.arr[i]:
                self.arr[i // 2], self.arr[i] = self.arr[i], self.arr[i // 2]  # swap with parent
            i = i // 2

    def remove(self):

        self.arr[0] = self.arr.pop()
        i = 0

        # trickle down
        while i < len(self.arr):
            child_max, index = self.get_max_child(i)
            if child_max is not None:
                if child_max > self.arr[i]:
                    self.arr[index], self.arr[i] = self.arr[i], self.arr[index]  # swap with max of both child
            else:
                return
            i = index

    def get_max_child(self, i):
        li = 2 * i + 1
        ri = 2 * i + 2
        lc = None
        rc = None
        if li < len(self.arr):
            lc = self.arr[2 * i + 1]
        if ri < len(self.arr):
            rc = self.arr[2 * i + 2]
        if lc is not None and rc is not None:
            if lc > rc:
                return lc, 2 * i + 1
            return rc, 2 * i + 2
        elif rc is not None and lc is None:
            return rc, 2 * i + 2
        elif lc is not None and rc is None:
            return lc, 2 * i + 1
        return None, -1


if __name__ == '__main__':
    hp = Heap()
    hp.add(2)
    hp.add(4)
    hp.add(3)
    hp.add(6)
    hp.add(8)

    print(hp.arr)
    hp.remove()
    print(hp.arr)
    hp.remove()
    print(hp.arr)
    hp.remove()
    print(hp.arr)
