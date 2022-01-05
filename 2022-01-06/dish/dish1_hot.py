#
#  17425번: 약수의 합
#  https://www.acmicpc.net/problem/17425
#  Version: Python 3.8.9
#
#  Created by hot on 2022/01/06.
#


from sys import stdin

read = stdin.readline

testcase = int(input().rstrip())
sumDivisorGList = [0] * (100000 + 1)

for _ in range(testcase):
    inputNum = int(input().rstrip())
    result = 0

    for i in range(inputNum + 1, 0, -1):
        result += (inputNum // i) * i

    sumDivisorGList[inputNum] = result

    print(result)
