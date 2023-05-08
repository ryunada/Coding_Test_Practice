def solution(n):
    for i in range(n+1):
        if i**2==n:
            return (i+1)**2
            break
    return -1

print(solution(121))
print(solution(3))