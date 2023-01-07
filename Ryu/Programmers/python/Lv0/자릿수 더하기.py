# def solution(n):
#     answer = 0
#     for i in range(0,10):
#         answer += n % 10
#         if (n//10) == 0:
#             break
#         else:
#             n = n // 10
#     return answer

def solution(n):
    answer = 0
    while n:
        answer += n % 10
        n = n//10
    return answer
n = 1234
print(solution(n))
