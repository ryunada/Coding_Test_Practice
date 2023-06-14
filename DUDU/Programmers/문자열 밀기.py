def solution(A, B):
    C = B * 2
    if A in C:
        return C.find(A)
    else:
        return -1
   
