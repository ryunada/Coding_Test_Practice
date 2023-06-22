t = "3141592"
p = '271'
# t = '500220839878'
# p = '7'

# def solution1(t,p):
#     l = []
#     result = 0
#     for i in range(len(p),len(t)+1):
#         l.append(t[len(l):i])
#
#     for i in l:
#         if int(i) <= int(p):
#             result += 1
#     return result
#
# print(solution1(t,p))

def solution2(t,p):
    result = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            result += 1
    return result

print(solution2(t,p))
