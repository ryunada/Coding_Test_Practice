# 어떤 자연수를 제곱했을때 나오는 정수를 제곱수라고 합니다.
# 정수 n이 매개변수로 주어질때, n이 제곱수라면 1을 아니라면2를 return하도록
# solution 함수를 완성하시오


def solution(n):
    for i in range(0, n):
        answer = 2
        if n != i**2:
            pass
        else:
            answer = 1
            break

    return answer

print(solution(144))
print(solution(976))

print(solution(10000))
print(solution(5))
print(solution(4))
print(solution(1))