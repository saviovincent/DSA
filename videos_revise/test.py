import random


def check(input):
    last = -1
    start = 0
    maps = {}

    for i in input:
        maps[i['id']] = i

        seen = False

        for j in range(start + 1, i['id'] + 1):
            if j not in maps:
                seen = False
                break
            else:
                seen = True

        if seen:
            for j in range(start + 1, last + 1):
                print(maps[j])
            start = last
        if i['id'] > last:
            last = i['id']


def rev(strl):
    arr = []
    i = j = 0
    while i < len(strl):
        tmp = ""
        j = i
        while j < len(strl) and strl[j] != " ":
            tmp += strl[j]
            j += 1
        arr.append(str(tmp))
        i = j
        i+=1

    ans = ""
    while arr:
        word = arr.pop()
        ans += word + " "

    return ans


if __name__ == '__main__':
    # data = [
    #     {'id': 2, 'op': 'delete'},
    #     {'id': 1, 'op': 'delete'},
    #     {'id': 3, 'op': 'delete'},
    #     {'id': 5, 'op': 'delete'},
    #     {'id': 4, 'op': 'delete'}
    # ]
    # print(random.random()*50)
    # print("de" < "db")
    print(rev("i am a software engineer"))
    # check(data)
