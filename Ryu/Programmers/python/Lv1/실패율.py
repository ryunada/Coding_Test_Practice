# 실패율
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

N = 8
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# 런타임 에러

def solution(N, stages):
    Player_N = len(stages) # 참여자?
    dic = {}
    for i in range(1, N+1):
        if Player_N != 0:
            FR = stages.count(i) / Player_N  # 실패율
        else:
            FR = 0
        Player_N -= stages.count(i)  # 플에이어 수
        dic[i] = FR
    return sorted(dic, key = lambda  x:dic[x], reverse= True)

# def solution(N, stages):
#     Player_N = len(stages) # 참여자?
#     FR_l = []
#     ranks = []
#     for i in range(1, N+1):
#         if Player_N == 0:
#             pass
#         FR = stages.count(i) / Player_N  # 실패율
#         Player_N -= stages.count(i)  # 플에이어 수
#         FR_l.append(FR)
#     print(FR_l)
#     return ranks
    # return sorted(dic, key = lambda  x:dic[x], reverse= True)

print(solution(N, stages))