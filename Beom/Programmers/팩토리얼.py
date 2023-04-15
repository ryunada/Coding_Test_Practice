def solution(n):
    for i in range(1, 11):
        n = n // i
        if n < i + 1:
            return i
            break

print(solution(121))