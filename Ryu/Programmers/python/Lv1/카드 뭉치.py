cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
# cards1 = ["i", "water", "drink"]
# cards2 = ["want", "to"]
# goal = ["i", "want", "to", "drink", "water"]

a = []
def solution(cards1, cards2, goal):
    cards1.append('빈칸')
    cards2.append('빈칸')
    for i in goal:
        # 리스트 두개를 한번에 비교하기 위하여 remove를 사용
        if cards1[0] == i:
            cards1.remove(cards1[0])
        elif cards2[0] == i:
            cards2.remove(cards2[0])
        else:
            return 'No'
    return 'Yes'

print(solution(cards1, cards2, goal))
