#
#  로또의 최고 순위와 최저 순위
#  https://programmers.co.kr/learn/courses/30/lessons/77484
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/07.
#


def solution(lottos, win_nums):
    win_lottery = set(win_nums)
    correct_count = 0
    zero_count = 0
    rank_list = [6] + [i for i in range(6, 0, -1)]

    for number in lottos:
        if number == 0:
            zero_count += 1
        elif number in win_lottery:
            correct_count += 1

    min_rank = rank_list[correct_count]
    max_rank = rank_list[correct_count + zero_count]
    return max_rank, min_rank


if __name__ == "__main__":
    lottos = [[44, 1, 0, 0, 31, 25], [0, 0, 0, 0, 0, 0], [45, 4, 35, 20, 3, 9]]
    win_nums = [[31, 10, 45, 1, 6, 19], [38, 19, 20, 40, 15, 25], [20, 9, 3, 45, 4, 35]]
    for lotto, win_num in zip(lottos, win_nums):
        print(solution(lotto, win_num))
