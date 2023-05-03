def solution(order):
    answer = 0
    for i in range(len(str(order))):
        if str(order)[i] == '3' or str(order)[i] == '6' or str(order)[i] == '9':
            answer += 1
    return answer

print(solution(39487))
