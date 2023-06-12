n = 4
result = [[]]
result = [[0] * n for i in range(n)]
print(f"빈 배열 생성 : {result}")

k = 1
for i in range(n):
    for j in range(n):
        if i == 0:
            result[i][j] = k
            k += 1
            print(f"result[{i}][{j}]에 {k}가 추가 되었습니다.")
            continue
        if j == n-1:
            result[i][j] = k
            k += 1
            print(f"result[{i}][{j}]에 {k}가 추가 되었습니다.")
            continue
    for j in range(n-2,-1,-1):
        if i == n-1:
            result[i][j] = k
            k += 1
            print(f"result[{i}][{j}]에 {k}가 추가 되었습니다.")
            continue

        # if j == 0:
        #     k += 1
        #     result[i][j] = k
        #     print(f"result[{i}][{j}]에 {k}가 추가 되었습니다.")
        #     continue

print(f"완성된 배열 : {result}")

