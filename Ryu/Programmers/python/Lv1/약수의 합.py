n = 5
l = list()
def solution(n):
    l = list()
    for i in range(1,n+1):
        if (n%i) == 0:
            l.append(i)
    return sum(l)

print(solution(n))