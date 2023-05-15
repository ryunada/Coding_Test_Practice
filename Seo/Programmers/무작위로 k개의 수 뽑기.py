def solution(arr, k):
    answer = [arr[0]]
    for i in arr:
        if i in answer:
            continue
        else:
            if len(answer) < k:
                answer.append(i)
    while len(answer) < k:
        answer.append(-1)
    return answer

print(solution([9, 9, 2, 1, 1],2))