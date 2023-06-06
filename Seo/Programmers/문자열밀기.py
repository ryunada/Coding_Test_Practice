def solution(A,B):
    A = list(A)
    B = list(B)
    if A == B:
        answer = 0
    else:
        answer = -1
    for n in range(1, len(A)):
        print(n)
        i = 1
        new = [0] * len(A)
        new[0] = A[len(A) - 1]
        while i <= len(A) - 1:
            new[i] = A[i - 1]
            print(new)
            i += 1
        A = new
        print(A)
        if A == B:
            answer = n
            break
    return answer
print(solution("hello","ohell"))

