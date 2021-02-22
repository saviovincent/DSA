class TwoWayMerge:
    def merge(self, arr1, arr2):
        i = 0
        j = 0
        k = 0
        n = len(arr1)
        m = len(arr2)
        result = []

        while i < n and j < m:
            if arr1[i] < arr2[j]:
                result.insert(k, arr1[i])
                i += 1
                k += 1
            else:
                result.insert(k, arr2[j])
                j += 1
                k += 1

        for a in range(i, n):
            result.insert(k, arr1[a])
            k += 1

        for a in range(j, m):
            result.insert(k, arr2[a])
            k += 1

        return result

    def merge_sort(self, ):

if __name__ == '__main__':
    test = TwoWayMerge()
    print(test.merge([2, 4, 6], [1, 3, 5]))
