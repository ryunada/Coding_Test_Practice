# 키를 최소한 몇 번 눌러야 하는지
def solution(keymap,targets):
    answer = [0] * len(targets)                     # target개수만큼 answer 배열 요소 생성
    for i in range(len(targets)):                   # 문자열 분리(for 한글자씩 비교)
        targets[i] = list(targets[i])
    for i in range(len(keymap)):
        keymap[i] = list(keymap[i])

    for i in range(len(targets)):
        for j in range(len(targets[i])):
            arr = [101] * len(keymap)               # keymap의 배열 속 배열끼리 비교하기 위해 arr 생성
            for k in range(len(keymap)):            # keymap에서 눌러야하는 횟수(인덱스+1) 각각 arr에 저장
                if targets[i][j] in keymap[k]:
                    arr[k] = keymap[k].index(targets[i][j]) + 1
            targets[i][j] = min(arr)                # targets의 알파벳을 최솟값으로 치환

            if targets[i][j] == 101:                # 101(존재X)이면 -1로 바꿔
                targets[i][j] = -1
        if '-1' in str(targets[i]):                 # 중간에 존재하지 않는 알파벳이 포함된 경우: 나중에 횟수 더해줄때 4 + (-1) + 3 방지
            answer[i] = -1                          # -1 포함하면 answer = -1
        else:
            answer[i] = sum(targets[i])

    return answer

print(solution(["AAEDFS","DFSAA","KEMAS"], ["GMP","P","AF"]))