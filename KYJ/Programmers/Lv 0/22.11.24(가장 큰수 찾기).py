# 가장 큰수 찾기
# 정수배열 array가 주어질때 가장큰수와 그 수의 인덱스를 담은 배열을 return하도록 solution함수를 완성하시오.

def solution(a):
    n = len(a)

    x=0
    for i in range(n):
        x = max(a[i],x)
    for i in range(n):
        if a[i] == x:
            y=i
            break
        else:
            pass
    return [x,y]


a=[1,3,6,77,39,25,125,98,30]
print(solution(a))