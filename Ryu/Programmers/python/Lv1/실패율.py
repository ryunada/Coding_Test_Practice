N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# 실패율
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

FR_stages = []
Player_N = len(stages) # 참여자?
stages.sort()
for i in range(1, N+1):
    FR = stages.count(i) / Player_N  # 실패율
    FR_stages.append(round(FR, 3))
    Player_N -= stages.count(i)      # 플에이어 수
print(FR_stages)

