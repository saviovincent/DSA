# def solution(A):
#     # write your code in Python 3.6
#     my_map ={}
#     if len(A)%2 !=0:
#         return False
#     else:
#         for i in range(0, len(A)):
#             if A[i] in my_map:
#                 my_map[i] = my_map[i] +1
#             else:
#                 my_map[i] = 1
#
#         for i in my_map:
#             if my_map[i] %2 != 0:
#                 return False
#     return True

# def solution(S):
#     # write your code in Python 3.6
#     my_map = {}
#     count = 1
#
#     for i in range(0, len(S)):
#         # print(my_map)
#         if S[i] in my_map:
#
#             print(my_map)
#             my_map = {}
#             my_map[S[i]] = 1
#             count = count + 1
#         else:
#             my_map[S[i]] = 1
#             # print(my_map)
#     return count
#
# if __name__ == '__main__':
#     print(solution("dddd"))