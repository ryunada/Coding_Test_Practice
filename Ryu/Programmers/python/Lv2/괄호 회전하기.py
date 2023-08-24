# ex1)
# s = "[](){}"

# ex2)
s = "}]()[{"

# ex3)
# s = "[)(]"

# ex4)
# s = "}}}"

# def solution(s):
#     answer = -1
#     return answer


result = 0
for i in range(len(s)):
    print(f"변환 전 : {s}")
    s_c = s[:]
    for j in range(len(s)//2):
        print(f"변환 전 s_c : {s_c}")
        # 쓸데 없는 메모리 낭비를 줄이기 위해 if 사용
        if s_c.find('{}') != -1:
            s_c = s_c.replace('{}', '')
        elif s_c.find('[]') != -1:
            s_c = s_c.replace('[]', '')
        elif s_c.find('()') != -1:
            s_c = s_c.replace('()', '')
    print(f"변환 후 s_c : {s_c}")
    if len(s_c) == 0:
        result += 1
    print(s)
    s += s[0]
    s = s[1:]

print(result)