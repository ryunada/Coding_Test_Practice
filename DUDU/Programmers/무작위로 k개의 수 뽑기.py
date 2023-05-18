def solution(arr, k):
    answer = []
    for i in range(len(arr)) :
        num = arr[i]
        if num not in arr[:i]:
            answer.append(num)
        
        if len(answer) == k :
            break
            
    while len(answer) < k:
        answer.append(-1)
    return answer
  
  # <원리>
  # arr의 리스트에서 순서대로,중복을 제외하여 k개의 개수만큼 result의 개수가 결정이 된다.
  # 만약 arr의 중복을 하지 않은 개수가 k개보다 적다면 나머지는 -1로 저장을 해준다.
  
  # <문제접근법>
  # 1. 조건문을 이용하여 arr의 개수만큼 실행한다.
  # 2. num = arr[i]를 이용하여 arr의 인덱스를 num에 저장한다.
  # 3. 조건문을 이용하여 num이 arr의 인덱스가 처음부터 현재인덱스-1까지 중 포함되지 않는 숫자라면 answer에 저장한다
  # 4. k의 개수에 따라 두가지로 나뉜다.
  # 5. 첫번째로 k개 이상인 경우 k개 일 경우만 생각해주면된다. => 조건문을 통해 k개이면 멈춘다.
  # 6. 두번째로 k개 보다 작은 경우 -1을 추가하면 된다.  
