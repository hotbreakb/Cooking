#
#  다음 큰 숫자
#  https://programmers.co.kr/learn/courses/30/lessons/12911
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/16.
#


def solution(number: int) -> int:
    answer = number + 1
    binary_number_one_count = bin(number).count("1")

    while binary_number_one_count != bin(answer).count("1"):
        answer += 1

    return answer
