import random


def revise():
    print("hello" + "world")
    global tempo
    tempo = 10
    print(tempo)
    print(random.randrange(0, 10))

    s = "this is good to know"
    print(s.find("is"), s.index("is"), s.join("savio"), s.split(" "))

    my_list = [10, 20, 30, 40, 50]
    my_list.append(60)
    my_list.extend([70,80])
    print(my_list)

    new_list = my_list.copy()
    new_list = list(my_list)

    print([x for x in my_list if x > 20])

    my_list.sort(key=custom_sort)
    print(my_list)

    print(type(tempo))


def custom_sort(n):
    return abs(n - 20)


tempo = 5

if __name__ == '__main__':
    # print(float("inf") > int(10))
    #
    # arr1 = [1,2,3]
    # arr2 = [1,2]
    # for i in zip(arr1,arr2):
    #     print(i)
    # revise()
    # print(tempo)

    arr = [[1] * 4 for i in range(4)]
    print(arr)
    arr[0][1] = 2
    print(arr)

    print(ord("a"))

    # maps = dict(sorted(maps.items())) sort dict
