def solution(numlist, n):
    diff = []
    answer = []
    for i in numlist: # n과 i의 차이를 절대값으로 diff에 저장
        diff.append(abs(i-n))
    diff.sort() # 오름차순
    for i in diff:
        if (n+i in numlist) & (n+i not in answer): # +가 먼저라서
            answer.append(n+i)
        else:
            answer.append(n-i)
    return answer