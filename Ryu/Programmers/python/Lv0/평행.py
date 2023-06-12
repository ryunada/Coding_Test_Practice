# 2023.02.14 이전
#
# def solution(dots):
#     answer = 0
#     slop = []
#     for i in range(0,len(dots)-1):
#         for j in range(i+1,len(dots)):
#             if(dots[j][0]-dots[i][0]) == 0:
#                 continue
#             slop.append((dots[j][1]-dots[i][1])/(dots[j][0]-dots[i][0]))
#
#     for i in range(0,len(dots)-1):
#         for j in range(i+1,len(dots)):
#             dots[j]
#     if (len(slop) == len(set(slop))):
#         return 0
#     return 1
#
# dots = [[1,5],[5,4],[1,1],[5,1]]
# slop = []
#
# print(solution(dots))

# 2023.02.14 이후
# dots = [[1,4],[9,2],[3,8],[11,6]]

dots = [[3, 5], [4, 1], [2, 4], [5, 10]]
def solution(dots):
    # 기울기
    slop = []
    for i in range(0, len(dots)-1):
        for j in range(i+1, len(dots)):
            slop.append((dots[i][1] - dots[j][1])/(dots[i][0] - dots[j][0])) # 두 점의 기울기

    for i in range(3):
        if slop[i] == slop[-i-1]:   # 처음과 끝 비교 해서 같으면 평행
            return 1
    return 0

print(solution(dots))
