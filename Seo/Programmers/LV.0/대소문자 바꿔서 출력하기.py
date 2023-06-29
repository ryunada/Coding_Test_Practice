str = input()
a=''
for i in range(0, len(str)):
    if str[i].islower() == False:
        a += str[i].lower()
    else:
        a += str[i].upper()
print(a)
