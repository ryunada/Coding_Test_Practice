# 그리움 점수합산
#name = ["may", "kein", "kain", "radi"]
#yearning = [5, 10, 1, 3]
#photo = [["may"],["kein", "deny", "may"], ["kon", "coni"]]
def solution(name, yearning, photo):
    score = [0] * len(photo)
    for i in range(0, len(photo)):
        score[i] = 0
        for j in range(0, len(photo[i])):
            if photo[i][j] in name:
                # photo 안의 이름 중 name에 해당하는 것이 있으면 점수로 이름을 바꿔
                k = name.index(photo[i][j])  # 인덱스 추출
                photo[i][j] = yearning[k]  # photo 안의 이름을 점수로 바꿈
            else:
                photo[i][j] = 0
            score[i] += photo[i][j]
    return score

