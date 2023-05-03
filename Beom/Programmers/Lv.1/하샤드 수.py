def solution(x):
    n=0
    for i in range(len(str(x))):
        n+=int(str(x)[i])
    if x%n==0:
        return True
    else:
        return False

print(solution(10))