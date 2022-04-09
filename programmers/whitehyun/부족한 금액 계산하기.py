#
#  부족한 금액 계산하기
#  https://programmers.co.kr/learn/courses/30/lessons/82612
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/09.
#


def solution(price, money, count):
    need_money = price * sum([i for i in range(1, count + 1)])
    if (short_cash := money - need_money) > 0:
        return 0
    else:
        return -short_cash
