# 가까운 수

array = [3,1,-1]
array = sorted(array)
n = 0
a = []
for i in array:
    a.append(abs(i - n))
num = a.index(min(a))
answer = 0
answer = array[num]

print(answer)

##
# def solution(array, n):
#     answer = 0
#     a = []
#     array = sorted(array)
#     for i in array:
#         a.append(abs(i - n))
#     num = a.index(min(a))
#     answer = array[num]
#
#     return answer

# solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]