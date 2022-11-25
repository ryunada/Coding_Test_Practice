# 약수 구하기
# 정수 n의 약수를 오름차순으로 담은 배열을 return하도록 solution함수를 완성하시오

def solution(n):
    a=[]
    for i in range(n+1):
        for j in range(n+1):
            if i*j == n:
                a.append(i)
            else:
                pass
    return a

print(solution(27))
print(solution(29))
print(solution(1024))