def solution(n):
    #     fac = 1
    #     answer = 0

    # #     if fac>n:
    # #         return answer
    # #     else:
    # #         for i in range(1, 11):
    # #             fac=fac*i
    # #             answer = i

    #     for i in range(1, 11):
    #         if fac<n:
    #             fac=fac*i
    #         elif fac>=n:
    #             return i-1

    fac = [i for i in range(11)]
    fac[0] = 1
    for i in fac:
        fac[i] = fac[i - 1] * fac[i]

    fac.append(n)
    fac.sort()
    print(fac)

    answer = fac.index(n)
    if fac[answer] == fac[answer + 1]:
        return answer
    else:
        return answer - 1
#     return answer