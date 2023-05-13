def solution(before, after):
    answer = 0
    a = list(after)
    a = sorted(a)
    b = list(before)
    b = sorted(b)
    if b == a :
        answer+=1
    return answer
