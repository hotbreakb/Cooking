#
#  음양 더하기
#  https://programmers.co.kr/learn/courses/30/lessons/76501
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/07.
#


from functools import reduce


def solution(absolutes, signs):
    return reduce(
        lambda acc, values: acc + values[0] if values[1] else acc - values[0],
        zip(absolutes, signs),
        0,
    )


if __name__ == "__main__":
    absolutes = [[4, 7, 12], [1, 2, 3]]
    signs = [[True, False, True], [False, False, True]]
    for absolute, sign in zip(absolutes, signs):
        print(solution(absolute, sign))
