lengt = 5


def check(arr, a):
    if a['i'] <= lengt / 2:
        a['i'] = a['i'] + 1
        check(arr, a)
    else:
        return

    a['i'] = a['i'] - 1
    if arr[a['j']] != arr[a['i']]:
        a['j'] = a['j'] + 1
        return False
    else:
        a['j'] = a['j'] + 1
        return True


if __name__ == '__main__':
    a = {'i': 0,
         'j': lengt / 2}
    print check([0, 1, 2, 1, 0], a)
