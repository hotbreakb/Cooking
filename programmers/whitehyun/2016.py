#
#  2016
#  https://programmers.co.kr/learn/courses/30/lessons/12901
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/09.
#


def solution(month, day):
    total_days = day
    weekends = ("THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED")

    month -= 1
    while month:
        # 1 3 5 7 8 10 12
        if (month <= 7 and month & 1 == 1) or (month >= 8 and month & 1 == 0):
            total_days += 31
        # 2
        elif month == 2:
            total_days += 29
        # 4 6 9 11
        else:
            total_days += 30
        month -= 1

    return weekends[total_days % 7]


print(solution(5, 24))
