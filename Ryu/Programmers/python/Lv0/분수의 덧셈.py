def solution(denum1, num1, denum2, num2):
    result = [] # 결과
    common = []  # 공통
    num_divisor = [] # 분자 약수
    denum_divisor = [] # 분모 약수
    num = denum1*num2 + denum2*num1 # 분자
    denum = num1*num2 # 분모
    for i in range(1, num+1):
        if (num % i) == 0:
            num_divisor.append(i)
    for j in range(1, denum+1):
        if (denum % j) == 0:
            denum_divisor.append(j)
    for a in num_divisor:
        for b in denum_divisor:
            if a == b:
                common.append(a) # 공약수
    z = max(common)
    num = num/z
    denum = denum/z
    result.append(int(num))
    result.append(int(denum))
    return result, common, z


# print(solution(1, 2, 3, 4))
# print(solution(9, 2, 1, 3))
# print(solution(1,1,1,1))
# print(solution(2,9,3,1))
# print(solution(8,3,2,7))
# print(solution(12,20,24,40))
print(solution(7,105,13,15))