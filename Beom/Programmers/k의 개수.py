def solution(i, j, k):
    answer=0
    for n in range(i,j+1):
        for t in range(len(str(n))):
            if int(str(n)[t]) == k:
                answer +=1
    return answer
