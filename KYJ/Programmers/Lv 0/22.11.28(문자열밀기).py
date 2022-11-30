# hello -> elloh
# 밀기전 문자열A와 밀고난 문자열B를 입력받아 민 횟수를 구하시오

def solution(A,B):
    a = {}
    for i in range(1, len(A)):
        a[A] = 0
        b = A[i:] + A[:i]
        a[b] = len(A) - i

    if B in a:
        answer = a[B]
    else:
        answer = -1

    return(answer)


print(solution('hello','ohell'))
print(solution('apple','elppa'))