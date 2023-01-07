def solution(A, B):
    if A == B:          # 같은 경우 제외
        return 0
    else:
        A = list(A)     # A와 B가 string이므로 list로 변경
        B = list(B)     # string이면 변경 할 수가 없다.
        answer = 0
        for i in range(0,len(A)-1):
            A.insert(0, A[-1])      # A 첫번째 글자에 마지막 글자 추가
            A.pop(-1)               # A 마지막 글자 삭제
            answer += 1
            if (A == B):            # A 와 B가 같을 때 빼냄
                return answer
        return -1

A = 'Apple'
B = 'eAppl'
print(solution(A,B))