# def solution(money):
#     answer = [int(money/5500),money - (int(money/5500)*5500)]
#     return answer

def solution(money):
    return [money//5500, money%5500]