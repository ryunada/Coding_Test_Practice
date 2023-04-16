def solution(my_string):
    answer = []
    mu = ["a","e","i","o","u"]
    for i in str(my_string) :
        if i not in mu :
            answer.append(i)
    return ''.join(answer)
