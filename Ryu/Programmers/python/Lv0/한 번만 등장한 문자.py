def solution(s):
    answer = ''
    for i in s:
        a = 0
        for j in s:
            if i == j:
                a += 1
        if a == 1:
            answer += i
    return ''.join(sorted(answer))

s = "abcabcadc"
a = ''
for i in s:
    answer = 0
    for j in s:
        if i == j:
            answer += 1
    if answer == 1:
        a += i
print(a)
