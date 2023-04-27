def solution(rank, attendance):
    a=[]
    b=[]
    for i,j in enumerate(attendance):
        if j == "true":
            a.append(i)
    for i in a:
        b.append(rank[a])
    a1 = b.sort()[0]
    a2 = b.sort()[1]
    a3 = b.sort()[2]
    return a

c=[3,6,1,9,2]
print(c.sort())



