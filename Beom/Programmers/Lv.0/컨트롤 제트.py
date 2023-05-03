def solution(s):
    answer = 0
    a = s.split(" ")
    for i in range(len(a)):
        if i != len(a)-1:
            if a[i+1] != "Z" and a[i] != "Z":
                answer += int(a[i])
        else:
            if a[i] != "Z":
                answer += int(a[i])
    return answer

print(solution("-1 2 -3 Z"))