def solution(numbers, hand):
    answer = ''  
    dic = {1: [0, 3], 2: [1, 3], 3: [2, 3],
           4: [0, 2], 5: [1, 2], 6: [2, 2],
           7: [0, 1], 8: [1, 1], 9: [2, 1],
          '*':[0, 0], 0: [1, 0], '#': [2, 0]}
    
    L_start = dic['*']
    R_start = dic['#']
    
    for i in numbers :
        now = dic[i]
        if i in [1,4,7] :
            answer += 'L'
            L_start = now
        elif i in [3,6,9] :
            answer += 'R'
            R_start = now
        elif i in [0,2,5,8] :
            # 좌표 거리 구하기
            L_dis = abs(L_start[0]-dic[i][0])+abs(L_start[1]-dic[i][1])
            R_dis = abs(R_start[0]-dic[0][0])+abs(R_start[1]-dic[i][1])
            
            # 왼손이 가까울 경우
            if L_dis < R_dis :
                answer += 'L'
                L_start = now
            
            elif L_dis > R_dis :
                answer += 'R'
                R_start = now 
            
            else :
                if hand == 'left' :
                    answer += 'L'
                    L_start = now
                else :
                    answer += 'R'
                    R_start = now
    return answer
