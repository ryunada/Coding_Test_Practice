# 가까운 수

array = [3,-1,1]

n = 0
a = []
for i in array:
    a.append(abs(i - n))

print(a)


num = a.index(min(a))

answer = 0
print(num)
answer = array[num]

print(answer)

#____________________________
# import numpy as np
# def solution(array, n):
#     diff = []
#     array = sorted(array)
#     for i in array :
#         diff.append(abs(n-i))
#     return array[np.argmin(diff)]