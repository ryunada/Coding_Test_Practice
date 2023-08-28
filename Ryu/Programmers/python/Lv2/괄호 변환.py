# ex1)
# p = "(()())()"

# ex2)
# p = ")("

# ex3).
p = "()))((()"

result = ''
p_p = p[:]

for i in range(4):
    print(f"{i+1}번째")
    o_n = 0  # 올바른것
    for i in range(len(p_p)//2):
        if p_p[0] == '(':     # u : 올바른 괄호 문자열
            if p_p.find('()') == 0:
                o_n += 1
                p_p = p_p.replace('()','',1)
                a = 0
            break
        else: # p[0] == ')'인 경우 # v : 나머지
            if p_p.find('()') != -1: # 올바른 괄호 문자열이 있다면 그 전까지
                a = 1
                u = p_p[:p_p.find('()')]
                v = p_p[p_p.find('()'):]
            break

    if a == 0:
        result += p[:o_n * 2]
        u = p[:o_n * 2]
        v = p[o_n*2 :]
    # else:

    print(f"result : {result}")
    print(f"u : {u}")
    print(f"v : {v}")

# print(solution(p))