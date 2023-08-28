# ex1)
# p = "(()())()"

# ex2)
# p = ")("

# ex3)
p = "()()))((()"

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
        else: # p[0] == ')'인 경우 # v : 나머지
            print(p_p)
            break

    result += p[:o_n * 2]
    u = p[:o_n * 2]
    v = p[o_n*2 :]
    p_p = v[:]
    print(f"result : {result}")
    print(f"u : {u}")
    print(f"v : {v}")

# print(solution(p))