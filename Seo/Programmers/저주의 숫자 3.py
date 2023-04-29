def solution(n):
    new=[]
    for i in range(1,200):
        new.append(i)
        if (i % 3 == 0) or ("3" in str(i)):
            new.remove(i)
    return new[n-1]
# print(solution(15))

