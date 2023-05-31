def solution(arr, query):
    result = []
    for i in range(len(query)):
        if i % 2 == 0:
            # 짝수 인덱스인 경우, query[i] 인덱스를 제외한 나머지 부분을 삭제합니다.
            arr = arr[:query[i]+1]
        else:
            # 홀수 인덱스인 경우, query[i] 인덱스를 제외한 나머지 부분을 삭제합니다.
            arr = arr[query[i]:]
    return arr
