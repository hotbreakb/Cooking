#
#  모음사전
#  https://programmers.co.kr/learn/courses/30/lessons/84512
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/14.
#

size = 5
board = [[1 for j in range(size)] for i in range(size)]
interval = 1


for i in range(size):
    for j in range(1, size):
        board[i][j] = board[i][j-1] + interval
    interval += pow(size, i+1)


def solution(word):
    index = 0
    word = '{:<05s}'.format(word)
    for i in range(size):
        if word[i] == "0":
            continue
        index += board[4-i][getColumns(word[i])]
    return index


def getColumns(char: str) -> int:
    if char == "A":
        return 0
    elif char == "E":
        return 1
    elif char == "I":
        return 2
    elif char == "O":
        return 3
    else:
        return 4


word = input().rstrip()
print(solution(word))
