# https://school.programmers.co.kr/learn/courses/30/lessons/120862
# 최댓값 만들기 (2)

def solution(numbers):
    answer = -999999999

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] > answer:
                answer = numbers[i] * numbers[j]

    return answer