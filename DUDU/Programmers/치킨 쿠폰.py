def solution(chicken):
    answer = 0
    while chicken >= 10 :
        mok = chicken//10 
        na = chicken%10
        answer += mok
        chicken = mok+na
    return answer
