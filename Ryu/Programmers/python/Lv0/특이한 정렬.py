numlist = [1,2,3,4,5,6]
n = 4
# numlist = [10000,20,36,47,40,6,10,7000]
# n = 30

def solution(numlist, n):
    numlist_f = list()  # n 이전
    numlist_l = list()  # n 이후 (n 포함)
    numlist.sort()

    for i in numlist:
        if i >= n:
            numlist_l.append(i)  # n 이후(n 포함)
        else:
            numlist_f.append(i)  # n 이전

    for i in range(len(numlist_f) - 1, -1, -1):
        for j in range(len(numlist_l)):
            if abs(numlist_l[j] - n) > abs(numlist_f[i] - n): # 기본 뒤 리스트 수 보다 더 작으면 해당 수 앞에 추가
                numlist_l.insert(j, numlist_f[i])
                numlist_f.remove(numlist_f[i])
                break
    for i in range(len(numlist_f) - 1, -1, -1): # 나머지 앞에것들
        numlist_l.append(numlist_f[i])
    return numlist_l



print(solution(numlist, n))




