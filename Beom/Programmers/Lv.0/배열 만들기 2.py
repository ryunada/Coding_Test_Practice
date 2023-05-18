def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if i % 5 != 0:
            continue
        a = 0
        b=str(i)
        for j in range(len(b)):
            if b[j] == "5" or b[j] == "0":
                a += 1
        if a == len(b):
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    else:
        return answer

print(solution(5,555))
#
# a=1234523
# for i in range(len(str(a))):
#     if str(a)==
# print(str(a)[3])