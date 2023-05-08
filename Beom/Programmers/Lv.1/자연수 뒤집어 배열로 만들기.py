def solution(n):
    answer = []
    sn = str(n)
    for i in range(len(sn)):
        answer.append(int(sn[len(sn)-i-1]))
    return answer

print(solution(12345))
print(solution(43321))
