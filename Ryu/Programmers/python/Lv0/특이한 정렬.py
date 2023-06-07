# numlist = [1,2,3,4,5,6]
# n = 4
numlist = [10000,20,36,47,40,6,10,7000]
n = 30
# def solution(numlist, n):
result = list() # 결과
numlist_f = list() # n 이전
numlist_l = list() # n 이후 (n 포함)
numlist.sort()

for i in numlist:
    if i < n:
        numlist_f.append(i) # n 이전
    else:
        numlist_l.append(i) # n 이후(n 포함)

print(f"앞 : {numlist_f}")
print(f"뒤 : {numlist_l}")

# solution(numlist, n)