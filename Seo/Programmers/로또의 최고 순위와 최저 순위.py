def solution(lottos, win_nums):
    n = 0
    zero = 0
    answer = []
    for i in range(0,6):
        if lottos[i] in win_nums:  # 몇 개의 번호가 일치하는가
            n += 1
        if lottos[i] == 0:         # 알아볼 수 없는 숫자가 몇 개인가
            zero += 1
    max = n + zero # 최고 순위 번호 일치 개수
    min = n # 최저 순위 번호 일치 개수
    for i in [max,min]:
        num = i
        # 순위 결정
        if num == 6:
            rank = 1
        elif num == 5:
            rank = 2
        elif num == 4:
            rank = 3
        elif num == 3:
            rank = 4
        elif num == 2:
            rank = 5
        else:
            rank = 6
        answer.append(rank)
    return answer

print(solution([44,1,0,0,31,25],[31,10,45,1,6,19]))

