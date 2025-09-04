# ------------- Shraddha ---------------
def push_bottom_stack():
    stack = [1, 2, 3, 4]

    def push(stack, el):
        if not stack:
            stack.append(el)
            return
        popped = stack.pop()
        push(stack, el)
        stack.append(popped)

    push(stack, 5)
    print(stack)


def design_circular_queue():
    size = 5
    queue = [None] * size
    start = -1
    end = -1

    def enqueue(data):
        nonlocal start
        nonlocal end

        if start == -1 and end == -1:
            start = end = 0
            queue[start] = data
        elif (end + 1) % size == start:
            print("queue full")
        else:
            end += 1
            queue[end % size] = data

    def dequeue():
        nonlocal start
        nonlocal end

        if start == end:
            queue[start % size] = None
            print("queue empty")
            start = end = -1
        elif start == -1 and end == -1:
            print("queue empty")
        else:
            queue[start % size] = None
            start += 1

    enqueue(1)
    enqueue(2)
    enqueue(3)
    enqueue(4)
    enqueue(5)
    print(queue)
    enqueue(6)
    dequeue()
    print(queue)
    dequeue()
    print(queue)
    dequeue()
    print(queue)
    dequeue()
    print(queue)
    dequeue()
    print(queue)
    dequeue()
    print(queue)


def queue_using_stack():
    s1 = []
    s2 = []

    def push(data):
        nonlocal s1
        s1.append(data)

    def pop():
        nonlocal s1
        nonlocal s2

        if not s1:
            print("queue empty")
            return
        while len(s1) > 1:
            s2.append(s1.pop())
        print(s1.pop())

        while s2:
            s1.append(s2.pop())

    push(1)
    push(2)
    push(3)
    pop()
    pop()
    pop()
    pop()


def stack_using_queue():
    " same logic queue_using_stack use 2 queue "
    pass


# -------------- AV -----------------
def reverse_stack():
    pass


def largest_rectangle():
    pass


def next_largest_el_right(arr):
    """
    foundation problem for stack -> Traverse from right end of array and push to stack.
    Check for 3 conditions:
    """
    stack = []
    ans = []

    for i in range(len(arr) - 1, -1, -1):

        if not stack:  # last el when pushed stack will be empty
            stack.append(arr[i])
            ans.append(-1)

        elif stack:

            if stack[len(stack) - 1] > arr[i]:  # top of stack is > current el
                ans.append(stack[len(stack) - 1])
                stack.append(arr[i])

            else:  # top of stack < current el
                while stack and stack[len(stack) - 1] < arr[i]:
                    stack.pop()

                if stack:  # check which cond. terminated above loop
                    ans.append(stack[len(stack) - 1])
                else:
                    ans.append(-1)
                stack.append(arr[i])

    ans.reverse()
    return ans


def stock_span(arr):
    stack = []
    ans = []

    for i in range(0, len(arr)):

        if not stack:
            ans.append(1)
            stack.append((arr[i], i))

        elif stack:

            price, index = stack[len(stack) - 1]

            if price > arr[i]:
                ans.append(1)
                stack.append((arr[i], i))

            else:

                while stack:
                    price, index = stack[len(stack) - 1]
                    if price < arr[i]:
                        stack.pop(len(stack) - 1)
                    else:
                        break
                if stack:
                    ans.append(i - index)
                else:
                    ans.append(1)
    return ans


class Minstack:

    def __init__(self):
        self.stack = []
        self.min_el = float('inf')

    def push(self, el):
        if not self.stack:
            self.stack.append(el)
            self.min_el = el
        else:
            if el >= self.min_el:
                self.stack.append(el)
            else:
                self.stack.append(2 * el - self.min_el)
                self.min_el = el

    def pop(self):
        if not self.stack:
            return -1
        else:
            if self.min_el < self.stack[len(self.stack) - 1]:
                self.stack.pop()
            else:
                self.min_el = 2 * self.min_el - self.stack[len(self.stack) - 1]
                self.stack.pop()

    def get_min(self):
        if not self.stack:
            print(-1)
        else:
            print(self.min_el)


if __name__ == '__main__':
    print(push_bottom_stack())
    # print(design_circular_queue())
    # print(queue_using_stack())

    # print(next_largest_el([3, 1, 2, 4]))  # 4 2 4 -1
    # print(stock_span([100, 70, 80, 60]))  # 1 1 2 1
    # min_stack = Minstack()
    # min_stack.push(3)
    # min_stack.get_min()
    # min_stack.push(1)
    # min_stack.get_min()
    # min_stack.push(0)
    # min_stack.get_min()
    # min_stack.pop()
    # min_stack.get_min()
    # min_stack.pop()
    # min_stack.get_min()

    # print(stack_using_queue())
    # print(queue_using_stack())
    # print(largest_rectangle())
