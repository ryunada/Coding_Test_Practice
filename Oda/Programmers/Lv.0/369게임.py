order = 33693

cnt = 0
for i in str(order):
    if i in ['3','6','9']:
        cnt += 1

print(cnt)

##
# def solution(order):
#     answer = 0
#     for i in str(order):
#         if i in ['3','6','9']:
#             answer += 1
#     return answer