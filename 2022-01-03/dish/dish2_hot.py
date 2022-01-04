#
#  17427번: 약수의 합 2
#  https://www.acmicpc.net/problem/17427
#  Version: Python 3.8.9
#
#  Created by hot on 2022/01/03.
#


from sys import stdin

read = stdin.readline

if __name__ == "__main__":
    pass


def getDivisorSum(num):
    divisorList = []

    for i in range(1, int((num) ** (1 / 2)) + 1):
        if num % i == 0:
            divisorList.append(i)
            if i ** 2 != num:
                divisorList.append(num // i)

    return sum(divisorList)


inputNum = int(input().rstrip())
sumList = [0] * (inputNum + 1)

for n in range(1, inputNum + 1):
    sumList[n] = getDivisorSum(n)

print(sum(sumList))
