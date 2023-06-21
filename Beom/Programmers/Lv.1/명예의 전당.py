def solution(k, score):
    answer = []
    k_score = []
    for i in score:
        if len(k_score)<k:
            k_score.append(i)
        elif (len(k_score)==k) & (i>k_score[0]):
            k_score[0] = i
        k_score.sort()
        answer.append(k_score[0])
    return answer