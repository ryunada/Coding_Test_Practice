# ctrl+z(stack으로 풀어야 함)

# def solution(s):
#     answer = 0
#     s = s.split(' ')
#     ctrl_z = []
#     for i in s:
#         ctrl_z.append(i)
#         if (ctrl_z[-1] == 'Z'):
#             if i == 0:      # 첫번째 Z인 경우
#                 ctrl_z = 0
#             else:
#                 del ctrl_z[-2:]
#     for j in ctrl_z:
#         answer += int(j)
#     return answer

def solution(s):
    s = s.split(' ')
    result = []
    for i in s:
        if i == 'Z':
            result.pop()
        else:
            result.append(int(i))
    return sum(result)


# s = "1 2 Z 3"
# s = "10 20 30 40"
# s = "Z 1 2 3"
# s = "Z Z 1 2"
# s = "1 2 3 Z Z"
# s = "1"
# s = "0 0 0 0 Z"
# s = "-1 -2 -3"
# s = "-1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1"
s = "-100 10 Z 11 12 Z Z"

print(solution(s))
answer = 0

# print(s.split(' '))
