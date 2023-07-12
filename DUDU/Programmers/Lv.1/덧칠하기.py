# 1.  section에서 처음 덧칠 할 구간에서부터 m만큼 덧칠을 한다. 그리고 answer에 1을 더해준다
# 2. 두번째 인덱스의 해당 값이 1번째에서 덧칠이 되었는지 되지 않았는지 if문을 통해 확인한다.
# 3. 다음과 같은 작업을 반복한다.

def solution(n, m, section):
    answer = 0
    paint = 0   # 현재까지 페인팅이 된 번호 
    for i in section :
        if i > paint :   
            paint = i + m -1  
            answer += 1
    return answer

