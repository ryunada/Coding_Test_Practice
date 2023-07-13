# ex1
# dartResult = "1S2D*3T"
# ex2
dartResult = "1D2S#10S"
# 문자열 식을 계산해줌 eval
def solution(dartResult):
    dart_l = list(dartResult)
    formula = []
    for i in range(len(dart_l)):
        # Single, Double, Triple
        if dart_l[i] == 'S':
            formula.append('**1')
        elif dart_l[i] == 'D':
            formula.append('**2')
        elif dart_l[i] == 'T':
            formula.append('**3')
        elif (dart_l[i] == '*') & (i == 3):      # 첫번째숫자에 아차상('*')
            formula.append('*2')                 # 자기 자신 * 2
        elif (dart_l[i] == '*') & (i != 3):
            formula.insert(len(formula)-3,'*2')  # 이전 식에 * 2
            formula.append('*2')                 # 자기 자신 * 2
        elif dart_l[i] == '#':
            formula.append('*(-1)')
        elif (dart_l[i] == '1') & (dart_l[i+1] == '0'): # 숫자가 10일떄
            formula.append('+')
            formula.append('10')
        elif (dart_l[i-1] == '1') & (dart_l[i] == '0'):
            continue
        else:   # 맨 처음이 0인경우가 안되네
            formula.append('+')
            formula.append(dart_l[i])



    print(formula[1:])
    result = ''
    for i in formula[1:]: # 맨 앞의 + 제외하기 위해 1부터 시작
        result += i
    print(result)
    return eval(result)
print(solution(dartResult))