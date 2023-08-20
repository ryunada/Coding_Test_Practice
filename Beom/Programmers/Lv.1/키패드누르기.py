def solution(numbers, hand):
    # 각 숫자패드에 위치 지정
    location = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        '*': [3, 0],
        0: [3, 1],
        '#': [3, 2],
    }

    answer = ''
    left_hand = '*'
    right_hand = '#'

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left_hand = i
        elif i in [3, 6, 9]:
            answer += 'R'
            right_hand = i
        elif i in [2, 5, 8, 0]:
            left_diff = abs(location[i][0] - location[left_hand][0]) + abs(location[i][1] - location[left_hand][1])
            right_diff = abs(location[i][0] - location[right_hand][0]) + abs(location[i][1] - location[right_hand][1])
            if left_diff < right_diff:
                answer += 'L'
                left_hand = i
            elif left_diff > right_diff:
                answer += 'R'
                right_hand = i
            else:
                if hand == 'right':
                    answer += 'R'
                    right_hand = i
                else:
                    answer += 'L'
                    left_hand = i
    return answer