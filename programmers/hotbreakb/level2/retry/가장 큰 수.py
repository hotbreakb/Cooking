#
#  가장 큰 수
#  https://programmers.co.kr/learn/courses/30/lessons/42746
#  Version: Python 3.8.9
#
#  Created by hotbreakb/retry on 2022/04/16.
#

from typing import OrderedDict


def solution(numbers):
    big_number = ""
    repeated_str_numbers = dict()

    for num in numbers:
        num = str(num)
        if num not in repeated_str_numbers.keys():
            repeated_str_numbers[num] = [str(num)*3]
        else:
            repeated_str_numbers[num].append(str(num)*3)

    repeated_str_numbers = OrderedDict(
        sorted(repeated_str_numbers.items(), key=lambda item: item[1], reverse=True))

    for num, str_num in repeated_str_numbers.items():
        for _ in range(len(str_num)):
            big_number += num

    if set(big_number) == {'0'}:
        return "0"

    return big_number


numbers = [0, 0, 0]
print(solution(numbers))
