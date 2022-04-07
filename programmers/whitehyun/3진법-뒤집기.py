#
#  3진법 뒤집기
#  https://programmers.co.kr/learn/courses/30/lessons/68935
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/07.
#


def solution(number: int) -> int:
    decimal = number
    answer = ""
    while decimal:
        answer += str(decimal % 3)
        decimal //= 3
    return int(answer, 3)


if __name__ == "__main__":
    for number in (45, 125):
        print(solution(number))
