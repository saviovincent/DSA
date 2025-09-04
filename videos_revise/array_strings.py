from collections import Counter


#######---- cyclic sort for 1-n problems ----------####


def cycle_sort(arr):
    i = 0
    missing = []
    duplicates = []

    while i < len(arr):
        if arr[i] != i + 1 and arr[i] != arr[arr[
                                                 i] - 1]:  # second check validates if element sitting at arr[i] - 1 is correct or not. If its correct then dont swap
            # need to swap
            swap(i, arr[i] - 1, arr)
        else:
            i += 1

    for i in range(len(arr)):
        if arr[i] != i + 1:
            missing.append(i + 1)
            duplicates.append(arr[i])
    return missing, duplicates


def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]


############----- sliding window--------------###########

def max_sum_k(arr, k):
    i = j = max_sum = cur_sum = 0

    while j < len(arr):
        cur_sum = cur_sum + arr[j]

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            max_sum = max(max_sum, cur_sum)
            cur_sum -= arr[i]
            i += 1
            j += 1

    return max_sum


def first_negative_size_k(arr, k):
    i = j = 0
    que = []
    ans = []

    while j < len(arr):

        if arr[j] < 0:
            que.append(arr[j])

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:

            if que:
                ans.append(que[0])
            else:
                ans.append(0)

            if que and arr[i] == que[0]:
                que.pop(0)
            i += 1
            j += 1
    return ans


def max_in_window_size_k(arr, k):
    i = j = 0
    que = []
    ans = []

    while j < len(arr):

        if not que:
            que.append(arr[j])
        elif arr[j] > que[0]:
            que = [arr[j]]
        else:
            que.append(arr[j])

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            ans.append(que[0])
            if arr[i] == que[0]:
                que.pop(0)
            i += 1
            j += 1

    return ans


def find_all_anagrams(str, ptr):
    ans = []
    maps = Counter(ptr)

    i = j = 0
    count = len(maps.keys())

    while j < len(str):

        if str[j] in maps:

            if str[j] in maps and maps[str[j]] > 0:
                maps[str[j]] -= 1
            if str[j] in maps and maps[str[j]] == 0:
                count -= 1

        if j - i + 1 < len(ptr):
            j += 1

        elif j - i + 1 == len(ptr):
            if count == 0:
                ans.append(i)
            if str[i] in maps and maps[str[i]] > 0:
                maps[str[i]] += 1
            elif str[i] in maps and maps[str[i]] == 0:
                maps[str[i]] = 1
                count += 1
            i += 1
            j += 1

    return ans


def LargestSubarrayofsumK(self, arr, sum):  # only works with positive, for negative need Kadane.
    i = j = 0
    ws = 0
    curr_sum = 0

    while j < len(arr):
        curr_sum = curr_sum + arr[j]

        if curr_sum < sum:
            j = j + 1

        elif curr_sum == sum:  # when cond. matches 1 probable ans. to be found
            ws = max(ws, j - i + 1)

        elif curr_sum > sum:  # when > cond, need to shrink window size
            while curr_sum > sum:
                curr_sum = curr_sum - arr[i]
                i = i + 1
    return ws


def k_unique_substr(s, k):
    i = j = 0
    maps = {}
    ans = 0

    while j < len(s):

        if s[j] in maps:
            maps[s[j]] += 1
        else:
            maps[s[j]] = 1
        j += 1

        if k == len(maps.keys()):
            ans = max(ans, j - i + 1)

        elif len(maps.keys()) > k:
            while len(maps.keys()) > k:
                maps[s[i]] -= 1
                if maps[s[i]] == 0:
                    del maps[s[i]]
                i += 1

    return ans


def pick_toys(toys, k):
    i = j = 0
    maps = {}
    count = 0

    while j < len(toys):

        if toys[j] in maps:
            maps[toys[j]] += 1
        else:
            maps[toys[j]] = 1
        j += 1

        if len(maps.keys()) > k:
            maps[toys[i]] -= 1
            if maps[toys[i]] == 0:
                del maps[toys[i]]
            i += 1

        if len(maps) == k:
            count = max(count, sum(maps.values()))
    return count


def min_window_substr(s, t):
    maps = Counter(t)
    i = j = 0
    ans = float('inf')
    count = len(maps.keys())

    while j < len(s):

        if s[j] in maps:
            maps[s[j]] -= 1
            if maps[s[j]] == 0:
                count -= 1
        j += 1

        if count == 0:
            while count == 0:
                if s[i] in maps:

                    if maps[s[i]] < 0:
                        maps[s[i]] += 1

                    elif maps[s[i]] == 0:
                        maps[s[i]] += 1
                        count += 1
                i += 1
            ans = min(ans, j - i + 1)
    return ans


if __name__ == '__main__':
    # print(max_in_window())
    # print(k_unique_substr("aa", 2))
    # print(pick_toys("abaccab", 1))
    # print(min_window_substr("a", "aa"))
    # print(max_sum_k([2, 3, 1, 5, 1], 3))
    # print(cycle_sort([2, 3, 1, 5, 1]))
    print(find_all_anagrams("abab","ab"))
