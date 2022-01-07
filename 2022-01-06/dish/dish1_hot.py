#
#  17425번: 약수의 합
#  https://www.acmicpc.net/problem/17425
#  Version: Python 3.8.9
#
#  Created by hot on 2022/01/06.
#


from sys import stdin

read = stdin.readline

MAX = 100000
sumList = [0] * (MAX + 1)
result = 0

for i in range(1, MAX + 1):
    result += (MAX // i) * i

testcase = int(input().rstrip())

for _ in range(testcase):
    inputNum = int(input().rstrip())
    result = 0

    print(result)
