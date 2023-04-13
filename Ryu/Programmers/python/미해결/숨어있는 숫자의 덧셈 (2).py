my_string = "aAb1B2cC34oOp"
result = 0
num = list()
for i in my_string:
    if i.isdigit() == 0:
        print(num)
        # result += int(num)
        num = list()
        continue
    num.append(int(i))
# print(num)

