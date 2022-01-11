#
#  3085번: 사탕 게임
#  https://www.acmicpc.net/problem/3085
#  Version: Python 3.8.9
#
#  Created by hot on 2022/01/08.
#


from sys import stdin

read = stdin.readline

boardSize = int(input().rstrip())
originBoard = [list(input()) for h in range(boardSize)]
countMaxChar = 0


def findMaxChar(board):
    result = 0

    # 행에서 가장 긴 거 찾기 (h: 위에서 아래로, w: 왼쪽에서 오른쪽으로)
    for h in range(boardSize):
        countMaxCharInRow = 1  # 문자 하나만 있어도 1
        for w in range(boardSize - 1):
            if board[h][w] == board[h][w + 1]:
                countMaxCharInRow += 1
            else:
                result = max(result, countMaxCharInRow)
                countMaxCharInRow = 1
        result = max(result, countMaxCharInRow)

    return result


def getCountMaxChar(board):
    # 그대로, 행과 열을 바꿔서
    return max(findMaxChar(board), findMaxChar([list(x) for x in zip(*board)]))


def switchListValue(board):
    global countMaxChar

    for h in range(boardSize):
        for w in range(boardSize - 1):
            if w != 0 and board[h][w] == board[h][w + 1]:
                continue

            board[h][w], board[h][w + 1] = board[h][w + 1], board[h][w]
            countMaxChar = max(countMaxChar, getCountMaxChar(board))
            board[h][w], board[h][w + 1] = board[h][w + 1], board[h][w]


switchListValue(originBoard)
switchListValue([list(x) for x in zip(*originBoard)])
print(countMaxChar)
