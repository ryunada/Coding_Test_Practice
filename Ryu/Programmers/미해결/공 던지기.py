def solution(numbers, k):
    if len(numbers) == 1:
        return numbers[0]
    elif (len(numbers) % 2) == 0:
        return numbers[(k % (len(numbers) // 2) - 1) * 2]
    else:
        return numbers[(k % ((len(numbers))// 2)-1) * 2 ]

# numbers = [1,2,3,4,5,6]
# k = 1

# numbers = [1]
# k = 2
numbers = [1,2,3,4,5]
k = 2
print(f'길이 :{len(numbers) // 2}')

if len(numbers) == 1:
    print(numbers[0])
elif (len(numbers) % 2) == 0:
    print(numbers[(k % (len(numbers) // 2 +1) - 1) * 2])
else:
    print(numbers[(k - 1) * 2])

print(solution(numbers, k))
# print(numbers[(k%(len(numbers)//2)-1)*2])


