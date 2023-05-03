def solution(chicken):
    n = chicken//10 + chicken%10
    answer=chicken//10
    while n >= 10:
        answer += n//10
        n = n//10+n%10
    return answer

print(solution(1081))