def solution(num, k):
    answer = -1
    nu = str(num)
    for i in range(len(nu)) :
        if int(nu[i]) == k :
            return i+1
    return answer
