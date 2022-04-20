def solution(board, moves):
    answer = 0
    size = len(board)
    boardDollHeight = checkBoardDollHeight(board, size)
    stack = []

    for m in moves:
        if boardDollHeight[m-1] > size-1:
            continue
        doll = board[boardDollHeight[m-1]][m-1]
        boardDollHeight[m-1] += 1
        if stack and stack[-1] == doll:
            answer += 2
            stack.pop()
            continue
        stack.append(doll)

    return answer


def checkBoardDollHeight(board: list, size: int) -> list:
    dollHeight = [size]*size
    for w in range(size):
        for h in range(size):
            if board[h][w] != 0:
                dollHeight[w] = h
                break

    return dollHeight


board = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [
    1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
moves = [1, 1, 1, 1, 1]
print(solution(board, moves))
