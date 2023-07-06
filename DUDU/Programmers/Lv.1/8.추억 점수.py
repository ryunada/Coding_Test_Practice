def solution(name, yearning, photo):
    answer = []
    for i in photo :    # photo의 조건문
        sum = 0         # yearning를 저장할 변수
        for v in range(len(i)):  # photo의 인덱스 안에 인덱스
            if i[v] in name :    # photo의 인덱스 안에 인덱스가 name에 포함되어 있을 경우
                name_index = name.index(i[v])  # 그 값의 name의 index값을 저장
                sum += yearning[name_index]    # yearning의 index의 값을 더함
        answer.append(sum)                   
    return answer
