#
#  다음 큰 숫자
#  https://programmers.co.kr/learn/courses/30/lessons/12911
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/14.
#
from collections import Counter


def solution(n):
    next_big_number = n+1

    while True:
        if Counter(bin(next_big_number))['1'] == Counter(bin(n))['1']:
            return next_big_number
        next_big_number += 1


n = int(input().rstrip())
print(solution(n))
