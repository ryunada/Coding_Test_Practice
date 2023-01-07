# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i]*numbers[j])
#     return max(answer)


def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2])

# numbers = [1, -3, 2, 4, -5]
numbers = [0, -31, 24, 10, 1, 9]

numbers = sorted(numbers)
print(numbers)
print(solution(numbers))