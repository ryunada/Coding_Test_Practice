# def solution(num_list):
#     answer = []
#     for i in range(len(num_list)-1,-1,-1):
#         answer.append(num_list[i])
#     return answer

def solution(numlist):
    return num_list[::-1]

num_list = [1,2,3,4,5]

print(solution(num_list))

