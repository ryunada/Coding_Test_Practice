def solution(keymap, targets):
    key_map_str = ''
    result = []
    for i in keymap:
        key_map_str += i

    for i in targets:
        score = 0
        for j in i:
            for k in keymap:
                if k.find(j) == -1:
                    pass
                else:
                    click = len(k)
                    if click > k.find(j) + 1:
                        click = k.find(j) + 1
                    score += click
        result.append(score)
    return result


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