def solution(my_string):
    answer = []
    for i in str(my_string):
        if i.isdigit() == True :
            answer.append(int(i))
    return sum(answer)
