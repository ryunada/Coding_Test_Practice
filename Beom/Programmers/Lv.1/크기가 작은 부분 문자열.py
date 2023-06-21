def solution(t, p):
    result = 0
    for i in range(0,len(t)):
        num = t[i:i+len(p)]
        if int(num) <= int(p):
            result+=1
        if len(t) <= i+len(p) :
            break
    return result
        # for j in range(len(p)):
        #     if i+j < len(t):
        #         obj += t[i+j]
        # t_split.append(obj)

    # result = 0
    # for i in t_split:
    #     if int(i)<=int(p):
    #         result+=1

    # return t_split

print(solution("10203","15"))
