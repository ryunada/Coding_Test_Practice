# '에라토스테네스의 체' 활용
def solution(n):
    answer = 0
    end = int(n**0.5)
    all = [True] * n # 2~n
    for i in range(2, end+1) :
        if all[i] == True :
            for j in range(i+i, n, i) :
                all[j] = False
    return [i for i in range(2, n) if all[i] == True]