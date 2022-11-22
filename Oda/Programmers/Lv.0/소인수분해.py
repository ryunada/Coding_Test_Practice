n = 12	# [2, 3]
# 소수 인 경우에 n을 그래도 반환
# 소수가 아닌 경우 소인수분해
# 소인수들은 약수

so = []
for i in range(2, n+1):
    if n % i == 0:
      so.append(i)
print(so)

for i in so:
    for j in range(2, 5000):
        if i * j in so:
            so.remove(i*j)
            print(so)
print(so)