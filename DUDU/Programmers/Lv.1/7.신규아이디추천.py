def solution(new_id):
    answer = '' 
    new_id = new_id.lower() # 1단계
    for word in new_id:     # 2단계
        if word.isalnum() or word in '-_.':
            answer += word

    while '..' in answer:   # 3단계
        answer = answer.replace('..', '.') # 단계적으로 계속 줄임(.을 만족할 때까지)

    if answer[0] == '.' and len(answer) > 1 :  # 4단계
        answer = answer[1:]
    else : 
        answer
    
    if  answer[-1] == '.' : 
        answer = answer[:-1]
    else :
        answer
    
    if answer == '' :  # 5단계
        answer = 'a'
    else : 
        answer 

    if len(answer) >= 16:    # 6단계 
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 2:     # 7단계
        answer = answer + answer[-1] * (3-len(answer)) # 3개를 만들어주기 위해서
    return answer
