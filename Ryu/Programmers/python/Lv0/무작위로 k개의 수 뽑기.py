arr = [0, 1, 1, 2, 2, 3]
k = 3
result = []

arr.sort()
for i in arr:
    if i not in result: # 새로운 것만 result에 추가
        result.append(i)
if len(result) < k:
    for i in range(k-len(result)):
        result.append(-1)
print(result[:k])

def solution(arr, k):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    while(len(result) < k):
        result.append(-1)
    return result[:k]