import re

my_string = "h12392"

# [0-9]    /d
a = re.findall(r'\d', my_string)

s = [int(i) for i in a]
s.sort()
print(s)


# import re
#
# def solution(my_string):
#     answer = []
#     a = re.findall(r'\d', my_string)
#     answer = [int(i) for i in a]
#     answer.sort()
#
#     return answer