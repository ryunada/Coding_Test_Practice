my_string = 'hello'
num1, num2 = 1, 2

string = []

for i in my_string:
    string.append(i)
string[num1], string[num2] = string[num2], string[num1]

answer = ''
for i in string:
    answer += i

print(answer)