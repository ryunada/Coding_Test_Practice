import re


def solution(my_string):
    # answer = []
    numbers = re.findall(r'\d', my_string)
    # print(numbers)
    answer = list(map(int, numbers))
    # answer = [int(i) for i in numbers]
    answer = sorted(answer)

    return answer