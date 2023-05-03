string = '3 - 4 = -3'

s_s = string.split(' ')
print(s_s[1] == '-')
def solution(string):
    answer = []
    s_s = string.split(' ')
    a = s_s[0]
    b = s_s[2]
    if str(s_s[1]) == '-':
        return (a-b) == int(s_s[-1])
        # return 'O'
print(solution(string))




