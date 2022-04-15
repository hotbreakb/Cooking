#
#  최댓값과 최솟값
#  https://programmers.co.kr/learn/courses/30/lessons/12939
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/12.
#


def solution(s):
    answer = sorted(map(int, s.split()))
    return f"{answer[0]} {answer[-1]}"
