# extra space
def urlify(str1, length):
    var = ""
    k = 0
    for i in str1:
        if k < length:
            if i == " ":
                var = var + "%20"
                k = k + 1
            else:
                var = var + i
                k = k + 1

    return var


if __name__ == '__main__':
    print urlify("my name is   ", 10)
