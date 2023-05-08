def solution(s):
    answer = 0
    if len(s)==4 or len(s)==6:
        for i in range(len(s)):
            if s[i]>="0" and s[i]<="9":
                answer+=1
    if answer == len(s):
        return True
    else:
        return False

print(solution("a234"))
print(solution("1234"))