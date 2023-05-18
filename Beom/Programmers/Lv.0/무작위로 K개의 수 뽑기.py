def solution(arr, k):
    answer=[]
    for i in arr:
        if i not in answer:
            answer.append(i)
        if len(answer) == k:
            break
    if len(answer)==k:
        return answer
    else:
        for i in range(k-len(answer)):
            answer.append(-1)
        return answer

print(solution([0, 1, 1, 2, 2, 3],3))