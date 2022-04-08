def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if getDivisorCount(num) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer


def getDivisorCount(num: int) -> int:
    count = 0
    for i in range(1, int(num**(0.5))+1):
        if num % i != 0:
            continue
        if i == num**(0.5):
            count += 1
        else:
            count += 2

    return count


left = 9
right = 9
print(solution(left, right))
