# https://school.programmers.co.kr/learn/courses/30/lessons/120892
# 암호 해독

def solution(cipher, code):
    answer = ''

    for i in range(code - 1, len(cipher), code):
        answer += cipher[i]

    return answer