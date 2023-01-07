# def solution(numbers, direction):
#     answer = []
#     if direction == "right":
#         for i in range(-1,len(numbers)-1):
#             answer.append(numbers[i])
#     else :
#         for i in range(1,len(numbers)):
#             answer.append(numbers[i])
#         answer.append(numbers[0])
#     return answer

def solution(numbers, direction):
    return [numbers[-1]] +numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]


direction = "right"
print(direction)
numbers = [1, 2, 3]
answer = []
if direction == 'right':
    for i in range(-1, len(numbers)-1):
        answer.append(numbers[i])
print(answer)

print(solution(numbers, direction))