def solution(id_pw, db):
    a=0
    for i in db:
        if id_pw[0]==i[0] and id_pw[1]==i[1]:
            a+=1
            return "login"
        elif id_pw[0]==i[0] and id_pw[1]!=i[1]:
            a+=1
            return "wrong pw"
    if a==0:
        return "fail"

print(solution(["programmer01", "15789"],[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))