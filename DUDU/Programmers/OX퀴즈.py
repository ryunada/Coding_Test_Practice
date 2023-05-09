def solution(quiz):
    answer = []
    for i in quiz :
        n = i.split(" ")
        if n[1] == "+" :
            if int(n[0])+int(n[2]) == int(n[4]) :
                answer.append("O")
            else :
                answer.append("X")
        elif n[1] == "-" :
            if int(n[0])-int(n[2]) == int(n[4]) :
                answer.append("O")
            else :
                answer.append("X")     
    return answer
