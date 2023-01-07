# def solution(hp):
#     H = hp // 5
#     hp = hp % 5
#     N = hp // 3
#     hp = hp % 3
#     return H+N+hp

def solution(hp):
    return (hp // 5) + (hp * 5 // 3) + ((hp % 5) % 3)

print(23 // 5)
print(23 % 5)