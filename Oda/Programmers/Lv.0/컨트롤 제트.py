s = "1 2 Z 3"
result = 0

s = s.split()
print(s)
a = []
for i in s:
    a.append(i)
    if i == 'Z':
        a.pop()
        a.pop()

print(a)
sum=0

for j in a:
    sum += int(j)
print(sum)

#########
def sol(s):
    answer = 0
    s = s.split()
    a = []
    for i in s:
        a.append(i)
        if i == 'Z':
            a.pop()
            a.pop()

    for j in a:
        answer += int(j)

    return answer