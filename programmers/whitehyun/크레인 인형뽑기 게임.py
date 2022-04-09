#
#  크레인 인형뽑기 게임
#  https://programmers.co.kr/learn/courses/30/lessons/64061
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/09.
#


def solution(board, moves):
    count = len(board)
    stack_brackets = []
    answer = 0

    for move in moves:
        move -= 1
        index = 0

        # 인형을 집어듦
        while board[index][move] == 0:
            index += 1
            if index == count:
                break
        else:
            stack_brackets.append(board[index][move])
            board[index][move] = 0

        # 바구니 점검
        if len(stack_brackets) > 1 and stack_brackets[-1] == stack_brackets[-2]:
            stack_brackets.pop()
            stack_brackets.pop()
            answer += 2

    return answer


if __name__ == "__main__":
    print(
        solution(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 3],
                [0, 2, 5, 0, 1],
                [4, 2, 4, 4, 2],
                [3, 5, 1, 3, 1],
            ],
            [1, 5, 3, 5, 1, 2, 1, 4],
        )
    )
