def solution(A, B):
    n = 0
    while n < len(A):
        if A == B:
            break
        else:
            n += 1
            AA = A[-1]
            for i in range(len(A) - 1):
                AA += A[i]
            A = AA
    if n < len(A):
        return n
    else:
        return -1
