# def solution(babbling):
#     shy = ["aya", "ye", "woo", "ma"]
#     answer = 0
#     for i in len(babbling):
#         for j in len(shy):
#             if shy[j] in babbling[i]:
#                 babbling[i]
#                 answer ++
#     return answer

# def solution(babbling):
#     shy = ["aya", "ye", "woo", "ma"]
#     answer = 0
#     for i in babbling:
#         for j in shy:
#             if j*2 in i: # 같은 발음을 하는 것을 어려워 함
#                 continue
#             else:
#                i = i.replace(j, "")
#         if len(i.strip()) == 0:
#                 answer += 1
#     return answer