def solution(sides):
    return min(sides)+(sum(sides)-max(sides)-1)

print(solution([11,7]))