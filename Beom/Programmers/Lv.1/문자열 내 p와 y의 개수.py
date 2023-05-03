def solution(s):
    pn=0
    yn=0
    for i in range(len(s)):
        if s[i]=="p" or s[i]=="P":
            pn +=1
        elif s[i]=="y" or s[i]=="Y":
            yn +=1
    if pn==yn:
        return True
    else:
        return False

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print(solution("PoooyY"))

