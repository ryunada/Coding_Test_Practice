# def solution(rsp):
#     answer = []
#     for i in rsp:
#         if i == '2':
#             answer.append('0')
#         elif i == '0':
#             answer.append('5')
#         elif i == '2':
#             answer.append('2')
#     return answer

def solution(rsp):
    dic = {'0':'5', '2':'0', '5':'2'}
    return ''.join(dic[i] for i in rsp)