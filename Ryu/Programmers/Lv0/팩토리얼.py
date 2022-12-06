# def solution(n):
#     result = 1
#     for i in range(1, 10):
#         result *= i
#         if result > n:
#             break
#     return i

from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k

result = 1
n = 7
for i in range(1,10):
    result *= i
    if result > n:
        break
print(i-1)