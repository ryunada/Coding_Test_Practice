# a병 → b병
# n병 → ?
a, b, n = 2, 1, 20
# a, b, n = 3, 1, 20

def solution(a, b, n):
    result = 0
    while(n >= a):
        result += (n // a) * b
        n = n - ((n // a) * a) + ((n // a) * b)
    return result

print(solution(a,b,n))
