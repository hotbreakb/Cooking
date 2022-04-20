#
#  위장
#  https://programmers.co.kr/learn/courses/30/lessons/42578
#  Version: Python 3.8.12
#
#  Created by WhiteHyun on 2022/04/19.
#


def solution(clothes):
    answer = 1
    clothes_dict = {}
    for _, type in clothes:
        clothes_dict[type] = clothes_dict.get(type, 1) + 1

    for _, count in clothes_dict.items():
        answer *= count
    return answer - 1
