def solution(nums):
    answer = -1
    return answer

nums = [1,2,3,4]
answer = []
# 3가지 숫자
# for i in range(0,len(nums)-2):
#     for j in range(i+1,len(nums)-1):
#         for z in range(j+1,len(nums)):
#             answer.append(nums[i]+nums[j]+nums[z])
# result = 0
# for a in answer:
#     for b in range(2,a):
#         if a % b == 0:
#             break
#         if b == (a-1):
#             result +=1
result = 0
for i in range(0,len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for z in range(j+1,len(nums)):
            for b in range(2,nums[i]+nums[j]+nums[z]):
                if (nums[i]+nums[j]+nums[z])%b == 0:
                    break
                if b == ((nums[i]+nums[j]+nums[z])-1):
                    result += 1
print(answer)
print(result)


