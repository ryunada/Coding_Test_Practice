# def solution(array):
#     answer = []
#     ma = max(array)
#     answer.append(ma)
#     for i in range(0,len(array)):
#         if ma == array[i]:
#             answer.append(i)
#     return answer

def solution(array):
    return [max(array), array.index(max(array))]

array = [1,8,3]
print(solution(array))