def solution(age):
    answer = ''
    age_string = ['a','b','c','d','e','f','g','h','i','j']
    for i in range(0,4):
        if age/10 > 0:
            answer = (age_string[int(age % 10)]) + answer
            age = int(age / 10)
        else:
            break
    return answer

print(solution(23))

