def solution(emergency):
    answer = [1 for i in range(len(emergency))] # 크기가 emergency길이인 배열 생성 1을 집어 넣음(등수는 1부터 시작하므로)

    # 배열의 첫번째 값부터 비교
    for i in range(len(emergency)):
       for j in range(len(emergency)):
           if emergency[i] < emergency[j]: # 자기 보다 크면 +1
               answer[i] += 1
    return answer

emergency = [3,76, 24]
print(solution(emergency))
