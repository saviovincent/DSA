class GreedyKnapsack:

    def run(self):

        weight_arr = [2, 3, 5, 7, 1, 4, 1]
        profit_arr = [10, 5, 15, 7, 6, 18, 3]

        max_weight = 15
        profit_weight_arr = []
        object_included_arr = []

        for i in range(0, len(weight_arr)):
            profit_weight_arr.append(profit_arr[i] / weight_arr[i])

        print(profit_weight_arr)

        current_weight = 0
        profit_weight_arr.sort()

        for i in weight_arr:
            if current_weight + i > max_weight:
                print("Need to add fractional")
            else:
                print("Include entire object")
                current_weight = current_weight + current_weight[i]


if __name__ == '__main__':
    knapsack = GreedyKnapsack()
    knapsack.run()
