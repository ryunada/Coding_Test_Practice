def solution(a, b, n):
    answer = 0
    while (n >= a) :
        remain_cok = n % a # 나머지를 먼저 제외
        n = (n//a)*b       # 목*b의 개수 = 받은 콜라
        answer += n        # 받은 콜라 
        n += remain_cok    # 나머지와 받은 콜라
    return answer
