#
#  최솟값 만들기
#  https://programmers.co.kr/learn/courses/30/lessons/12941
#  Version: Python 3.8.12
#
#  Created by WhiteHyun on 2022/04/12.
#


def solution(A, B):
    return sum(map(lambda x, y: x * y, sorted(A), sorted(B, reverse=True)))
