#
#  예상 대진표
#  https://programmers.co.kr/learn/courses/30/lessons/12985
#  Version: Python 3.8.9
#
#  Created by hotbreakb/level2 on 2022/04/18.
#

def solution(n, a, b):
    turn = 1

    if a > b:
        a, b = b, a

    while True:
        if b & 1 == 0 and b-1 == a:
            return turn

        a = getNextTurnNumber(a)
        b = getNextTurnNumber(b)
        turn += 1


def getNextTurnNumber(num: int) -> int:
    if num & 1 == 0:
        return num//2
    return (num+1)//2
