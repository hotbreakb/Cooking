#
#  17427번: 약수의 합 2
#  https://www.acmicpc.net/problem/17427
#  Version: Python 3.8.9
#
#  Created by hot on 2022/01/04.
#

from sys import stdin

read = stdin.readline

inputNum = int(input().rstrip())
result = 0

for i in range(1, inputNum + 1):
    result += (inputNum // i) * i

print(result)
