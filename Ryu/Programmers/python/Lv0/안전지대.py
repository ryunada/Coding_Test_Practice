# # 미해결
# # 0,0 배열 크기가 에러 남
# def solution(board):
#     answer = 0
#     if len(board) == 0 :
#
#     for i in range(0,len(board)):
#         for j in range(0, len(board)):
#             if (i == 0 & j == 0):
#                 if (board[i][j] % 10) == 1:
#                     board[i][j + 1] += 10
#                     board[i + 1][j] += 10
#                     board[i + 1][j + 1] += 10
#             elif(i==0 & j == len(board)):
#                 if (board[i][j] % 10) == 1:
#                     board[i][j - 1] += 10
#                     board[i + 1][j - 1] += 10
#                     board[i + 1][j] += 10
#             elif(j==0 & i==len(board)):
#                 if (board[i][j] % 10) == 1:
#                     board[i - 1][j] += 10
#                     board[i - 1][j + 1] += 10
#                     board[i][j + 1] += 10
#             elif(i==0):
#                 if (board[i][j] % 10) == 1:
#                     board[i][j - 1] += 10
#                     board[i][j + 1] += 10
#                     board[i + 1][j - 1] += 10
#                     board[i + 1][j] += 10
#                     board[i + 1][j + 1] += 10
#             elif(j==0):
#                 if (board[i][j] % 10) == 1:
#                     board[i - 1][j] += 10
#                     board[i - 1][j + 1] += 10
#                     board[i][j + 1] += 10
#                     board[i + 1][j] += 10
#                     board[i + 1][j + 1] += 10
#             else:
#                 if (board[i][j] % 10) == 1:
#                     board[i - 1][j - 1] += 10
#                     board[i - 1][j] += 10
#                     board[i - 1][j + 1] += 10
#                     board[i][j - 1] += 10
#                     board[i][j + 1] += 10
#                     board[i + 1][j - 1] += 10
#                     board[i + 1][j] += 10
#                     board[i + 1][j + 1] += 10
#
#
#     for i in range(0,len(board)):
#         for j in range(0, len(board)):
#             if board[i][j] == 0:
#                 answer += 1
#     return answer
#
# board1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
# board2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
# board3 = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
# board4 = [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]]
# board5 = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
# board6 = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
# board7 = [[0,0,0],[1,0,0],[0,0,0]]
# board8 = [[1,0,0],[0,0,0],[0,0,0]]
#
# # print(solution(board1)) # 16
# # print(solution(board2)) # 13
# print(solution(board3)) # 0
# # print(solution(board4)) # 16
# # print(solution(board5)) # 8
# # print(solution(board6)) # 15
# # print(solution(board7)) #
# # print(solution(board8)) #
