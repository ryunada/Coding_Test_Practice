def solution(s1, s2):
    answer = 0
    for i in s1:
        for v in s2 :
            if i == v :
                answer+=1
    return answer
