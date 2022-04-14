#
#  가운데 글자 가져오기
#  https://programmers.co.kr/learn/courses/30/lessons/12903
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/10.
#


def solution(s):
    count = len(s)
    if count & 1:
        return s[count >> 1]
    return s[(count >> 1) - 1 : (count >> 1) + 1]
