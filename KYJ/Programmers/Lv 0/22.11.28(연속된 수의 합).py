# 연속된 num개의 정수의 합이 total이 된다.
# num과 total을 입력받아 연속된 정수렬을 출력하시오

def solution(num, total):
    sum = 0
    for i in range(num):
        sum += i
#   가장 작은수 = a 일때
#   total = num * a + sum
#   a = (total-sum) / num
    answer = list()
    a = (total-sum)/num
    for j in range(num):
        answer.append(int(a+j))

    return answer


print(solution(3,12))
print(solution(5,15))
print(solution(4,14))
print(solution(5,5))