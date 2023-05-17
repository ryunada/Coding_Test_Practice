code = "abc1abc1abc"
mode = 0
result = []

mode = 0
result = ''
# V1
def solution(code):
    mode = 0
    result = ''
    for i in range(len(code)):
        if code[i] == '1':
            mode += 1
        else:
            if (mode % 2 == 0) & (i % 2 == 0): # mode = 0 일때 짝수 추가
                result += code[i]
            elif (mode % 2 == 1) & (i % 2 == 1): # mode = 1 일때 홀수 추가
                result += code[i]
    if len(result) == 0:
        return 'EMPTY'
    else:
        return result

