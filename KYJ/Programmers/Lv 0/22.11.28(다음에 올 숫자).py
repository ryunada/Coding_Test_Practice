# 등차 혹은 등비수열 common이 주어진다.
# 마지막 원소 다음으로 올 숫자를 return하라

def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        answer = common[-1]+common[1]-common[0]
    else:
        answer = common[-1]*common[1]/common[0]
    return answer

print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))