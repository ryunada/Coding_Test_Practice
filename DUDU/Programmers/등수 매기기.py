def solution(score):
    answer = []
    lis = []
    for i in score :
        lis.append([sum(i)])
    lis_arr = sorted(lis,reverse=True)
    
    for v in lis :
        answer.append(lis_arr.index(v)+1)
    return answer
