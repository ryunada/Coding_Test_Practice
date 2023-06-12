def solution(lottos, win_nums):
    answer = []                   # 0이 아닌 값을 저장할 공간
    result = 0                    # 순위를 부여하기 위해 만듬
    for i in lottos :
        for v in win_nums :
            if i == v :
                answer.append(i)  # 0이 아닌 값을 answer에 저장 
    if len(answer) ==  0 :        # answer에 길이에 따라
        result = 6                # 순위 부여 
    elif len(answer) == 1 :
        result = 6 
    elif len(answer) == 2 :
        result = 5
    elif len(answer) == 3 :
        result = 4
    elif len(answer) == 4 :
        result = 3
    elif len(answer) == 5 :
        result = 2
    elif len(answer) == 6 :
        result = 1 
    
    plus = lottos.count(0)            # lottos의 0의 개수
    if len(set(lottos)) == 1 :        # lottos가 모두 같으면 
        return [result-plus+1,result] # [1,6]을 반환
    else :
        if plus == 0 :                # 0의 개수가 없다면
            return [result,result]    # [1,1]처럼 반환 => 0이 없으면 [1,2]와 같은 경우가 생기지 않음
        else :                        
            return [result-plus,result] # 0이 1,2,3,4,5개인 경우에는 [result-plus,result]사용
