my_string = "people"
my_string = list(my_string)
print(my_string)

a = []
for i in my_string:
    if i in a:
        continue
    else:
        a.append(i)
print(a)
s = ''
for i in a:
    s += i
print(s)



# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i not in answer:
#             answer+=i
#     return answer

def solution(my_string):
    my_string = list(my_string)
    answer = ''
    a = []
    for i in my_string:
        if i in a:
            continue
        else:
            a.append(i)

    for i in a:
        answer += i

    return answer