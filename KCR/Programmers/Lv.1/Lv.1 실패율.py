def solution(N, stages):
    answer = []
    left = len(stages)
    for i in range(1, N+1) :
        if left == 0 :
            answer.append([0, i])
            continue
        answer.append([stages.count(i)/left, i])
        left -= stages.count(i)
    return [a[1] for a in sorted(answer, key= lambda x : (-x[0], x[1]))]