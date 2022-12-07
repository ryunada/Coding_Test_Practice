cipher = "pfqallllabwaoclk"
code = 2

cnt=0
answer = ''
for i in cipher:
    cnt += 1
    if cnt == code:
        answer += i
        cnt = 0
print(answer)


##

# def solution(cipher, code):
#     answer = ''
#     cnt=0
#     for i in cipher:
#         cnt += 1
#         if cnt == code:
#             answer += i
#             cnt = 0
#     return answer

#####
#
# def solution(cipher, code):
#     answer = cipher[code-1::code]   # code-1부터 code씩 증가
#     return answer