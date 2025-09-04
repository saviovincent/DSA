# you can write to stdout for debugging purposes, e.g.
# start app -> idle state -> running state -> shut down
print("This is a debug message")


class app():
    def __init__(self):
        self.current_state = "init done"

    def start(self):
        self.current_state = "start"
        print("app start")

    def idle(self):
        self.current_state = "idle"
        print("app idle")

    def run(self):
        self.current_state = "run"
        print("app run")

    def stop(self):
        self.current_state = "stop"
        print("app stop")

    def get_state(self):
        return self.current_state


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


# TODO implement
class LRU:

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove app from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # add app to right side of list
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    # {
    # "app1":("app1":"start time")
    # }
    def add(self, key, value):  # key:app name  value: time
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove my app from list and delete from map
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# init cache
lru = LRU(3)

app1 = app()
app1.start()
lru.add(app1)

app2 = app()
app2.start()
lru.add(app2)

app3 = app()
app3.start()
lru.add(app3)

#################

app4 = app()
app1.stop()

app4.start()
lru.add(app4)

# expected app 1 to stop and then start app 4


# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")


# [circle, rectangle, rectangle]

class Calculator():

    def __init__(self, arr):
        self.arr = arr

    def calc_area(self):
        summ = 0
        for i in self.arr:

            if i[0] == "circle":
                summ += Circle(i[1]).area()

            elif i[0] == "rectangle":
                summ += Rectangle(i[1], i[2]).area()

            elif i[0] == "square":
                summ += Square(i[1]).area()

        return summ


class Circle():
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


class Square():
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle():
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


cal = Calculator([("circle", 3), ("rectangle", 2, 3), ("rectangle", 2, 3)])
print(cal.calc_area())

self.msg['committed']





