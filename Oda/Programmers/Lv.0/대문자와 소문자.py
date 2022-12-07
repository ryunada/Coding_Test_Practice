
import re

my_string = "cccCCC"

answer = ''
for i in my_string:
    if i.islower():
        answer += i.upper()
    elif i.isupper():
        answer += i.lower()

print(answer)


# def solution(my_string):
#     return my_string.swapcase()