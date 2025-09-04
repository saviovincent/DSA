# // # # You are given a list of equations:
# // # # A / B = 5
# // # # B / C = 10
#
# // # # Deduce the following:
# // # # A / C = ?
# // # # B / A = ?
# // # # A / A = ?
# // # # A / X = ?
#
# // # # Constraints: All values are positive. If you cannot deduce a solution, the answer is -1.
#
# // # # Sample Input:
#
# // # # equations = [['A', 'B'], ['B', 'C']]
# // # # results = [5, 10]
# // # # queries = [['A', 'C'], ['B', 'A'], ['A', 'A'], ['A', 'X']]
#
# a- [5B,]
# b - a/5,
# // # # Sample Output: [50, 0.2, 1, -1]

relation_map = {}


def calculate(equations, results):
    for i in range(len(equations)):
        first_char = equations[i][0]
        second_char = equations[i][1]
        value = results[i]

        if first_char in relation_map:
            relation_map[first_char] = relation_map[first_char].append(str(value) + second_char)
        else:
            relation_map[first_char] = [str(value) + second_char]

        if second_char in relation_map:
            relation_map[second_char] = relation_map[second_char].append(str(1 / value) + first_char)
        else:
            relation_map[second_char] = [str(1 / value) + first_char]


if __name__ == '__main__':
    calculate()
