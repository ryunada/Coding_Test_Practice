def solution(num_list):
    odd = 0
    even = 0
    for i in num_list:
        if i % 2 == 0:
            even += 1
        if i % 2 != 0:
            odd += 1
    answer = [even,odd]
    return answer