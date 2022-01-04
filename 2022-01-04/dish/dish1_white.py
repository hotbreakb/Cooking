#
#  17427번: 약수의 합 2
#  https://www.acmicpc.net/problem/17427
#  Version: Python 3.8.12
#
#  Created by white on 2022/01/04.
#


from sys import stdin

read = stdin.readline

if __name__ == "__main__":
    length = int(read())
    count = length  # 1 * length
    # ✨ O(n) ✨
    for i in range(2, length + 1):  # 2~length
        count += length // i * i
    print(count)

