# 1. id_list에게 메일을 보내는 횟수를 나타낼 리스트를 만들자 => answer
# 2. 신고 횟수를 누적하는 방을 딕셔너리를 만들자 => report_all
# 3. report에 중복되는 값을 제거하자 => set(report)
# 4. 중복되지 않는 report를 split하고 1번 인데스의 값을 신고 횟수 누적하는 딕셔너리에 누적하자.
# 5. 딕셔너리에 누적된 값이 k보다 크거나 같으면 
# 6. report를 split한 0번째 인덱스의 값이 id_list에 해당하는 리스트의 인덱스에 메일을 보내는 횟수의 리스트(answer)에 1을 더해라

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_all = {i : 0 for i in id_list}
    
    for i in set(report):
        report_all[i.split(' ')[1]] += 1
        
    for i in set(report):
        if report_all[i.split(' ')[1]] >= k :
            answer[id_list.index(i.split(' ')[0])] += 1
    
    return answer



# 최초 코드(흐름대로 따라가봄) = 예시 테스트는 2개 모두 통과 / but 제출시 시간초과 + 틀림
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    count= [0]*len(id_list)
    lst = [] 
    kkk = []
    for i in range(len(report)) :
        a = report[i].split(' ')
        if a not in lst :   # 동일한 유저ID와 유저가 신고한 ID가 동일하면 삭제
            lst.append(a)
    
    for i in range(len(lst)):   # 신고당한 횟수를 계산
        for v in range(len(id_list)) :
            if lst[i][1] == id_list[v] :
                count[v] += 1
            else :
                pass
    
    for a,b in zip(count,id_list):
        if a >=2 :
            kkk.append(b)
    
    for i in range(len(lst)):
        if lst[i][1] in kkk :
            idx = id_list.index(lst[i][0])
            answer[idx] += 1
    return answer
