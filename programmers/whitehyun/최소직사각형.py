#
#  최소직사각형
#  https://programmers.co.kr/learn/courses/30/lessons/86491
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/09.
#

from functools import reduce


def solution(sizes):
    # 크기를 정렬
    sorted_sizes = [size if size[0] < size[1] else [size[1], size[0]] for size in sizes]
    return reduce(
        lambda acc, x: acc * max(x),
        zip(*sorted_sizes),
        1,
    )


print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
