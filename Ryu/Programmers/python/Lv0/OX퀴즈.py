string = '3 - 4 = -3'

s_s = string.split(' ')
print(s_s[1] == '-')


def solution(string):
    result = []
    s_s = string.split(' ')
    if str(s_s[1]) == '-':
        result = (int(s_s[0])-int(s_s[2])) == int(s_s[-1])
        # return 'O'
    elif str(s_s[1]) == '-':
        result = (int(s_s[0]) + int(s_s[2])) == int(s_s[-1])
    print(result)
print(solution(string))
#



