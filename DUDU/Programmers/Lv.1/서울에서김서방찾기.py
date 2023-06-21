def solution(seoul):
    answer = ''
    for i in seoul :
        if i == "Kim" :
            answer = '김서방은 {}에 있다'.format(seoul.index(i))
    return answer
