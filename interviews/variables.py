def check():
    global name
    name = "savio"

    global age
    age = 20


def check(no):
    reverse = 0
    num = no
    while no > 0:
        digit = no % 10
        reverse = reverse * 10 + digit
        no = no // 10
    if num == reverse:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check(101))
    print(check(-1011))

