# def solution(my_string):
#     answer = ['a','e','i','o','u']
#     for i in answer:
#         my_string = my_string.replace(i, '')
#     return my_string

def solution(my_string):
    answer = ''
    for i in my_string:
        if i in ['a','e','i','o','u']:
            continue
        answer += i
    return answer