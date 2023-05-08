def solution(quiz):
    a = [0] * len(quiz)   # a=[]
    b = []
    answer = []
    for i in range(0,len(quiz)):
        a[i] = quiz[i].split("=")  # a.append(quiz[i].split("="))
        if '+' in a[i][0]:
            b = a[i][0].split(' + ')
            if int(b[0]) + int(b[1]) == int(a[i][1]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            b = a[i][0].split(' - ')
            if int(b[0]) - int(b[1]) == int(a[i][1]):
                answer.append("O")
            else:
                answer.append("X")
    return answer

print(solution(["-19 - 6 = 13", "-5 + 66 = 61"]))




