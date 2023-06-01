# # 미해결
# # 0,0 배열 크기가 에러 남
# def solution(board):
#     answer = 0
#     if len(board) == 1 :
#         if board[0] == 1:
#             return 1
#         else:
#             return 0
#     else:
#         for i in range(0,len(board)):
#             for j in range(0, len(board)):
#                 try:
#                     if (board[i][j] % 10) == 1:
#                         board[i - 1][j - 1] += 10
#                         board[i - 1][j] += 10
#                         board[i - 1][j + 1] += 10
#                         board[i][j - 1] += 10
#                         board[i][j] += 10
#                         board[i][j + 1] += 10
#                         board[i + 1][j - 1] += 10
#                         board[i + 1][j] += 10
#                         board[i + 1][j + 1] += 10
#                 except:
#                     pass
#         # for i in range(1,len(board)):
#         #     for j in range(1, len(board)):
#         #         try:
#         #             if (i == 0 & j == 0):
#         #                 if (board[i][j] % 10) == 1:
#         #                     board[i][j + 1] += 10
#         #                     board[i + 1][j] += 10
#         #                     board[i + 1][j + 1] += 10
#         #             elif(i==0 & j == len(board)):
#         #                 if (board[i][j] % 10) == 1:
#         #                     board[i][j - 1] += 10
#         #                     board[i + 1][j - 1] += 10
#         #                     board[i + 1][j] += 10
#         #             elif(j==0 & i==len(board)):
#         #                 if (board[i][j] % 10) == 1:
#         #                     board[i - 1][j] += 10
#         #                     board[i - 1][j + 1] += 10
#         #                     board[i][j + 1] += 10
#         #             elif(i==0):
#         #                 if (board[i][j] % 10) == 1:
#         #                     board[i][j - 1] += 10
#         #                     board[i][j + 1] += 10
#         #                     board[i + 1][j - 1] += 10
#         #                     board[i + 1][j] += 10
#         #                     board[i + 1][j + 1] += 10
#         #             elif(j==0):
#         #                 if (board[i][j] % 10) == 1:
#         #                     board[i - 1][j] += 10
#         #                     board[i - 1][j + 1] += 10
#         #                     board[i][j + 1] += 10
#         #                     board[i + 1][j] += 10
#         #                     board[i + 1][j + 1] += 10
#         #             else:
#         #                 if (board[i][j] % 10) == 1:
#         #                     board[i - 1][j - 1] += 10
#         #                     board[i - 1][j] += 10
#         #                     board[i - 1][j + 1] += 10
#         #                     board[i][j - 1] += 10
#         #                     board[i][j + 1] += 10
#         #                     board[i + 1][j - 1] += 10
#         #                     board[i + 1][j] += 10
#         #                     board[i + 1][j + 1] += 10
#         #         except:
#         #             pass
#
#     for i in range(0,len(board)):
#         for j in range(0, len(board)):
#             if board[i][j] == 0:
#                 answer += 1
#     return answer


# board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
# board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
# board = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
# board = [[0,0,0],[0,0,0],[0,0,1]]
# board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# board = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
# board = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# board = [[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]]
# board = [1]
# board = [[0,0],[0,0]]
board = [[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]]
def solution(board):
    test = [[0] * len(board) for i in range(len(board))]
    answer = 0
    if len(board) == 1:   # 배열이 1*1인 경우
        if board[0] == 1: # 1배열에 폭탄이 있으면 안전 지대는 0
            return 0
        else:             # 배열에 폭탄이 없으면 안전지대는 1
            return 1
    elif len(board) == 2: # 배열이 2*2인 경우
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    return 0
        return 4
    else:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    if (i == 0) & (j == 0): # 왼쪽 위 모서리
                        test[i][j] += 1
                        test[i][j+1] += 1
                        test[i+1][j+1] += 1
                        test[i+1][j] += 1
                    if (i == 0) & (0 < j < len(board)-1): # 모퉁이 제외 위쪽 벽면
                        test[i][j] += 1
                        test[i][j-1] += 1
                        test[i+1][j-1] += 1
                        test[i+1][j] += 1
                        test[i+1][j+1] += 1
                        test[i][j+1] += 1
                    if (i == 0) & (j == len(board)-1): # 오른쪽 위 모퉁이
                        test[i][j] += 1
                        test[i][j-1] += 1
                        test[i+1][j-1] += 1
                        test[i+1][j] += 1
                    if (0 < i < len(board)-1) & (j == 0): # 모퉁이 제외 왼쪽 벽면
                        test[i][j] += 1
                        test[i-1][j] += 1
                        test[i-1][j+1] += 1
                        test[i][j+1] += 1
                        test[i+1][j] += 1
                        test[i+1][j+1] += 1
                    if (0 < i < len(board)-1) & (j == len(board)-1): # 모퉁이 제외 오른쪽 벽면
                        test[i][j] += 1
                        test[i-1][j-1] += 1
                        test[i-1][j] += 1
                        test[i][j-1] += 1
                        test[i+1][j-1] += 1
                        test[i+1][j] += 1
                    if (i == len(board)-1) & (j == 0): # 왼쪽 아래 모퉁이
                        test[i][j] += 1
                        test[i-1][j] += 1
                        test[i-1][j+1] += 1
                        test[i][j+1] += 1
                    if (i == len(board)-1) & (0 < j < len(board)-1): # 모퉁이 제외 아래 벽면
                        test[i][j] += 1
                        test[i-1][j-1] += 1
                        test[i-1][j] +=1
                        test[i-1][j+1] += 1
                        test[i][j-1] += 1
                        test[i][j+1] += 1
                    if (i == len(board)-1) & (j == len(board)-1): # 오른쪽 아래 모퉁이
                        test[i][j] += 1
                        test[i-1][j-1] += 1
                        test[i-1][j] += 1
                        test[i][j-1] += 1
                    if (0 < i < len(board)-1) & (0 < j < len(board)-1): # 제외 없음
                        test[i][j] += 1
                        test[i-1][j-1] += 1
                        test[i-1][j] += 1
                        test[i-1][j+1] += 1
                        test[i][j-1] += 1
                        test[i][j+1] += 1
                        test[i+1][j-1] += 1
                        test[i+1][j] += 1
                        test[i+1][j+1] += 1

    for i in range(0,len(board)):
        for j in range(0, len(board)):
            if test[i][j] == 0:
                answer += 1
    return answer

print(solution(board))

