def solution(order):
    answer = 0
    n = ['3','6','9']
    for i in str(order) :
        if i in n :
            answer+=1
    return answer
