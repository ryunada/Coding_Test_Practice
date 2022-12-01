def solution(s):
    x_cnt = 0
    cnt = 0
    answer = 0

    i = 0
    while i != len(s):
        x = s[0]
        if s[i] == x:
            x_cnt += 1
        else:
            cnt += 1
        i += 1
        if x_cnt == cnt:
            answer += 1
            s = s[i:]
            i = 0
            x_cnt = 0
            cnt = 0

            if i == len(s)-1 :
                answer+= 1
    return answer

s = 'aaabbaccccabba' # 3
print(solution(s))