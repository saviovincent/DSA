# def maze(p, r, c, n, ans, vis):
#     if r == n - 1 and c == n - 1:
#         ans.append(p)
#         return
#
#     if str(r) + ":" + str(c) not in vis:
#         vis.add(str(r) + ":" + str(c))
#     else:
#         return
#     if r < n: maze(p + "D", r + 1, c, n, ans, set(vis))
#     if c < n: maze(p + "R", r, c + 1, n, ans, set(vis))
#     if r > 0: maze(p + "U", r - 1, c, n, ans, set(vis))
#     if c > 0: maze(p + "L", r, c - 1, n, ans, set(vis))
#
#     return len(ans)


if __name__ == '__main__':
    # print(maze("", 0, 0, 3, [], set()))

    print(ord("a"))

    from collections import deque

    d = deque()
    d.append(1)
    d.appendleft(2)

    print(d)

    d.popleft()
    print(d)



