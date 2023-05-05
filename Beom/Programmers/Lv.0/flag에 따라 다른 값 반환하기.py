def solution(a, b, flag):
    if flag == 1:
        return a+b
    elif flag == 0:
        return a-b


print(solution(-4,7,"true"))
print(solution(-4,7,"false"))