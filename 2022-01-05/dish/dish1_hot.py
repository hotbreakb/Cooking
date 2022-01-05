#
#  1157번: 단어 공부
#  https://www.acmicpc.net/problem/1157
#  Version: Python 3.8.9
#
#  Created by hot on 2022/01/05.
#


from sys import stdin
from typing import Counter

read = stdin.readline


def findMaxChar(word):
    counter = sorted(Counter(word).items(), key=lambda item:-item[1])

    if len(counter) == 1 or (counter[0][1] != counter[1][1]):
        return counter[0][0].upper()
    return '?'

inputWord = input().rstrip().lower()
print(findMaxChar(inputWord))