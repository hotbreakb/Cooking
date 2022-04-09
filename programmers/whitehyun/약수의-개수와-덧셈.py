#
#  약수의 개수와 덧셈
#  https://programmers.co.kr/learn/courses/30/lessons/77884
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/09.
#


from functools import reduce


def solution(left, right):
    answer = 0
    for number in range(left, right + 1):
        factorization = {}
        modular = 2
        temp_number = number
        while temp_number != 1:
            if temp_number % modular == 0:
                if modular not in factorization:
                    factorization[modular] = 1
                factorization[modular] += 1
                temp_number //= modular
            else:
                modular += 1

        # 약수의 개수
        if reduce(lambda acc, element: acc * element, factorization.values(), 1) & 1:
            answer -= number
        else:
            answer += number
    return answer


if __name__ == "__main__":
    for left, right in ((13, 17), (24, 27)):
        print(solution(left, right))
