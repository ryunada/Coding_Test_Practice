# 1. 숫자를 요소로 모두 분할하여 리스트로 저장
# 2. 각 자리 숫자를 모두 더하기

def solution(n):
    answer=0
    nl = [int(i) for i in str(n)]
    for i in nl :
        answer += i
    return answer
