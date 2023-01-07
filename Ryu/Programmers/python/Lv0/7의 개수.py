# def solution(array):
#     answer = 0
#     for i in array:
#         for j in range(len(str(i))):
#             if str(i)[j] == '7':
#                 answer += 1
#     return answer

def solution(array):
    return sum([str(i).count('7') for i in array])

array = [7,77,17]
# array = [7,7,2,10,17,777]
print(solution(array))
# str(array[0])
answer = 0

