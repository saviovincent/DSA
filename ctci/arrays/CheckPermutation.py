def perm_check(str1, str2):
    if len(str1) == len(str2):
        my_map = {}

        for i in str1:
            try:
                my_map[i] = my_map[i] + 1
            except Exception as e:
                my_map[i] = 1

        for i in str2:
            try:
                my_map[i] = my_map[i] - 1
                if my_map[i] < 0:
                    return False
            except Exception as e:
                return False
        return True
    return False


if __name__ == '__main__':
    print perm_check("savf", "hdfhdfh")
