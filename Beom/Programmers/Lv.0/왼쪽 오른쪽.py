def solution(str_list):
    answer = []
    for i,j in enumerate (str_list):
        if j == "l":
            for k in range(i):
                answer.append(str_list[k])
            break
        elif j=="r":
            for k in range(i+1,len(str_list)):
                answer.append(str_list[k])
            break
    return answer

print(solution(["u", "u", "l", "r"]))
