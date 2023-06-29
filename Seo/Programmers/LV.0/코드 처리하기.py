def solution(code):
    mode = 0
    ret = ""
    for idx in range(0, len(code)):
        if mode == 0:
            if code[idx] != "1" and idx % 2 == 0:
                ret += code[idx]
            elif code[idx] == "1":
                mode = 1
        else:
            if code[idx] != "1" and idx % 2 == 1:
                ret += code[idx]
            elif code[idx] == "1":
                mode = 0
        print(idx, code[idx],mode, ret)
    if ret == "":
        ret = "EMPTY"
    return ret

print(solution("abc1abc1abc"))