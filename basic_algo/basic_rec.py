def check(no):
    if no == 0:
        return 0

    return (check(no // 10) * 10) + no % 10


def reverse(strl, s, e):
    if s == e:
        return strl
    strl[s], strl[e] = strl[e], strl[s]
    return reverse(strl, s + 1, e - 1)

def pal(strl, s, e):
    if s == e:
        return True
    if strl[s] != strl[e]:
        return False
    return pal(strl, s + 1, e - 1)

def bin(no, strl):
    if no ==0:
        return strl
    strl = strl + no%2
    return bin(no/2, strl)

# def fir_las(strl, key,idx, first = -1, last = -1):
#     if len(strl) == 0:
#         return
#     if key == strl[idx] and first == -1:
#         first = idx
#
#     fir_las(strl[idx:], key, idx+1, first, last)
#
#     if key == strl[idx] and last == -1:
#         first = idx



if __name__ == '__main__':
    # print(check(1234))
    tmp = ['s', 'a', 'v']
    # print(reverse(tmp, 0, len(tmp) - 1))
    # print(pal("kayaki",0,5))
    # print(bin(6,""))
    # print(fir_las("saviao", 'a'))

