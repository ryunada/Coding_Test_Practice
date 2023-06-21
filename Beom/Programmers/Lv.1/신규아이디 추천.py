def solution(new_id):
    new_id = new_id.lower() # 1단계

    # for i in range(len(new_id)): #1단계
    #     if new_id[i].isalpha():
    #         if new_id[i].isupper():
    #             new_id = new_id.lower()
    #             break

    new_id2='' #2번
    for i in range(len(new_id)):
       if (new_id[i].isdigit()) | (new_id[i].isalpha()) | (new_id[i] in ['-','_','.']):
           new_id2+=new_id[i]
    new_id = new_id2

    b = []
    for i in range(len(new_id)):  # 3단계
        if new_id[i] == '.':
            b.append(i)

    # return b
    # [0, 1, 2, 6, 7, 9]
    #['.', '.', '.', 'b', 'a', 't', '.', '.', 'y', '.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    new_id_list = list(new_id)
    # return new_id_list
    for i in range(len(b)-1,0,-1):
        if b[i] - b[i-1] == 1:
            del new_id_list[b[i]]

    new_id=''
    for i in new_id_list:
        new_id+=i

    if new_id[0] == '.':  # 4단계
        if len(new_id)==1:
            new_id='a' # 5단계
        else:
            new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    if len(new_id) >= 16:  # 6단계
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 2:  # 7단계
        for i in range(3):
            new_id += new_id[-1]
            if len(new_id) == 3:
                break

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
