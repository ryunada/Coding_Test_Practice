def solution(keymap, targets):
    answer = [0] * len(targets)
    for t in range(len(targets)):
        for i in range(len(targets[t])):
            save = []  # targets의 값을 keymap의 인덱스와 비교해서 숫자를 추가해서 비교를 하기 위해 만든 방
            for j in range(len(keymap)): 
                if targets[t][i] in keymap[j]: # keymap의 @번인덱스안에 인덱스들의 값이 있는가?
                    save.append(keymap[j].index(targets[t][i])+1) # 있다면 그 값에 해당되는 keymap의 인덱스를 저장
            if len(save) == 0:   # 저장된 값이 없다면 
                answer[t] = -1   # -1을 호출
                break
            else:
                answer[t] += min(save) # save에 내부의 값 중에서 최소값만 answer에 더하라
    return answer
