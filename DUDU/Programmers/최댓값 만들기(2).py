def solution(numbers):
    answer = 0
    numbers.sort(reverse=False)
    return max(numbers[0] * numbers[1],numbers[-1] * numbers[-2])
