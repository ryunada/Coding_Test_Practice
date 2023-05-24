def sol(arr,i,j): #위험지역을 표시하기 위한 함수
    try:
        arr[i-1][j-1] +=2
    except:
        pass
    try:
        arr[i-1][j] +=2
    except:
        pass
    try:
        arr[i-1][j+1] +=2
    except:
        pass
    try:
        arr[i][j-1] +=2
    except:
        pass
    try:
        arr[i][j+1] +=2
    except:
        pass
    try:
        arr[i+1][j-1] +=2
    except:
        pass
    try:
        arr[i+1][j] +=2
    except:
        pass
    try:
        arr[i+1][j+1] +=2
    except:
        pass

def solution(board):
    #배열추가 (-1인덱스 처리하기 위함)
    arr = []
    for i in board:
        i.insert(0, 2)
    for i in range(len(board)+1):
        arr.append(2)
    board.insert(0, arr)

    answer=0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]%2==1: #지뢰
                sol(board,i,j)  #위험지역 표시
    for k in board: #안전지역 칸수 세기
        answer += k.count(0)
    return answer

print(solution([[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))