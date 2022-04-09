#
#  없는 숫자 더하기
#  https://programmers.co.kr/learn/courses/30/lessons/86051
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/06.
#


def solution(numbers: list):
    set_numbers = set([i for i in range(10)])
    for number in numbers:
        set_numbers.remove(number)
    return sum(set_numbers)


if __name__ == "__main__":
    for numbers in ([1, 2, 3, 4, 6, 7, 8, 0], [5, 8, 4, 0, 6, 7, 9]):
        print(solution(numbers))
