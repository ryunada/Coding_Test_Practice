# ex1)
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

# ex2)
# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = 'left'

# ex3)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# hand = "right"

def solution(numbers, hand):
    # 키패드 dict
    keypad = {1 : [0, 0], 2 : [0, 1], 3 : [0, 2],
              4 : [1, 0], 5 : [1, 1], 6 : [1, 2],
              7 : [2, 0], 8 : [2, 1], 9 : [2, 2],
              '*' : [3, 0], 0 : [3, 1], '#' : [3, 2]}
    # 결과 str
    result = ""
    # 손 위치
    l_hand = keypad['*']
    r_hand = keypad['#']

    for i in numbers: # 눌러야 할 번호 : i
        if i in [1, 4, 7]: # 왼손가락 고정 번호 : 1, 4, 7
            result += 'L'
            l_hand = keypad[i]
        elif i in [3, 6, 9]: # 오른 손가락 고정 번호 : 3, 6, 9
            result += 'R'
            r_hand = keypad[i]
        else:
            l_hand_l = abs(l_hand[0] - keypad[i][0]) + abs(l_hand[1] - keypad[i][1]) # 왼쪽 손가락과 눌러야할 번호와의 거리
            r_hand_l = abs(r_hand[0] - keypad[i][0]) + abs(r_hand[1] - keypad[i][1]) # 오른쪽 손가락과 눌러야할 번호와의 거리
            if l_hand_l < r_hand_l: # 왼 손가락 위치가 오른쪽 보다 가깝다면 ~
                result += 'L'
                l_hand = keypad[i]
            elif l_hand_l > r_hand_l: # 오른 손가락 위치가 왼쪽 보다 가깝다면 ~
                result += 'R'
                r_hand = keypad[i]
            else: # 같을 경우
                if hand == 'left': # 왼손잡이
                    result += 'L'
                    l_hand = keypad[i]
                else:  # 오른손 잡이
                    result += 'R'
                    r_hand = keypad[i]
    return result


print(solution(numbers, hand))


