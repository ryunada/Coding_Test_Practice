name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],
        ["may", "kein", "brin", "deny"],
        ["kon", "kain", "may", "coni"]]
# [19, 15, 6]

print(yearning[name.index('may')])

answer = []
for i in photo:
    result = 0
    for j in i:
        if j in name:
            result += int(yearning[name.index(j)])
    answer.append(result)
print(result)
