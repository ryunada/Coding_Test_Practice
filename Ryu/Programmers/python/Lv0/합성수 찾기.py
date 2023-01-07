# def solution(n):
#     result = 0
#     for i in range(1, n + 1):
#         answer = 0
#         for j in range(1, i + 1):
#             if (i % j) == 0:
#                 answer += 1
#         if answer >= 3:
#             result += 1
#     return result

n = 10
result = 0
for i in range(1,n+1):
    answer = 0
    for j in range(1,i+1):
        if (i % j) == 0:
            answer += 1
    if answer >= 3:
        result += 1


print(result)