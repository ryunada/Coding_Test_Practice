def solution(n, arr1, arr2):
    arr = []
    for i, j in zip(arr1, arr2) :
        a = bin(i).split('b')[1]
        b = bin(j).split('b')[1]
        add = ''
        for k, l in zip('0'*(n-len(a))+a, ('0'*(n-len(b))+b)) :
            if (k == '0') and (l == '0') :
                add += ' '
            else :
                add += '#'
        arr.append(add)
    return arr
