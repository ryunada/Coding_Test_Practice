def solution(babbling):
    answer = 0
    for i in babbling:
        a=0
        if "aya" in i:
            a+=3
        if "ye" in i:
            a+=2
        if "ma" in i:
            a+=2
        if "woo" in i:
            a+=3
        if a==len(i):
            answer+=1
    return answer


print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]	))
