class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.ans = []
        self.idx = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """

        if not self.stack:
            self.stack.append((price, self.idx))
            self.idx += 1
            return 1
        else:
            prev_cost, index = self.stack[len(self.stack) - 1]

            if prev_cost > price:
                self.stack.append((price, self.idx))
                self.idx += 1
                return 1
            else:
                while self.stack:
                    prev_cost, index = self.stack[len(self.stack) - 1]
                    if prev_cost < price:
                        self.stack.pop()
                    else:
                        break

                if self.stack:
                    self.stack.append((price, self.idx))
                    self.idx += 1
                    return self.idx - index - 1
                else:
                    self.stack.append((price, self.idx))
                    self.idx += 1
                    return 1


if __name__ == '__main__':
    stock = StockSpanner()
    print(stock.next(31))
    print(stock.next(41))
    print(stock.next(60))
    print(stock.next(70))
    print(stock.next(60))
    print(stock.next(75))
    print(stock.next(85))

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
