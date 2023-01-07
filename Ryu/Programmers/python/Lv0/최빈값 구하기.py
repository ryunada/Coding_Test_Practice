def solution(array):
    array.sort()
    answer = []
    result = []
    a = 0
    for i in array:
        if i not in answer:
            answer.append(i)
            result.append(array.count(i))
    print(answer)
    print(result)
    for j in range(0,len(result)):
        if result[j] == max(result):
            a += 1
    if a > 1:
        return -1
    for x in range(0, len(result)):
        if result[x] == max(result):
            return answer[x]

array = [1,4,3,3,3,2]

print(solution(array))

# def solution(array):
#     while len(array) != 0:
#         for i, a in enumerate(set(array)):
#             array.remove(a)
#         if i == 0:
#             return a
#     return -1

