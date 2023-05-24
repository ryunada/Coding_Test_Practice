def solution(dots):
    x1 , y1 = dots[0][0] , dots[0][1]
    x2 , y2 = dots[1][0] , dots[1][1]
    x3 , y3 = dots[2][0] , dots[2][1]
    x4 , y4 = dots[3][0] , dots[3][1]
    if (y2-y1)/(x2-x1) == (y4-y3)/(x4-x3) :
        return 1
    elif (y3-y1)/(x3-x1) == (y4-y2)/(x4-x2) :
        return 1
    else :
        return 0
