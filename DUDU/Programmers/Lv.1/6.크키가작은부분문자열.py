#1. list에 저장 후 비교
def solution(t, p):
    answer = 0
    t_li = []  # len(p)에 따른 t를 저장할 방
    for i in range(0, len(t)-len(p)+1): 
        t_li.append(t[i:i+len(p)])  # len(p)에 따른 t를 t_li에 저장

    for v in t_li:  
        if int(v) <= int(p):        # 비교
            answer += 1
    return answer

#2. list에 저장 하지 않고 비교
# def solution(t, p):
#     answer = 0
#     for i in range(len(t)-len(p)+1) :
#         if int(t[i:i+len(p)]) <= int(p):
#             answer+=1
#     return answer

