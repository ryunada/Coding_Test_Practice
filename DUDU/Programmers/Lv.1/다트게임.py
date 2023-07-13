def solution(dartResult):
    answer = []
    score = []
    list_dart = list(dartResult)
    for i in range(len(list_dart)):
        if list_dart[i] == "1" and list_dart[i+1] =="0" :
            score.append('10')
        elif list_dart[i] == "0" and list_dart[i-1] =="1" :
            pass
        else :
            score.append(list_dart[i])
            
    for i in range(1,len(score)):
        if score[i] == 'S' :
            answer.append(int(score[i-1]))
        elif score[i] == 'D' :
            answer.append(int(score[i-1])**2)
        elif score[i] == 'T' :
            answer.append(int(score[i-1])**3)
        elif score[i] == '*' :
            if len(answer) >= 2:
                answer[-1] *= 2
                answer[-2] *= 2
            else :
                answer[-1] *= 2
        elif score[i] == '#' :
            answer[-1] *= -1
    return sum(answer)
