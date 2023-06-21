def solution(t,p):
    List = []
    for i in range(0,len(t)-len(p)+1): # i = p길이 만큼 자를 때, 시작 인덱스
        List.append(t[i:i+len(p)])     # p길이 만큼 잘라서 List에 추가
    n = 0
    for i in List:                     # i = 자른 문자열을 담은 List의 원소들
        if int(i) <= int(p):           # p보다 작거나 같은 문자열 개수 구하기
            n += 1
    return n

print(solution("3141592","271"))