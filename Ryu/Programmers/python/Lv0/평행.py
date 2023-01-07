
def solution(dots):
    answer = 0
    slop = []
    for i in range(0,len(dots)-1):
        for j in range(i+1,len(dots)):
            if(dots[j][0]-dots[i][0]) == 0:
                continue
            slop.append((dots[j][1]-dots[i][1])/(dots[j][0]-dots[i][0]))

    for i in range(0,len(dots)-1):
        for j in range(i+1,len(dots)):
            dots[j]
    if (len(slop) == len(set(slop))):
        return 0
    return 1

dots = [[1,5],[5,4],[1,1],[5,1]]
slop = []

print(solution(dots))
# print(solution(dots))=
