def solution(n):
    answer=[]
    # 0만을 포함한 n*n 배열생성
    for i in range(n):
        line = []
        for j in range(n):
            line.append(0)
        answer.append(line)

    # 1. i는 0으로 고정, j는 0부터 n-1까지
    # 2. j는 n-1으로 고정, i는 1부터 n-1까지
    # 3. i는 n-1고정, j는 n-2부터 0까지
    # 4. j는 0고정, i는 n-2부터 1까지

    # 5. i는 1고정, j는 1부터 n-2까지
    # 6. j는 n-2고정, i는 2부터 n-2까지
    # 7. i는 n-2고정, j는 n-3부터 1까지
    # 8. j는 1고정, i는 n-3부터 2까지

    # k는 0부터 1씩 늘어나는 수
    # 1. i는 k로 고정 , j는 k부터 n-k-1까지
    # 2. j는 n-k-1로 고정, i가 k+1부터 n-k-1까지
    # 3. i는 n-k-1로 고정 , j가 n-k-2부터 k까지
    # 4. j는 k로 고정 , i가 n-k-2부터 k+1까지
    # 5. 리스트에 요소를 추가할 때 마다 a+=1
    # 6. a==n**2면 break

    a=0
    for k in range(n):
        for j in range(k,n-k):
            i=k
            a += 1
            answer[i][j] = a
            if a==(n**2):
                break
        if a == (n ** 2):
            break
        for i in range(k+1,n-k):
            j = n-k-1
            a += 1
            answer[i][j] = a
            if a == (n ** 2):
                break
        if a == (n ** 2):
            break
        for j in range(n-k-2,k-1,-1):
            i=n-k-1
            a += 1
            answer[i][j] = a
            if a == (n ** 2):
                break
        if a == (n ** 2):
            break
        for i in range(n-k-2,k,-1):
            j=k
            a += 1
            answer[i][j] = a
            if a == (n ** 2):
                break
        if a == (n ** 2):
            break
    return answer





print(solution(5))

# two_d_list = []
# for _ in range(5)
#     line = []
#     for _ in range(10):
#         line.append(0)
#     two_d_list.append(line)