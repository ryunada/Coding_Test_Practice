def solution(p):
    answer = ''
    p1 = p
    v = []
    score = 0
    while ('()' in p1):
        p1 = p1.replace('()', '')
    if len(p1) == 0:
        return p
    else:
        p_lst = list(p)
        for idx, value in enumerate(p):
            if value == '(':
                score += 1
            else:
                score -= 1
            if score < 0:
                v.append(idx)
            elif (score == 0) & (value == '('):
                v.append(idx)
        for i in v:
            if p_lst[i] == '(':
                p_lst[i] = ')'
            elif p_lst[i] == ')':
                p_lst[i] = '('
        return ''.join(p_lst)
