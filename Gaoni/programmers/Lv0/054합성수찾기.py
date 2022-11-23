def solution(n):
    answer = 0

    # for i in range(1, int(n**(1/2))):
    #     if n%i ==0 :
    #         answer-=1
    #         if i**2 != n:
    #             answer-=1

    for i in range(1, n + 1):
        for j in range(2, i):
            if i % j == 0:
                answer += 1
                break
    return answer