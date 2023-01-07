def solution(dot):
    print(dot[0], dot[1])
    if (dot[0] > 0 and dot[1] > 0):
        return 1
    elif (dot[0] < 0 and dot [1] > 0):
        return 2
    elif(dot[0] < 0 and dot[1] < 0):
        return 3
    elif(dot[0] > 0 and dot[1] < 0):
        return 4


dot = [2,4]
print(solution(dot))

print(dot[0] > 1)