# ex1
# new_id ="...!@BaT#*..y.abcdefghijklm.."
new_id = ''
# new_id = 'z-+.^.'

print(f"입력한 ID : {new_id}")
def solution(new_id):
    # 조건 1. 소문자로 치환
    one_id = new_id.lower()

    # 조건 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    two_id = ''
    for i in one_id:
        if (i.isalnum() == True) | (i == '-') | (i == '_') | (i == '.'):
            two_id += i

    # 조건 3. 마침표가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    three_id = ''
    two_id_l = list(two_id)

    for i in range(1, len(two_id_l)):
        if (two_id_l[i - 1] == '.') & (two_id_l[i] == '.'):
            continue
        three_id += two_id_l[i - 1]


    # 조건 4. 앞에 뒤에 마침표(.)이면 제거 | 조건 3에서 뒤에 마침표가 있으면 없앰
    four_id = ''
    if three_id[0] == '.':
        four_id = three_id[1:]

    # 조건 5. new_id가 빈 문자열이라면, new_id에 'a'를 대입
    if len(four_id) == 0:
        four_id = 'a'

    # 조건 6.
    if len(four_id) >= 16:
        five_id = four_id[:15]
        if five_id[-1] == '.':
            five_id = five_id[:-1]

    # 조건 7.
    result_id = five_id
    if len(five_id) <= 2:
        while (len(result_id) >= 3):
            result_id += five_id[-1]

    return result_id

print(solution(new_id))
