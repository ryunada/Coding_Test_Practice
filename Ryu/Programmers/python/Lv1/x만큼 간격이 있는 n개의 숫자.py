x = 2
n = 5
l = list()
k = 0
for i in range(n):
    k += x
    l.append(k)

print(l)

# lambda
def number_generator(x,n):
    return [i * x + x for i in range(n)]

print(number_generator(2,5))