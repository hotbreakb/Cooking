#
#  9461번: 파도반 수열
#  https://www.acmicpc.net/problem/9461
#  Version: Python 3.8.9
#
#  Created by hot on 2022/01/02.
#


from sys import stdin

read = stdin.readline


def getRectangleLength(n):
    lenList = [1, 1, 1, 2, 2]
    if n < 5:
        return lenList[n - 1]

    for i in range(5, n + 1):
        lenList.append(lenList[i - 1] + lenList[i - 5])

    return lenList[n - 1]


testCase = int(input().rstrip())
for _ in range(testCase):
    N = int(input().rstrip())
    print(getRectangleLength(N))
