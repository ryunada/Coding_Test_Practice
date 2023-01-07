# def solution(cipher, code):
#     answer = ''
#     for i in range(len(cipher)):
#         if (i % 4) == 0:
#             answer += cipher[i]
#     return answer

def solution(cipher, code):
    return cipher[code-1::code]

cipher = "dfjardstddetckdaccccdegk"
code = 4
a = []
for i in range(len(cipher)):
    if (i % 4) == 0 :
      a.append(cipher[i])
