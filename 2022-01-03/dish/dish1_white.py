#
#  4375번: 1
#  https://www.acmicpc.net/problem/4375
#  Version: Python 3.8.12
#
#  Created by white on 2022/01/03.
#


from sys import stdin

read = stdin.readline

if __name__ == "__main__":
    while value := read():
        count = 1
        number = int(value)
        div_number = 1  # 1, 11, 111, 1111...
        while div_number % number != 0:
            count += 1
            div_number = div_number * 10 + 1
        print(count)
