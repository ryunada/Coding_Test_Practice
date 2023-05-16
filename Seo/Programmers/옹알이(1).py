def solution(babbling):
    answer = 0
    for i in babbling:
        #print("babbling=",i)
        for j in ["aya", "ye", "woo", "ma"]:
            #print("words=",j)
            while (j in i):
                i = i.replace(j," ")
                #print("babbling=",i)
                if i.replace(" ","") == "":
                    answer += 1
                    #print(answer)
                    break
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))