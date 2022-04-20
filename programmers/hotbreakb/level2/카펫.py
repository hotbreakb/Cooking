#
#  카펫
#  https://programmers.co.kr/learn/courses/30/lessons/42842
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/13.
#

def solution(brown, yellow):
    sum = brown + yellow
    for w in range(1, int(sum**(0.5))+1):
        if sum % w != 0:
            continue
        h = sum // w
        if w+h-2 == brown//2:
            return [h, w]
