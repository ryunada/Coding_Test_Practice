def solution(quiz):
    answer = []
    for i in quiz:
        n = i.split(" ")
        if n[1] == "+":
            if int(n[0])+int(n[2]) == int(n[4]):
                answer.append("O")
            else:
                answer.append("X")
        elif n[1] == "-":
            if int(n[0])-int(n[2]) == int(n[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer

print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))

# quiz=["3 - 4 = -3"]
# for i in quiz:
#     a = i.split(" ")
#     print(a)