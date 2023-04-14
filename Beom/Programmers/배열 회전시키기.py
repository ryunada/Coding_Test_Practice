def solution(numbers, direction):
    answer = []
    for i in range(len(numbers)):
        if direction == "right":
            if i == 0:
                answer.append(numbers[len(numbers)-1])
            else:
                answer.append(numbers[i-1])
        elif direction == "left":
            if i != len(numbers)-1:
                answer.append(numbers[i+1])
            else:
                answer.append(numbers[0])
    return answer

print(solution([1,2,3],"right"))