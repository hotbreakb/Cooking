#
#  두 정수 사이의 합
#  https://programmers.co.kr/learn/courses/30/lessons/12912
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/10.
#

def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))
