class QuickSort:

    def partition(self, arr, l, h):
        pivot = arr[h]
        i = l  # look for > pivot
        j = h - 1  # look for < pivot

        while i < j:

            while arr[i] < pivot:
                i += 1

            while arr[j] > pivot:
                j -= 1

            if i < j:  # j should not exceed i for swapping
                arr[i], arr[j] = arr[j], arr[i]

        arr[i], arr[h] = arr[h], arr[i]  # swap with pivot element
        return i

    def quick_sort(self, arr, l, h):
        if l < h:
            pivot = self.partition(arr, l, h)
            self.quick_sort(arr, l, pivot - 1)
            self.quick_sort(arr, pivot + 1, h)


if __name__ == '__main__':
    sort = QuickSort()
    tmp = [2, 5, 1, 7, 4, 9]
    sort.quick_sort(tmp, 0, len(tmp) - 1)
    print(tmp)
