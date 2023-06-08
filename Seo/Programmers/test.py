numlist = [1,2,3,4,5,6]
n=4
newlist1 = [0]*len(numlist)
newlist2 = [0]*len(numlist)
# 거리 구하기
for i in range(0,len(numlist)):
    newlist1[i] = abs(numlist[i]-n)
print(newlist1)

# 가까운 순위 매겨서 새로운 배열 생성
k = min(newlist1)
for i in range(0,len(numlist)):
    if newlist1