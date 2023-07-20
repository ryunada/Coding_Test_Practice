# ex1)
# k, m = 3, 4
# score = [1, 2, 3, 1, 2, 3, 1]

# ex2)
k, m = 4, 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]


# 왜 시간초과 일까
# def solution(k, m, score):
#     result = 0
#     score.sort() # score 오름차순 정렬
#     while(len(score) >= m):
#         box = score[-m:]
#         result += min(box) * m
#         score = score[:-m]
#     return result
# print(solution(k, m, score))

def solution(k, m, score):
    result = 0
    score.sort(reverse = True)           # score 내림차순 정렬
    for i in range(0, len(score), m):    # 상자의 가격에 곱해지는 k의 인덱스
        if (i + m) <= len(score):
            result += score[i + m  - 1]
    result = result * m
    return result

print(solution(k, m, score))



