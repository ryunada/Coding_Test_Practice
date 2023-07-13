def solution(dartResult):
    dartResult += " "
    score=[]
    for i in range(len(dartResult)-1):
        if (dartResult[i].isdigit()) & (dartResult[i+1].isdigit()):
            score.append(10)
        elif (dartResult[i].isdigit()) & (dartResult[i-1].isdigit()) :
            pass
        elif dartResult[i].isdigit():
            score.append(int(dartResult[i]))
        elif dartResult[i]=='D':
            score[-1] = score[-1]**2
        elif dartResult[i]=="T":
            score[-1] = score[-1]**3
        elif dartResult[i]=="*":
            if len(score) != 1:
                score[-2] = score[-2]*2
                score[-1] = score[-1]*2
            else:
                score[-1] = score[-1]*2
        elif dartResult[i]=="#":
            score[-1] = score[-1] * (-1)
    return sum(score)