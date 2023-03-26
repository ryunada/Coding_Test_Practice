def solution(array, n):
    result = list()
    array = sorted(array)
    for i in array:
        result.append(abs(i - n))
    return array[result.index(min(result))]

array = [3, 15, 11]
n = 13



