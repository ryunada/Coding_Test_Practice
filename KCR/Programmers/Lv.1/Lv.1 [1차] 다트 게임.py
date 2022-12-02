def solution(dartResult) :
    dartResult = dartResult.replace('*', '*2 ')
    dartResult = dartResult.replace('#', '*(-1) ')
    for i in
    # for n, i in enumerate(dartResult) :
    #     if 'D' in i :
    #         dartResult[n] = int(i[:-1])**2
    #     elif 'S' in i :
    #         dartResult[n] = int(i[:-1])
    #     elif 'T' in i :
    #         dartResult[n] = int(i[:-1])**3
    return dartResult
dartResult = '1S2D*3T' # 37
# dartResult = '1D2S#10S' # 9
# dartResult = '1D2S0T' # 3
# dartResult = '1S*2T*3S' # 23
# dartResult = '1D#2S*3S' # 5
# dartResult = '1T2D3D#' # -4
# dartResult = '1D2S3T*' # 59

# 1D2**1+3T*
# 1**2+2**1+3T*
# 1**2+2**1+3**3*
# 1**2+2**1+3**3*
# 1**2+2**1+3**

print(solution(dartResult))