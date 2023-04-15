def solution(numbers, k):
    a = 2*(k-1)
    b = a%len(numbers)
    return numbers[b]

print(solution([1, 2, 3, 4],2))