# ex 1)
# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2

# ex 2)
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

def solution(id_list, report, k):
    report = set(report)
    report = list(report)

    id_list_dict = {}
    for i in id_list:
        id_list_dict[i] = 0
    print(id_list_dict)
    for i in range(len(report)):
        id_list_dict[report[i].split()[1]] += 1
    return id_list_dict
