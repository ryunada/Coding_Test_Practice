numbers = "onetwothreefourfivesixseveneightnine"

num = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
       'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
answer = 0
for i in num:
    numbers = numbers.replace(i, str(num[i]))

answer = int(numbers)

# def solution(numbers):
#     num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
#            'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
#     for i in num:
#         numbers = numbers.replace(i, str(num[i]))
#
#     return int(numbers)
#-------------------------------------------------------------------------
# def solution(numbers):
#     for num, eng in enumerate(["zero", "one", "two", "three", "four",
#                               "five", "six", "seven", "eight", "nine"]):
#         numbers = numbers.replace(eng, str(num))
#     return int(numbers)