#
#  나머지가 1이 되는 수 찾기
#  https://programmers.co.kr/learn/courses/30/lessons/87389
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/09.
#


def solution(n):

    if n & 1:
        return 2

    for i in range(3, n):
        if n % i == 1:
            return i
