def solution(cards1, cards2, goal):
    for i in goal:
        if (len(cards1) == 0) & (len(cards1) == 0):
            return "No"

        elif len(cards1) == 0:
            if i == cards2[0]:
                del cards2[0]
            else:
                return "No"

        elif len(cards2) == 0:
            if i == cards1[0]:
                del cards1[0]
            else:
                return "No"
        else:
            if i == cards1[0]:
                del cards1[0]
            elif i == cards2[0]:
                del cards2[0]
            else:
                return "No"

    return "Yes"
