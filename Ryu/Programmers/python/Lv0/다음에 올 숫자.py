# 등차수열 a[n] = a[n-1] + r
# 등비수열 a[n] = a[n-1] * a


def solution(common):
    for i in range(1, len(common)-1):
        if common[i] == (common[i-1] + common[i + 1]) / 2: # 등차 중앙
            r = common[i] - common[i-1]
            return common[-1] + r
        elif pow(common[i],2) == common[i-1] * common[i + 1]: # 등비 중앙
            a = divmod(common[i], common[i-1])[0]
            return common[-1] * a
        else:
            return "아닌 경우는 없다!"

common = [0, 0, 0, 0]
print(solution(common))

