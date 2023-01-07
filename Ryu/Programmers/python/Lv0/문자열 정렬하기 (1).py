def solution(my_string):
    answer = []
    Number = []
    for i in range(0, 10):
        Number.append(str(i))
    for j in my_string:
        if j in Number:
            answer.append(int(j))
    return answer.sort()


my_string = "hi12392"
answer = []
Number = []
for i in range(0, 10):
    Number.append(str(i))
for j in my_string:
    if j in Number:
        answer.append(int(j))
print(sorted(answer))