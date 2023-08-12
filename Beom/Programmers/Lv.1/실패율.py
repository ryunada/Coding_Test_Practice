def solution(N, stages):
    sta_per = {}
    for i in range(1,N+1):
        if i in stages:
            if len(stages) != 0:  #ZeroDivisionError를 피하기 위해 if문 사용
                sta_per[i] = stages.count(i) / len(stages)
                stages = [j for j in stages if j not in {i}]
            else : # 해당 스테이지에 도달한 사용자가 없을 경우 실패율 0
                sta_per[i] = 0
        else:  # i가 stages안에 없다면 해당 스테이지 실패율은 0
            sta_per[i] = 0
    sta_per = sorted(sta_per,key=lambda x:sta_per[x],reverse=True) # value를 기준으로 내림차순 정렬
    return sta_per