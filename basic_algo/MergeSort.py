class MergeSort:

    def merge(self, arr, low, mid, high):

        tmp1 = arr[:mid]
        tmp2 = arr[mid:]

        i = j = k = 0

        while i < len(tmp1) and j < len(tmp2):
            if tmp1[i] < tmp2[j]:
                arr[k] = tmp1[i]
            else:
                arr[k] = tmp2[j]
            j += 1
            k += 1

        while i < len(tmp1):
            arr[k] = tmp1[i]
            i += 1
            k += 1
        while j < len(tmp2):
            arr[k] = tmp2[j]
            j += 1
            k += 1
        return arr

    def merge_sort(self, arr, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(arr, low, mid)
            self.merge_sort(arr, mid + 1, high)
            return self.merge(arr, low, mid, high)


if __name__ == '__main__':
    sort = MergeSort()
    arr = [4, 1, 2, 3]
    print(sort.merge_sort(arr, 0, len(arr) - 1))
    # print(sort.merge([2,3,0,1], 0, 2, 4))
