def count_occurences(input):
    my_map = {}
    my_list = input.split("\n")

    most_used_word = ""
    count = 0

    space_list = my_list[0].split(" ")
    for i in space_list:
        try:
            if i in my_map:
                my_map[i] = my_map[i] + 1
            else:
                my_map[i] = 1
        except Exception as e:
            print(e)

    for i in my_map:
        if my_map[i] > count:
            most_used_word = i
            count = my_map[i]

    return most_used_word


def valid(input):
    print()


def check_row():
    print()


def check_col():
    print()


def check_diag():
    print()


if __name__ == '__main__':
    my_string = "one one one one one one " \
                "two two " \
                "three three three " \
                "four four four four " \
                "five five five five five"

    print(count_occurences(my_string))

    my_arr = [
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 1, 0]
    ]

    print(valid(my_arr))
