class SelectSort:

    def sort(self, arr):

        for i in range(0, len(arr)):
            minm = 1000
            key = -1
            for j in range(i, len(arr)):
                if arr[j] < minm:
                    minm = arr[j]
                    key = j
            if minm != 1000 and key != -1:
                arr[i], arr[key] = arr[key], arr[i]

        return arr


if __name__ == '__main__':
    sort = SelectSort()
    print(sort.sort([6, 5, 4, 3, 2, 0, -1]))
