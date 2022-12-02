# 두 수의 같은자리에 같은숫자가 있을때 이를 모아 만든 가장큰 정수 -> 짝꿍
# 짝꿍이 없으면 -1,
# X,Y는 문자열로 시작


def solution(X,Y):
    x = {}
    for i in range(len(X)):
        a = len(X) - i - 1
        x[i] = X[a]
    y = {}
    for i in range(len(Y)):
        a = len(Y) - i - 1
        y[i] = Y[a]

    n = {}
    for i in range(min(len(X), len(Y))):
        n[x[i]] = 0

    for i in range(min(len(X), len(Y))):
        if x[i] == y[i]:
            n[x[i]] += 1
        else:
            pass

    answer = ''
    for i in range(10):
        if str(10 - i) in n:
            for j in range(n[str(10-i)]):
                answer += str(10-i)
        else:
            pass

    if answer == '':
        answer = '-1'
    else:
        pass

    return answer

print(solution('12321','42531'))
print(solution('1521167855','157555'))
print(solution('123456','12345'))


# ps. 굳이 자릿수가 같을 필요는 없던거 같다... 뻘짓했넹