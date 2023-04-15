def solution(numer1, denom1, numer2, denom2):
    if denom1 == denom2:
        denom3 = denom1
        numer3 = numer1 + numer2
    else:
        denom3 = denom1 * denom2
        numer3 = numer1 * denom2 + numer2 * denom1

    # 최대공약수 찾기
    for i in range(1, min(denom3, numer3) + 1):
        if (numer3 % i == 0) and (denom3 % i == 0):
            k = i

    return [numer3//k, denom3//k]



