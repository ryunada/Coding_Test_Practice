import math
def solution(my_str, n):
    answer = []
    for i in range(0,math.ceil(len(my_str)/n)): # math.ceil  : 올림
        answer.append(my_str[:n])
        my_str = my_str[n:]
    return answer

def other_solution(my_str,n):
    return [my_str[i : i + n] for i in range(0, len(my_str),n)]

print(solution("abc1Addfggg4556b",6))
print(other_solution("abc1Addfggg4556b",6))

