def solution(dots):
    max = [dots[0][0], dots[0][1]]
    min = [dots[0][0], dots[0][1]]
    for i in range(0, 4):
        if [dots[i][0], dots[i][1]] >= max :
            max = [dots[i][0], dots[i][1]]
        if [dots[i][0], dots[i][1]] <= min:
            min = [dots[i][0], dots[i][1]]
    return (max[0]-min[0])*(max[1]-min[1])

# print(solution([[1,1],[2,1],[2,2],[1,2]]))

# 다른 풀이
def solution(dots):
    sorted_dots = sorted(dots)
    width = sorted_dots[3][0] - sorted_dots[0][0]
    length = sorted_dots[3][1] - sorted_dots[0][1]
    return width * length

# print(solution([[1,1],[2,1],[2,2],[1,2]]))