# def solution(num_list, n):
#     answer = []
#     for i in range(len(num_list)//n):
#         answer.append(num_list[0:n])
#         del num_list[:n]
#     return answer

def solution(num_list, n):
    return [num_list[i-1:i] for i in range(n, len(num_list)+1, n)]

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
solution(num_list,n)