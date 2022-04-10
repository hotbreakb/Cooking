#
#  124 나라의 숫자
#  https://programmers.co.kr/learn/courses/30/lessons/12899
#  Version: Python 3.8.12
#
#  Created by WhiteHyun on 2022/04/10.
#


def solution(n):
    number = "412"
    answer = ""
    while n > 3:
        answer += number[n % 3]
        if n % 3 == 0:
            n //= 3
            n -= 1
        else:
            n //= 3
    answer += number[n % 3]
    return answer[::-1]


if __name__ == "__main__":
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    answer = [1, 2, 4, 11, 12, 14, 21, 22, 24, 41]
    for n, a in zip(number, answer):
        print(solution(n))
        if solution(n) == a:
            print("정답")
        else:
            print("실패")
