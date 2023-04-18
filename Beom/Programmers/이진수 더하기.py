def solution(bin1, bin2):
    answer = ''
    a1 = 0
    b1 = 0
    for i in range(len(bin1)):
        if bin1[i] == "1":
            a1 = a1 + 2 ** (len(bin1) - i - 1)
    for i in range(len(bin2)):
        if bin2[i] == "1":
            b1 = b1 + 2 ** (len(bin2) - i - 1)
    n=a1+b1
    if n == 0:
        return "0"
    else:
        while n !=0:
            if n % 2 == 1:
                answer += "1"
                n = n//2
            elif n % 2 == 0:
                answer += "0"
                n = n//2
    return answer[::-1]

print(solution("0","0"))