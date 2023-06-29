def solution(arr, query):
    for i in range(0,len(query)):
        if i % 2 == 0:
            del arr[query[i]+1:len(arr)]
        else:
            del arr[0:query[i]]
    return arr