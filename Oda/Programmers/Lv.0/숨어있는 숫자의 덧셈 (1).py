import re

my_string = "aAb1B2cC34oOp"

a = re.findall(r'\d', my_string)
print(a)
answer = 0
for i in a:
    answer += int(i)
print(answer)

# import re
#
# def solution(my_string):
#     answer = 0
#     a = re.findall(r'\d', my_string)
#     for i in a:
#         answer += int(i)
#     return answer