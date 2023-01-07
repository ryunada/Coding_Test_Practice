def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    return answer/len(numbers)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(solution(numbers))
