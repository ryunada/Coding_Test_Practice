def solution(emergency):
    answer = []
    ems = sorted(emergency,reverse = True)
    for i in emergency :
        answer.append(ems.index(i)+1)
    return answer
