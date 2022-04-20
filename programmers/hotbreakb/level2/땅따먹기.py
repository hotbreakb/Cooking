#
#  땅따먹기
#  https://programmers.co.kr/learn/courses/30/lessons/12913
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/15.
#

def solution(land):
    WIDTH = 4

    DP = [[0 for i in range(WIDTH)] for j in range(len(land))]
    DP[0] = land[0]

    for i in range(1, len(land)):
        for j in range(WIDTH):
            before_list = DP[i-1].copy()
            before_list.remove(DP[i-1][j])
            DP[i][j] = max(before_list) + land[i][j]

    return max(DP[-1])
