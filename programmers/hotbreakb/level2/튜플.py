#
#  튜플
#  https://programmers.co.kr/learn/courses/30/lessons/64065
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/13.
#

import re


def solution(s):

    origin_s = []

    list_nums = re.findall("(?:(?:\d+,){1,10})?\d+", s)
    for nums in list_nums:
        origin_s.append(list(nums.split(',')))

    origin_s = sorted(origin_s, key=len)
    origin_tuple = origin_s[0]

    for i in range(1, len(origin_s)):
        origin_tuple.append(list(set(origin_s[i])-set(origin_s[i-1]))[0])

    return list(map(int, origin_tuple))
