# def solution(balls, share):
#     answer = 1
#     a = 0
#     for i in range(share + 1, balls + 1):
#         a += 1
#         answer *= i
#         answer /= a
#     return answer

import math
def solution(balls, share):
    return math.comb(balls,share)



balls = 5
share = 3
answer = 1
a = 0
for i in range(share+1,balls+1):
    a += 1
    answer *= i
    answer /= a
    print(i)
    print(a)

print(answer)
# print(answer/a)
print(6/2)