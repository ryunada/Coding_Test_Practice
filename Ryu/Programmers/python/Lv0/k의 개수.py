# def solution(i, j, k):
#     answer = 0
#     for a in range(i, j + 1):
#         a = str(a)
#         a = list(a)
#         b = a.count(str(k))
#         answer += b
#     return answer

def solution(i,j,k):
    return sum([ str(i).count(str(k)) for i in range(i,j+1)])

i = 1
j = 13
k = 1
result = 0
for a in range(i,j+1):
    a = str(a)
    a = list(a)
    b = a.count(k)
    result += b