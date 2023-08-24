# ex 1)
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2


# ex 2)
# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3
def solution(id_list, report, k):
    report = set(report)
    report = list(report)

    # 딕셔너리 초기화
    Name_dict = {} # 유저 ID당 신고를 한 사람 딕셔너리
    N_dict = {}    # 신고를 받은 수를 담는 딕셔너리
    for i in id_list:
        Name_dict[i] = 0
        N_dict[i] = 0
    print(f"유저 -> 신고한 사람 : {Name_dict}")
    print(f"유저 -> 신고 당한 수 : {N_dict}")
    print("---------------------------------------------------------------------------------------")

    for i in range(len(report)):
        N_dict[report[i].split()[1]] += 1                            # 유저ID -> 신고를 당한 수
    print(f"유저 -> 신고 당한 수 : {N_dict}")

    # k번 이상이면 메일 발송
    for i in N_dict:
        if N_dict[i] >= k:
            N_dict[i] = 1
        else:
            N_dict[i] = 0
    print(f"유저 -> 신고 당한 수 : {N_dict}")

    print(f"유저 -> 신고한 사람 : {Name_dict}")
    for i in range(len(report)):
        if N_dict[report[i].split()[1]] == 1:
            Name_dict[report[i].split()[0]] += 1 # 유저ID -> 신고를 당한 사람
    return list(Name_dict.values())

print( solution(id_list, report, k))
