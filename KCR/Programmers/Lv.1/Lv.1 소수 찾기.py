# '에라토스테네스의 체' 활용
import math
def solution(n):
    answer = 0
    end = math.ceil(n**0.5)
    all = [True] * n # 1~n
    for i in range(2, end+1) :
        if all[i-1] == True : # 리스트는 0부터 시작이므로
            for j in range(i+i, n+1, i) :
                all[j-1] = False
    return len([i for i in range(1, n) if all[i] == True])