#
#  3085번: 사탕 게임
#  https://www.acmicpc.net/problem/3085
#  Version: Python 3.8.12
#
#  Created by white on 2022/01/08.
#


from sys import stdin

read = stdin.readline

# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y
def max_eat_count(candies: list, length: int) -> int:
    max_count = 0
    for i in range(length):
        for candy in ("C", "P", "Z", "Y"):
            temp_row_count = 0
            temp_col_count = 0
            for j in range(length):
                # 가로비교
                # 만약 원하는 캔디(?)가 나오면
                if candies[i][j] == candy:
                    temp_row_count += 1
                # 다른 캔디가 나왔을 때, 그 이전에 이어진 캔디의 길이가 이전에 구했던 길이보다 긴 경우
                else:
                    if temp_row_count > max_count:
                        max_count = temp_row_count
                    temp_row_count = 0

                # 세로비교
                if candies[j][i] == candy:
                    temp_col_count += 1
                else:
                    if temp_col_count > max_count:
                        max_count = temp_col_count
                    temp_col_count = 0

            if temp_row_count > max_count:
                max_count = max(max_count, temp_row_count)
            if temp_col_count > max_count:
                max_count = max(max_count, temp_col_count)

    return max_count


def swap_values(sequence: list, i: int, j: int, x: int, y: int) -> None:
    sequence[i][j], sequence[x][y] = sequence[x][y], sequence[i][j]


if __name__ == "__main__":
    length = int(read())
    candy_list = [list(read().rstrip()) for _ in range(length)]
    general_max_count = max_eat_count(candy_list, length)

    for i in range(length):
        for j in range(length - 1):
            # 가로비교
            if candy_list[i][j] != candy_list[i][j + 1]:
                # print((i, j), (i, j + 1))
                swap_values(candy_list, i, j, i, j + 1)
                general_max_count = max(
                    general_max_count, max_eat_count(candy_list, length)
                )
                swap_values(candy_list, i, j, i, j + 1)

            # 세로비교
            if candy_list[j][i] != candy_list[j + 1][i]:
                # print((j, i), (j + 1, i))
                swap_values(candy_list, j, i, j + 1, i)
                general_max_count = max(
                    general_max_count, max_eat_count(candy_list, length)
                )
                swap_values(candy_list, j, i, j + 1, i)

    print(general_max_count)
