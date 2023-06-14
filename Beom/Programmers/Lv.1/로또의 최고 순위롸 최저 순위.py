def lot_rank(a):
    answer = 0
    if a < 2:
        answer = 6
    elif a == 2:
        answer = 5
    elif a == 3:
        answer = 4
    elif a == 4:
        answer = 3
    elif a == 5:
        answer = 2
    elif a == 6:
        answer = 1
    return answer


def solution(lottos, win_nums):
    answer = []
    n_correct = 0
    n_0 = 0
    for i in lottos:
        if i in win_nums:
            n_correct += 1
        if i == 0:
            n_0 += 1
    min_cor = n_correct
    max_cor = n_correct + n_0

    answer.append(lot_rank(max_cor))
    answer.append(lot_rank(min_cor))
    return answer