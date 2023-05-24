def solution(code):
    ret = ''
    mode = 0
    for i in range(len(code)) :
        if mode == 0 :
            if code[i] != "1":
                if i % 2 == 0 :
                    ret += code[i]
            else : 
                mode = 1 
        else : 
            if code[i] != "1":
                if i % 2 == 1 :
                    ret += code[i]
            else : 
                mode = 0
    if ret == "":
        return "EMPTY"
    else :            
        return ret
      
# <문제접근법>

1. "ret"이라는 변수와 mode = 0 이라는 변수를 생성했다. => mode =0 인 인유는 처음 mode는 0이라고 했기 때문에

2. 조건문을 활용하여 code의 길이만큼 code의 인덱스를 사용하여 새로운 조건문을 이용해 mode = 0와 아닐 때를 구분해준다.

3. mode = 0일 때 code[i]가 문자열 "1"이 아니라면 인덱스의 짝수에 해당되는 값을 ret에 저장

4. code[i] = "1"이라면 mode = 1로 저장

5. mode = 0이 아닐 때를 생각해보자.

6. code[i]가 문자열 "1"이 아니라면 인덱스의 홀수에 해당되는 값을 ret에 저장

7. code[i] = "1"이라면 mode = 0로 저장

8. (위 과정을 len(code)만큼 반복)

9. 만약 ret이 빈 문자열이라면 'EMPTY' 출력 / 아니라면 ret을 출력
