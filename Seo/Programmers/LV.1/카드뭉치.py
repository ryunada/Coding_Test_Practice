#cards1 = ['i','want','water'] # i water want 0 2 1
#cards2 = ['to','drink','bread']
#goal = ['i','want','to','drink','water']

# 1. cards1에서 뽑은 것들이 순서대로 있는지 확인
# 2. cards2에서 뽑은 것들이 순서대로 있는지 확인
# 3. 뽑힌것들의 개수와 goal의 개수가 같은지 -> YES else -> NO

def solution(cards1, cards2, goal):
    num1 = []
    num2 = []
    n = 0
    # cards에서 goal과 일치하면 cards의 인덱스를 각각 새로운 배열에 저장
    for i in goal:
        for j in range(0, len(cards1)):
            if i == cards1[j]:
                num1.append(j)
        for k in range(0, len(cards2)):
            if i == cards2[k]:
                num2.append(k)
    # 인덱스가 순서대로 들어있는지 확인 -> 순서대로 들어있지않으면 1점
    for i in range(0, len(num1) - 1):
        if num1[i + 1] - num1[i] != 1:
            n += 1
    for i in range(0, len(num2) - 1):
        if num2[i + 1] - num2[i] != 1:
            n += 1
    # 뽑힌 것들의 개수와 goal 안에 들어있는 개수가 일치하는지 확인
    # -> 일치하지 않으면 1점(cards에 적힌 단어들로 만들 수 없다는 것)
    if len(num1) + len(num2) != len(goal):
        n += 1
    # 0점이면 조건에 부합한다는 것 -> Yes
    if n == 0:
        return "Yes"
    else:
        return "No"