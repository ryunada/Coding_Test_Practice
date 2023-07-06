def solution(l,r):
    result = []
    for i in range(l,r+1):
        new = str(i).replace("5"," ").replace("0"," ")
        new = new.replace(" ","")
        print(i,new)
        if new == "":
            result.append(i)
    if result == []:
        result.append(-1)
    return result
print(solution(10,55))