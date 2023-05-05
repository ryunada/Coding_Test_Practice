def solution(rank, attendance):
    a=[]
    b=[]
    for i,j in enumerate(attendance):
        if j:
            a.append(i)
    for i in a:
        b.append(rank[i])
        b=sorted(b)
    a1 = rank.index(b[0])
    a2 = rank.index(b[1])
    a3 = rank.index(b[2])
    return a1*10000+a2*100+a3

print(solution([3, 7, 2, 5, 4, 6, 1],[False, True, True, True, True, False, False]))
