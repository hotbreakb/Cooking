#
#  15904번: UCPC는 무엇의 약자일까?
#  https://www.acmicpc.net/problem/15904
#  Version: Python 3.9.7
#
#  Created by white on 2022/01/01.
#


from sys import stdin

read = stdin.readline

if __name__ == "__main__":
    uppercase_list = list(filter(lambda x: 65 <= ord(x) <= 90, read().rstrip()))
    ucpc = "UCPC"
    index = 0
    for char in uppercase_list:
        if ucpc[index] == char:
            index += 1
        if index == 4:
            print("I love UCPC")
            break
    else:
        print("I hate UCPC")
