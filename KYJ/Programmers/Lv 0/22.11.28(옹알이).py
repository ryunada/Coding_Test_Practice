# aya, ye, woo, ma
# 중복되지 않게 조합

a = 'aya'
b = 'ye'
c = 'woo'
d = 'ma'
e = ''

bab = list()


for i in (a, b, c, d):
    element = ''
    element_1 = element + i
    bab.append(element_1)
    for j in (a, b, c, d):
        if i == j:
            pass
        else:
            element_2 = element_1 + j
            bab.append(element_2)
            for k in (a, b, c, d):
                if k == j:
                    pass
                elif k == i:
                    pass
                else:
                    element_3 = element_2 + k
                    bab.append(element_3)
                    for h in (a, b, c, d):
                        if h == k:
                            pass
                        elif h == j:
                            pass
                        elif h == i:
                            pass
                        else:
                            element_4 = element_3 + h
                            bab.append(element_4)


def solution(babbling):
    num = 0

    for i in range(len(babbling)):
        if babbling[i] in bab:
            num += 1
        else:
            pass

    return num

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))