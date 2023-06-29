def solution(name, yearning, photo):
    result = []
    for i in photo:
        score = 0
        for j in i:
            if j in name:
                idx = name.index(j)
                score += yearning[idx]
        result.append(score)

    return result