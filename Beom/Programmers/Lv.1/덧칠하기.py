def solution(n, m, section):
    num=0
    while len(section) >0:
        num+=1
        for i in range(section[0],section[0]+m):
            if i in section:
                section.remove(i)
    return num

# def solution(n, m, section):
#     num=0
#     while max(section) >= section[0]+m:
#         section.append(section[0]+m)
#         section.sort()
#         num+=section.index(section[0]+m)
#         section = section[section.index(section[0]+m):]
#     return num