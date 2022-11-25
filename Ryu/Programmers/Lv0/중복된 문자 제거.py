def solution(my_string):
    answer = list(my_string)
    answer = set(answer)
    return answer

my_string = "people"
answer = list(my_string)
result = []
for i in range(0,len(answer)):
    for j in range(i,len(answer)):
        result.append(answer[i])
        if answer[i] == answer[j]:
            continue
print(result)

