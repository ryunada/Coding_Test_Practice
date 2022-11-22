def solution(order):
    answer = 0
    if (order %10) ==  0:
        return 0
    order = list(str(order))
    for i in order:
        if (int(i) % 3) == 0:
            answer += 1
    return answer

order = 10
print(solution(order))

