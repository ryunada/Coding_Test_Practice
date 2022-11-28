def solution(land):
    answer = 0
    for i in range(len(land)):
        answer += max(land[i])
        # 이거 왜 아님?????????????
        if i != len(land)-1:
            land[i+1][land[i].index(max(land[i]))] = 0
    return answer