NOTATION = 3


def solution(n):
    remainer = []
    answer = 0

    while n >= NOTATION:
        remainer.append(n % NOTATION)
        n //= NOTATION
    remainer.append(n)

    degree = len(remainer)-1
    for r in remainer:
        answer += r * (NOTATION**degree)
        degree -= 1
    return answer


n = 100000000
print(solution(n))
