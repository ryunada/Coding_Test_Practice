lottos = [1, 2, 3, 4, 5, 6]
win_nums = [7, 8, 9, 10, 11, 12]


# Version 1
# def solution(lottos, win_nums):
#     zero = 0
#     T = 0
#     for i in lottos:
#         if i in win_nums: # Lotto번호 중 일치하는 번호
#             T += 1
#         if i == 0:        # 모르는 번호
#             zero += 1
#     result = [T+zero, T]
#     answer = []
#     for i in result:
#         if i >= 6:
#             answer.append(1)
#         elif i == 5:
#             answer.append(2)
#         elif i == 4:
#             answer.append(3)
#         elif i == 3:
#             answer.append(4)
#         elif i == 2:
#             answer.append(5)
#         else:
#             answer.append(6)
#     return answer



def solution(lottos, win_nums):
    zero = 0
    T = 0
    for i in lottos:
        if i in win_nums:  # Lotto번호 중 일치하는 번호
            T += 1
        # or zero = lotto.count(0)
        if i == 0:  # 모르는 번호
            zero += 1
    MinLotto = T + zero
    MaxLotto = T

    if MinLotto > 6:
        MinLotto = 6
    elif MinLotto == 0:
        MinLotto = 1

    if MaxLotto <= 1:
        MaxLotto = 1

    return [7 - MinLotto, 7 - MaxLotto]

print(solution(lottos, win_nums))

