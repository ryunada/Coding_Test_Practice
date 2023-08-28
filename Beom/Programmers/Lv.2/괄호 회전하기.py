def solution(s):
    answer = 0
    for i in range(len(s)):

        if i == 0:
            s1 = s
        else:
            s = s + s[0]
            s = s[1:]
            s1 = s

        while ('()' in s1) | ('[]' in s1) | ('{}' in s1):
            s1 = s1.replace('()', '')
            s1 = s1.replace('{}', '')
            s1 = s1.replace('[]', '')

        if len(s1) == 0:
            answer += 1

    return answer