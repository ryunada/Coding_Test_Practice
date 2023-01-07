# def solution(num, k):
#     num = list(str(num))
#     k = list(str(k))
#     for j in k:
#         for i in range(len(num)):
#             if num[i] == str(j):
#                 answer = i+1
#                 break
#             else:
#                 answer = -1
#     return answer

def solution(num, k):
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1



num = 29183
num = list(str(num))
print(num)
k = 1
for i in range(len(num)):
    if num[i] == str(k):
        print(i )
