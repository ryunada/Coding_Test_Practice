def solution(arr, k):
    answer = [arr[0]]
    for i in arr:
        if i in answer:            # 나온 적이 있는 수: pass
            continue
        else:                      # 나온 적이 없는 수: 길이 k될 때 까지 배열 뒤에 추가
            if len(answer) < k:
                answer.append(i)
    while len(answer) < k:         # 위에서 만든 배열의 길이 < k 이면 나머지 -1로 채워
        answer.append(-1)
    return answer

print(solution([9, 9, 2, 1, 1],2))