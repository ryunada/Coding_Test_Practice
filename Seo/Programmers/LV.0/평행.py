# [a-b, c-d],[a-c, b-d],[a-d, b-c]

def solution(dots):
    if (dots[0][1]-dots[1][1])/(dots[0][0]-dots[1][0]) == (dots[2][1]-dots[3][1])/(dots[2][0]-dots[3][0]):
        return 1
    elif (dots[0][1]-dots[2][1])/(dots[0][0]-dots[2][0]) == (dots[1][1]-dots[3][1])/(dots[1][0]-dots[3][0]):
        return 1
    elif (dots[0][1]-dots[3][1])/(dots[0][0]-dots[3][0]) == (dots[1][1]-dots[2][1])/(dots[1][0]-dots[2][0]):
        return 1
    else:
        return 0

# a-b, a-c, a-d, b-c, b-d, c-d로 잘못접근함

# def solution(dots):
#     answer = 0
#     arr=[]
#     for i in range(0,4):
#         for j in range(i+1,4):
#             # 두 직선이 일치하는 경우 1 return
#             if dots[i][1] == dots[j][1] and dots[i][0] == dots[j][0]:
#                 answer = 1
#                 m = 0
#             else:
#                 # 두 점의 기울기 구하기
#                 m = (dots[i][1]-dots[j][1])/(dots[i][0]-dots[j][0])
#             arr.append(m)
#     # 기울기가 같으면 1 return
#     for i in range(0, 6):
#         for j in range(i + 1, 6):
#             if arr[i] == arr[j]:
#                 answer = 1
#     return answer



