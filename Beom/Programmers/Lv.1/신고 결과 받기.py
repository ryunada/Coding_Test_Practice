def solution(id_list, report, k):
    score = [0] * len(id_list)  # 신고받은 횟수
    report = list(set(report))  # 중복제거

    # 신고 받은 횟수 구하기
    for i in report:
        score[id_list.index(i.split(' ')[1])] += 1

    bad_people = []  # 정지 받을 사람 명단

    # 신고받은 횟수가 k보다 크다면 정지받을 명단에 추가.
    for idx, num in enumerate(score):
        if num >= k:
            bad_people.append(id_list[idx])
            
    result = [0] * len(id_list)
    # 신고받은 사람이 정지받을 사람 명단에 있다면
    # 신고한 사람에게 메일 발송
    for value in report:
        if value.split(' ')[1] in bad_people:
            result[id_list.index(value.split(' ')[0])] += 1

    return result