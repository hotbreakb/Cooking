#
#  땅따먹기
#  https://programmers.co.kr/learn/courses/30/lessons/12913
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/17.
#


def solution(lands: list) -> int:
    dp = [[0] * len(lands[0]) for _ in range(len(lands))]
    for i in range(len(lands[0])):
        dp[0][i] = lands[0][i]

    for row in range(1, len(lands)):
        for col in range(len(lands[0])):
            dp[row][col] = (
                max(dp[row - 1][:col] + dp[row - 1][col + 1 :]) + lands[row][col]
            )

    return max(dp[-1])


if __name__ == "__main__":
    print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
