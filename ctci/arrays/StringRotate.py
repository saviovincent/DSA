def is_substr(str1, str2):
    return str2 in str1


def rotate(str1, str2):
    strr = str2 + str2
    return is_substr(strr, str1)


if __name__ == '__main__':
    print rotate("waterbottle", "erbottlewat")
