
def solution(array):
    array.sort()
    return array[len(array)//2]

# def solution(array):
#     array.sort()
#     if len(array) == 1:
#         return array[0]
#     elif len(array) % 2 == 0:
#         return (array[len(array)//2 - 1]+array[len(array)//2])/2
#     elif len(array) % 2 == 1:
#         return array[len(array)//2]
# array = [1,2,7,10,11]]
array = [9, -1, 0,1]
print(len(array)/2)
print(solution(array))