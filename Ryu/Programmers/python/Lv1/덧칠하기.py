# ex1
# n, m = 8, 4
# section = [2, 3, 6]

# ex2
n, m = 17, 3
section = [2, 3, 6, 11, 17]

# ex3
# n, m = 4, 1
# section = [1, 2, 3, 4]

# 첫번째 생각 실패 중간에 비어있으면 안됨
# import math
# def solution(n, m, section):
#     return math.ceil((max(section) - min(section) + 1)/m)

def solution(n, m, section):
    result = 0
    fill_paint = 0
    for i in section:
        if i < fill_paint:      # 페인트를 색칠한곳이면 뛰어넘기
            continue
        result += 1
        fill_paint = i + m      # 페인트를 칠한곳의 최대값 갱신
    return result

print(solution(n, m, section))