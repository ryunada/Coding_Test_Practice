def solution(babbling):
    answer = 0
    for i in babbling:
        #print("babbling=",i)
        for j in ["aya", "ye", "woo", "ma"]:
            #print("words=",j)
            while (j in i):                         # 옹알이 안에 네 가지 발음이 중 하나가 있다면 공백으로 대체
                i = i.replace(j," ")                # "wyeoo" -> "w oo" , 발음만으로 구성됐다면 모두 공백
                #print("babbling=",i)
                if i.replace(" ","") == "":         # 공백 여러 개를 하나로 다루기 위해
                    answer += 1
                    #print(answer)
                    break
    return answer
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))