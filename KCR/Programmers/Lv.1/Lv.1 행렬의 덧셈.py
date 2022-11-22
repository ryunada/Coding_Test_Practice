def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2) :
        a = []
        for k, l in zip(i, j) :
            a.append(k+l)
        answer.append(a)
    return answer

arr1 = [[1,2],[2,3]] ; arr2=	[[3,4],[5,6]]	# [[4,6],[7,9]]
arr1 = [[1],[2]]; arr2=	[[3],[4]]	# [[4],[6]]
print(solution(arr1, arr2))