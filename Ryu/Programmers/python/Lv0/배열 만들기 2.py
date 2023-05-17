l = 5
r = 555

result = []
def solution(l, r):
    result = []
    five_zero = []
    for i in range(100):
        five_zero.append(5*int(bin(i)[2:])) # 이진수 1, 10, 11 ~ 5를 곱한값
        if (5*int(bin(i)[2:]) >= r):   # r전까지 5, 50, 55 ~ 만들기
            break
    for i in range(l,r+1):
        if i in five_zero:
            result.append(i)
    if len(result) == 0:
        result.append(-1)
    return result


# 신박한 방식 풀이 본것
# def solution(l, r):
#     answer = []
#     cnt=0
#     for i in range(l, r+1):
#         cnt=str(i).count('5')+str(i).count('0')
#         if len(str(i))==cnt:
#             answer.append(i)
#     if len(answer)==0:
#         answer.append(-1)
#     return answer
# print(solution(l,r))