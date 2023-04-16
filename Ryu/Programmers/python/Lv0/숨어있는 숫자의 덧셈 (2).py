my_string = "aAb1B2cC34oOp1"
result = 0
str = ''
for i in my_string:
    if i.isdigit() == 1:
        str += i
    else:
        if len(str) == 0:
            continue
        result += int(str)
        str = ''
if len(str) != 0:
    result += int(str)
print(result)

def solution(my_string):
    result = 0
    str = ''
    for i in my_string:
        # 숫자면 str에 문자열로 집어넣기
        if i.isdigit() == 1:
            str += i
        else:
            # str이 비어져있으면 통과
            if len(str) == 0:
                continue
            # 숫자가 아니고 문자인 경우 멈춰서 이때까지의 str 더해주기
            result += int(str)
            str = ''

    # 마지막에 숫자가 오는 경우
    if len(str) != 0:
        result += int(str)
    return result

def solution_1(my_string):
    n = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in n.split())
