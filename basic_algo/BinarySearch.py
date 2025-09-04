class BinarySearch:

    def iter_binary_search(self, arr, key):

        i = 0
        j = len(arr) - 1

        while i < j:

            mid = int((i + j) / 2)
            if arr[mid] is key:
                return mid
            elif arr[mid] < key:
                i = mid
            else:
                j = mid - 1

    def rec_binary_search(self, arr, key):

        mid = (len(arr) // 2) - 1
        if arr[mid] is key:
            return mid
        elif arr[mid] < key:
            return self.rec_binary_search(arr[mid:], key)
        else:
            return self.rec_binary_search(arr[:mid], key)


if __name__ == '__main__':
    test = BinarySearch()
    print(test.iter_binary_search([4, 6, 9, 12, 15, 18], 18))
    # print(test.rec_binary_search([4, 6, 9, 12, 15, 18], 18))
