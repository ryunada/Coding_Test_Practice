# def solution(my_string):
#     answer = list(my_string)
#     result = []
#     for i in answer:
#         if i not in result:
#             result.append(i)
#     return ''.join(result)

# Dictionary 사용
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))


my_string = "people"
answer = list(my_string)
result = []
for i in answer:
    if i not in result:
        result.append(i)
print(result)

print(answer)
print(set(answer))

