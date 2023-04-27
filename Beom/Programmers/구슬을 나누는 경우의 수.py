def solution(balls, share):
    answer=1
    if balls==share:
        return 1
    else:
        for i in range(1,balls+1):
            answer *= i
        for j in range(1,share+1):
            answer /= j
        for k in range(1,balls-share+1):
            answer /= k
    return round(answer)

print(solution(7,4))