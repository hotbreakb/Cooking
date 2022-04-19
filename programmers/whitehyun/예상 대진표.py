#
#  예상 대진표
#  https://programmers.co.kr/learn/courses/30/lessons/12985
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/19.
#


import math


def solution(n, a, b):

    while (a <= (n >> 1) and b <= (n >> 1)) or (a > (n >> 1) and b > (n >> 1)):
        n >>= 1
        if a > (n >> 1):
            a = (a - 1) % n + 1
            b = (b - 1) % n + 1
    return int(math.log2(n))


if __name__ == "__main__":
    print(solution(8, 4, 7))
    print(solution(8, 7, 8))
    print(solution(8, 3, 4))
    print(solution(16, 9, 12))
    print(solution(16, 14, 16))
    print(solution(16, 15, 16))
