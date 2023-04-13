def solution(hp):
    general=5
    soldier=3
    worker=1
    answer = (hp//general) + (hp%general)//soldier + ((hp%general)%soldier)
    return answer

print(solution(9))
