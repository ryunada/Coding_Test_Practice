s = 'pPoooyY'
def string_p_y(s):
    p = 0
    y = 0
    for i in s:
        if (i == 'p') | (i == 'P'):
            p += 1
        elif (i == 'y') | (i == 'Y'):
            y += 1
    if (p == y):
        return True
    else:
        return False

print(string_p_y(s))