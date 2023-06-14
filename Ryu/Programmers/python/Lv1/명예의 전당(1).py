k = 3
score = [10, 100, 20, 150, 1, 100, 200]

def solution(k, score):
    result = []
    answer = []
    for i in score:
        result.append(i)            # 일단 추가
        if len(result) > k:         # 명예의 전당에
            result.remove(i)        # 자리가 넘어버리면 제거 이후 조건에 맞게 추가
            if (i >= min(result)) & (i != min(result)): # i != min(result)는 없어도 되지만 불필요한 반복을 없애기 위해 사용
                result.remove(min(result))   # 며예의 전당 안에 있는 최소값이 i 보다 작으면 제거
                result.append(i)             # 없어진 점수 보다 크기때문에 추가
        answer.append(min(result))
    return answer