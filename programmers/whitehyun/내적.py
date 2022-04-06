#
#  내적
#  https://programmers.co.kr/learn/courses/30/lessons/70128
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/06.
#


def solution(a: list, b: list):
    return sum(map(lambda values: values[0] * values[1], zip(a, b)))


if __name__ == "__main__":
    a = [[1, 2, 3, 4], [-1, 0, 1]]
    b = [[-3, -1, 0, 2], [1, 0, -1]]

    for x, y in zip(a, b):
        print(solution(x, y))
