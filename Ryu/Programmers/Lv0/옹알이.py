def solution(babbling):
    shy = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in len(babbling):
        for j in len(shy):
            if shy[j] in babbling[i]:
                babbling[i]
                answer += 1
    return answer