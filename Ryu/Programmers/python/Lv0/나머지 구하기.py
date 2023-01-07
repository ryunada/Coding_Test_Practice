def solution1(num1, num2):
    answer = num1 % num2
    return answer

def solution2(num1, num2):
    return divmod(num1, num2)   # divmod(x, y) : 두 숫자를 인자로 전달 받아 첫번째 인자를 두번째 인자로 나눈 몫과 나머지를 tuple 형식으로 반환

num1 = int(input("num1을 입력하세요 : "))
num2 = int(input("num2를 입력하세요 : "))
print(solution1(num1,num2))
print(solution2(num1,num2))
