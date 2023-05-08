n = 10
l = list()
for i in range(1,n):
    if (n % i) == 1:
        l.append(i)
print(min(l))

