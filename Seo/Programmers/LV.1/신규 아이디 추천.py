def recommend(id):
    # 1단계
    id = id.lower()
    # 2단계
    List = list(id)
    for i in range(0, len(List)):
        if (List[i].isalpha() == False) & (List[i].isdigit() == False) & (List[i] not in ['-', '_', '.']):
            List[i] = ""
    # 문자열로 변환
    id = ""
    for i in List:
        id = id + i

    # 3단계
    List = list(id)
    for i in range(0, len(List) - 1):
        if (List[i] == ".") & (List[i] == List[i + 1]):
            List[i] = ""
    # 문자열로 변환
    id = ""
    for i in List:
        id = id + i

    # 4단계
    List = list(id)
    if (List[0] == "."):
        List[0] = ""
    if (List[len(List) - 1] == "."):
        List[len(List) - 1] = ""
    # 문자열로 변환
    id = ""
    for i in List:
        id = id + i

    # 5단계
    if id == "":
        id += "a"

    # 6단계
    List = list(id)
    if len(List) >= 16:
        for i in range(15,len(List)):
            List[i] = ""
        if (List[14] == "."):
            List[14] = ""
    # 문자열로 변환
    id = ""
    for i in List:
        id = id + i

    # 7단계
    List = list(id)
    if len(List) <= 2:
        var = List[len(List) - 1]
        while len(List) < 3:
            List.append(var)
    # 문자열로 변환
    id = ""
    for i in List:
        id = id + i

    return id


def solution(id):
    n = 0
    # 아이디 길이 검사
    if (len(id) >= 3) & (len(id) <= 15):
        n += 1
    # 아이디 구성 문자 검사
    length = 0
    for i in range(0, len(id)):
        if id[i].islower() == True:
            length += 1
        elif id[i].isdigit() == True:
            length += 1
        elif id[i] == "-":
            length += 1
        elif id[i] == "_":
            length += 1
        elif id[i] == ".":
            length += 1
    if length == len(id):
        n += 1
    # 추가 조건 검사
    if (id[0] == ".") | (id[len(id)-1] == "."):
        n -= 1
    for i in range(0, len(id)-1):
        if (id[i] == ".") & (id[i] == id[i+1]):
            n -= 1
    # 규칙에 부합하는지 판단
    if n==2:
        return id
    else:
        return recommend(id)

print(solution("abcdefghijklmn.p"))

