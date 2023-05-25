def solution(arr, query):
    for i,j in enumerate(query):
        if i%2==0: #query 인덱스가 짝수인 경우
            arr = arr[:j+1]
        else: #query 인덱스가 홀수인 경우
            arr = arr[j:]
    return arr
print(solution([0, 1, 2, 3, 4, 5],[4, 1, 2]))