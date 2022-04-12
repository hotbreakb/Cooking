#
#  같은 숫자는 싫어
#  https://programmers.co.kr/learn/courses/30/lessons/12906
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/10.
#


def solution(arr):
    answer = []
    for element in arr:
        if answer and answer[-1] == element:
            continue
        answer.append(element)
    return answer
