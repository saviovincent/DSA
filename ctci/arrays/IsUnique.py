def unique(strl):
    my_map = {}
    for i in strl:
        try:
            if my_map[i]:
                return False
        except Exception as e:
            my_map[i] = True
    return True


if __name__ == '__main__':
    print unique("savio")
