def lot_rank(score):
    rank = 0
    if score < 2:
        rank = 6
    elif score == 2:
        rank = 5
    elif score == 3:
        rank = 4
    elif score == 4:
        rank = 3
    elif score == 5:
        rank = 2
    elif score == 6:
        rank = 1
    return rank


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
