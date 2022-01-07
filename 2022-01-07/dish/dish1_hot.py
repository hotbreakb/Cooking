#
#  6588번: 골드바흐의 추측
#  https://www.acmicpc.net/problem/6588
#  Version: Python 3.8.9
#
#  Created by hot on 2022/01/07.
#


from sys import stdin

read = stdin.readline


def getPrimeNum(target) -> int:
    for index in range(2, MAX_NUM + 1):
        if sieve[index] and sieve[target - index]:
            return index
    return -1


def makeSieveList():
    for num in range(2, MAX_NUM + 1):
        if sieve[num]:
            for notSieve in range(num * 2, MAX_NUM + 1, num):
                sieve[notSieve] = False


MAX_NUM = 1000000
sieve = [True] * (MAX_NUM + 1)
makeSieveList()


# 실행
while True:
    testNum = int(input().rstrip())

    # 0이면 실행 종료
    if testNum < 1:
        exit()

    smallerNum = getPrimeNum(testNum)
    print(f"{testNum} = {smallerNum} + {testNum - smallerNum}")
