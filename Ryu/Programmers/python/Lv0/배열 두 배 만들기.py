# def solution(numbers):
#     answer = []
#     for i in range(0,len(numbers)):
#         answer.append(numbers[i]*2)
#     return answer

# def solution(numbers):
#     for i in range(0,len(numbers)):
#         numbers[i] = numbers[i]*2
#     return numbers

def solution(numbers):
    return [num*2 for num in numbers]

numbers = [1,2,3,4,5]

print(solution(numbers))
