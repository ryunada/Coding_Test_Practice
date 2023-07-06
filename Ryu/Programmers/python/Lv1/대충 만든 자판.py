# ex 1
# keymap = ["ABACD", "BCEFD"]
# targets = ["ABCD", "AABB"]

# ex 2
# keymap, targets = ["AA"], ["B"]

# ex 3
# keymap, targets= ["ABCDE"], ["FGHIJ"]

# ex4
keymap, targets = ["ABCE"], ["ABDE"]

# Prototyping Version
def solution_v1(keymap, targets):
    # keymap에 있는 알파벳이 들어갈 딕셔너리 생성
    key_dic = {}

    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            # 딕셔너리(key_dic) 안에 이미 같은 키가 있고 안의 값이 더 작으면 pass
            if keymap[i][j] in key_dic.keys():
                if key_dic[keymap[i][j]] < j+1:
                    continue
            # 키 : 알파벳 , 값 : 인덱스 + 1
            key_dic[keymap[i][j]] = j+1

    # 결과 담을 리스트
    result = []
    for i in targets:
        a = 0
        for j in i:
            # 알파벳이 딕셔너리(key_dic)안에 있다면 키에 해당하는 값을 더해줌
            if j in key_dic.keys():
                a += key_dic[j]
            # 알파벳이 딕셔너리 안에 없다면 계산이 불가능 하므로 -1
            else:
                a = -1
                break
        result.append(a)
    return result

print(solution_v1(keymap,targets))

# Refactoring Version
