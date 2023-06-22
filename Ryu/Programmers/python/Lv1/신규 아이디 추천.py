# ex1
new_id ="...!@BaT#*..y.abcdefghijklm"
print(f"입력한 ID : {new_id}")

# 조건 1. 소문자로 치환
one_id = new_id.lower()

two_id = ''
# 조건 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
for i in one_id:
    if (i.isalnum() == True)| (i == '-') | (i == '_') | (i == '.'):
        two_id += i
print(two_id)


# 조건 3. 마침표가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
three_id = ''
two_id_l = list(two_id)

for i in range(1,len(two_id_l)):
    if (two_id_l[i-1] == '.') & (two_id_l[i] == '.'):
        continue
    three_id += two_id_l[i - 1]
# 마지막..?
# if three_id[-1] != '.':

print(three_id)




