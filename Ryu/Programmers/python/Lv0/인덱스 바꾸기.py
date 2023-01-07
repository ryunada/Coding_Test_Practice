def solution(my_string, num1, num2):
    my_string = list(my_string)

    temp = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = temp

    return ''.join(my_string)

my_string = "hello"
num1 = 1
num2 = 2

my_string = list(my_string)

print(my_string[1])
temp = my_string[num1]
my_string[num1] = my_string[num2]
my_string[num2] = temp

print(my_string)