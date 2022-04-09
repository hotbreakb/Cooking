#
#  폰켓몬
#  https://programmers.co.kr/learn/courses/30/lessons/1845
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/09.
#


def solution(nums):
    count = len(nums)
    kind_count = len(set(nums))
    while count - kind_count < count >> 1:
        kind_count -= 1
    return kind_count
