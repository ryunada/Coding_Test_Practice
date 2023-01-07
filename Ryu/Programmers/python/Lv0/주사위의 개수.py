def solution(box, n):
    answer = 1
    for i in box:
        answer *= (i//n)
    return answer

box = [1,1,1]
n = 1

answer = 1
for i in box:
    answer *= (i//n)
print(1//1)
print(answer)