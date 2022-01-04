#
#  4375번: 1
#  https://www.acmicpc.net/problem/4375
#  Version: Python 3.8.9
#
#  Created by hot on 2022/01/03.
#


from sys import stdin

read = stdin.readline


def DividedLeg(n):
    if n == 1:
        return 1

    if n % 2 == 0 or n % 5 == 0:
        return -1

    oneString = "11"

    while True:
        if int(oneString) % n == 0:
            return len(oneString)
        else:
            oneString += "1"


while True:
    try:
        num = int(input().rstrip())
        print(DividedLeg(num))
    except EOFError:
        break
