def solution(d, budget):
    answer = 0
    sum = 0

    d = sorted(d)
    for num in d:
        sum += num

        if sum > budget:
            break
        answer += 1
    return answer


d = [1, 2, 8, 9]
budget = 2
print(solution(d, budget))
