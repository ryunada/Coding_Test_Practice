def solution(common):
    d = None
    r = None
    if common[1] - common[0] == common[2] - common[1]:
        d = common[1] - common[0]
    elif common[1] // common[0] == common[2] // common[1]:
        r = common[1] // common[0]
    if d is None:
        answer = common[len(common) - 1] * r
    else:
        answer = common[len(common) - 1] + d

    return answer

print(solution([2,4,8]))