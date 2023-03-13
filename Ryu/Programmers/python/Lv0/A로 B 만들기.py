before = "olleh"
after = "hello"

a = list(before)
b = list(after)
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i] == b[j]:
#             print(a[i])
#             a.remove(a[i])
#             break
#     print(f"{i}번째 {a}")
print(a)
del a[3]
print(a)

k = 0
for i in range(len(a)):
    # print(i)
    for j in range(len(b)):
        print(f"i: {i} |j : {j}")
        if a[i] == b[j]:
            print(a)
            del a[i]
            k += 1
            break

# if k == len(a):
#     return 1
# else:
#     return 0

