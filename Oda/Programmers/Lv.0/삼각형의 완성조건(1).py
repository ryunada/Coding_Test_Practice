# sides = [1, 2, 3]
#
# M = sides.index(max(sides))

# c > a,b
# a+b > c

answer = 0
sides = [1,2,3]

ms = max(sides)
sides.remove(ms)

if sum(sides) > ms:
    answer = 1
else:
    answer = 2

#——————————————
# def solution(sides):
#     answer = 0
#
#     ms = max(sides)
#     sides.remove(ms)
#
#     if sum(sides) > ms:
#         answer = 1
#     else:
#         answer = 2
#
#     return answer
#————————————————
# def sol(sides):
#     return 1 if max(sides) <= (sum(sides) - max(sides)) else 2