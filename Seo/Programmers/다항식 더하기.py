def solution(polynomial):
    c1 = 0
    c2 = 0
    c = polynomial.replace(" ", "").split('+')
    for i in range(0, len(c)):
        if 'x' in c[i]:
            if c[i].replace('x','') != '':
                c1 += int(c[i].replace('x',''))
            else:
                c1 += 1
        else:
            c2 += int(c[i])

    if c1 == 1:
        if c2 == 0:
            answer = 'x'
        else:
            answer = 'x + ' + str(c2)
    elif c1 == 0:
        if c2 == 0:
            answer = ""
        else:
            answer = str(c2)
    else:
        if c2 == 0:
            answer = str(c1) + 'x'
        else:
            answer = str(c1) + 'x + ' + str(c2)

    return answer

print(solution("3x + 7 + x"))
print(solution("100x + 7 + 16x"))
print(solution("x + x + 9"))
print(solution("x + x"))
print(solution("012x + 001x"))
print(solution("7 + 001 + 003 + x"))   #x계수가 1인경우 생각