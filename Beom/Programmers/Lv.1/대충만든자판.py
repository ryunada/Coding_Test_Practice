def solution(keymap, targets):
    result = []
    for i in targets:
        score = []
        for j in i:
            idx = []
            cnt = 0
            for k in keymap:
                if k.find(j) != -1:
                    idx.append(k.find(j) + 1)
                else:
                    cnt += 1
            if cnt == len(keymap):
                score.append(-1)
            else:
                score.append(min(idx))
        if -1 in score:
            result.append(-1)
        else:
            result.append(sum(score))
    return result



    #             if (len(idx)!=0) & (len(idx) != len(keymap)):
    #                 score.append(min(idx))
    #             else:
    #                 score.append(-1)

    #         if -1 in score:
    #             result.append(-1)
    #         else:
    #             result.append(sum(score))


    #         if j in key_map_str:
    #             for k in keymap:
    #                 click = len(k)-1
    #                 if k.find(j)+1 < click:
    #                     click = (k.find(j)+1)
    #                 score += click
    #         else:
    #             result.append(-1)
    #             break
    #     result.append(score)
    # return result