## ----- Kunal --------- ####
def bs(arr, target, s, e):
    if s > e:
        return -1
    mid = (s + e) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        bs(arr, target, mid + 1, e)
    else:
        bs(arr, target, s, mid - 1)


def check_sorted(arr, i):
    if i == len(arr) - 1:
        return True
    if arr[i] > arr[i + 1]:
        return False
    return check_sorted(arr, i + 1)


def search(arr, el, i):
    if i == len(arr):
        return False
    return arr[i] == el or search(arr, el, i + 1)


def reverse_no(no, digits):
    if no == 0:
        return no
    rem = no % 10
    return rem * pow(10, digits) + reverse_no(no // 10, digits - 1)


def reduce(no, steps):
    if no == 0:
        return steps
    if no & 1:
        return reduce(no // 2, steps + 1)
    return reduce(no - 1, steps + 1)


def star():
    for i in range(5, -1, -1):
        for j in range(0, i):
            print("*", end="")
        print()

    for i in range(0, 6):
        for j in range(0, i):
            print("*", end="")
        print()


def star_recursion(row, col):
    if row == 0:
        return
    if col == row:
        print()
        star_recursion(row - 1, 0)
    else:
        print("*", end="")
        star_recursion(row, col + 1)


def star1(row, col):
    if row == 0:
        return
    if col == row:
        star_recursion(row - 1, 0)
        print()

    else:
        star_recursion(row, col + 1)
        print("*", end="")


def remove_a_args(strl, ans, index):
    if index == len(strl):
        return ans
    if strl[index] == 'a':
        return remove_a_args(strl, ans, index + 1)
    return remove_a_args(strl, ans + strl[index], index + 1)


def remove_a_body(strl, index):
    if index == len(strl):
        return ""
    if strl[index] == 'a':
        return remove_a_body(strl, index + 1)
    else:
        return strl[index] + remove_a_body(strl, index + 1)


# -------- MOST IMPORTANT ----------------
def subset(strl, ans, index, my_list):
    if index == len(strl):
        my_list.append(ans)
        return
    subset(strl, ans + strl[index], index + 1, my_list)
    subset(strl, ans, index + 1, my_list)
    return my_list


# simple version of subset pattern
def subs(p, up):
    if not up:
        print(p)
        return
    subs(p, up[1:])
    subs(p + up[0], up[1:])

# example of VARIABLE NO of recursive calls
# In processed/unprocessed method ans is always going be in processed when unprocessed becomes empty
def perm(p, up):
    if not up:
        print(p)
        return
    for i in range(0, len(p) + 1):
        pre = p[:i]
        post = p[i:]
        perm(pre + up[0] + post, up[1:])


maps = {
    '1': "abc",
    '2': "def"
}


def keypad(p, up):
    if not up:
        print(p)
        return
    for i in range(0, len(maps[up[0]])):
        keypad(p + maps[up[0]][i], up[1:])


def comb_sum(p, target):
    if target < 0:
        return
    if target == 0:
        print(p)
        return
    for i in range(1, 7):
        comb_sum(p + str(i), target - i)


def count_subset(p, up, ans, i, my_set):
    count = 0
    if not up:
        if ''.join(sorted(p)) not in my_set:
            my_set.add(p)
            ans.append(p)
            count = 1
        return count
    count += subset(p + up[0], up[1:], ans, i + 1, my_set)
    count += subset(p, up[1:], ans, i + 1, my_set)
    return count


# extension of subset pattern with 2 vars - row, col
# when r,c == n-1, n-1 then similar to up ans in p
def maze_count_no_paths(r, c, n):
    if r == n - 1 or c == n - 1:
        return 1
    count = 0
    count += maze_count_no_paths(r + 1, c, n)
    count += maze_count_no_paths(r, c + 1, n)
    return count


def maze_down_right_all_paths(p, r, c, n, ans):
    if r == n - 1 and c == n - 1:
        ans.append(p)
        return

    if r < n: maze_down_right_all_paths(p + "D", r + 1, c, n, ans)
    if c < n: maze_down_right_all_paths(p + "R", r, c + 1, n, ans)
    return ans


# without backtracking 4 paths is infinite loop. mark visited for each cell in that recursion call
# once that fn is about to get over, revert changes made for that rec call. ie visited = false for that cell. This is BT
def maze_4dirs(p, r, c, n, ans, vis):  # error
    if r == n - 1 and c == n - 1:
        ans.append(p)
        return

    if str(r) + ":" + str(c) not in vis:
        vis.add(str(r) + ":" + str(c))
    else:
        return
    if r < n: maze_4dirs(p + "D", r + 1, c, n, ans, vis)
    if c < n: maze_4dirs(p + "R", r, c + 1, n, ans, vis)
    if r > 0: maze_4dirs(p + "U", r - 1, c, n, ans, vis)
    if c > 0: maze_4dirs(p + "L", r, c - 1, n, ans, vis)

    vis.remove(str(r) + ":" + str(c))
    return len(ans)


## ------- Shraddha -------- #########
def powx(x, n):
    if n == 0:
        return 1
    a = powx(x, n // 2)
    if n % 2 == 0:
        return a * a
    else:
        return a * a * x


def hanoi(n, src, helper, dest):
    if n == 1:
        print("transfer {} from {} to {}".format(n, src, dest))
        return
    hanoi(n - 1, src, dest, helper)
    print("transfer {} from {} to {}".format(n, src, dest))
    hanoi(n - 1, helper, src, dest)


def rev(strl):
    if not strl:
        return ""
    return rev(strl[1:]) + strl[0]


def find(strl, first, last, index):
    if index > len(strl) - 1:
        return first, last
    if strl[index] == 'a':
        if first == -1:
            first = index
        else:
            last = index
    return find(strl, first, last, index + 1)


def check_Sort(arr, idx):
    if idx == len(arr) - 1:
        return True
    return arr[idx] < arr[idx + 1] and check_Sort(arr, idx + 1)


def subseq(strl, idx, ans):
    if idx == len(strl):
        print(ans)
        return
    subseq(strl, idx + 1, ans + strl[idx])
    subseq(strl, idx + 1, ans)


def maze(n, m):
    if n == 1 or m == 1:
        return 1
    return maze(n - 1, m) + maze(n, m - 1)


def palce_tile(n, m):
    if n == m:
        return 2
    if n < m:
        return 1
    return palce_tile(n - m, m) + palce_tile(n - 1, m)


def party_ppl(n):
    if n == 1 or n == 0:
        return 1
    return party_ppl(n - 1) + (n - 1) * party_ppl(n - 2)


def reverse_str(strl):
    rslt = ""
    tmp = strl.split(" ")
    for i in range(len(tmp) - 1, -1, -1):
        rslt += rev(tmp[i]) + " "
    return rslt


def dec_bin(no):
    if no == 0:
        return ""
    return dec_bin(no // 2) + str(no % 2)


def palin(strl, s, e):
    if s > e:
        return True
    return strl[s] == strl[e] and palin(strl, s + 1, e - 1)


if __name__ == '__main__':
    # print(party_ppl(3))
    # print(palce_tile(4, 2))
    # print(maze(3, 3))
    # print(check_Sort([1,5,3,4],0))
    # print(subseq("abc", 0, ""))
    # print(find("abaaca", -1, -1, 0))
    # print(rev("savio"))
    # print(hanoi(3, "source", "helper", "destination"))
    # print(powx(3, 5))

    comb_sum("", 5)
    # combo("", '12')
    # perm("", "abc")
    # print(subset("abc", "", 0, []))
    # print(remove_a_body("savio", 0))
    # print(check_sorted([1, 4, 3], 0))
    # print(search([1, 2, 3], 4, 0))
    # print(reduce(14, 0))
    # star1(5, 0)
    # star_recursion(5, 0)
    # print(subset("", ''.join(sorted("aabc")), [], 0, set()))

    # print(dec_bin(2))
    # print(palin("kka",0,2))
    # print(reverse_str("the simple engineer"))
    #  print(reverse("Savio"))
    # print(maze_down_right_all_paths("", 0, 0, 4, []))
    # print(maze_4dirs("", 0, 0, 3, [], set()))
    # print(subs([],[1,2,3]))
