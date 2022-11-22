def solution(s):
    try:
        return (type(int(s)) == int) & (len(s) in (4, 6))
    except :
        return False