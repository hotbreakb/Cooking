#
#  체육복
#  https://programmers.co.kr/learn/courses/30/lessons/42862
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/08.
#


def solution(n, lost, reserve):
    reserve_set = set(reserve)
    lost_set = set(lost)
    intersection = reserve_set.intersection(lost_set)
    reserve_set -= intersection
    lost_set -= intersection
    for number in range(n):
        if number in reserve_set and number in lost_set:
            reserve_set.remove(number)
            lost_set.remove(number)
        elif number in reserve_set:
            if number - 1 in lost_set:
                lost_set.remove(number - 1)
                reserve_set.remove(number)
            elif number + 1 in lost_set:
                lost_set.remove(number + 1)
                reserve_set.remove(number)
        elif number in lost_set:
            if number - 1 in reserve_set:
                lost_set.remove(number)
                reserve_set.remove(number - 1)
            elif number + 1 in reserve_set:
                lost_set.remove(number)
                reserve_set.remove(number + 1)
    return n - len(lost_set)


if __name__ == "__main__":
    ns = [5, 5, 3, 6]
    losts = [[2, 4], [2, 4], [3], [2, 4, 5]]
    reserves = [[1, 3, 5], [3], [1], [1, 3, 6]]
    for n, lost, reserve in zip(ns, losts, reserves):
        print(solution(n, lost, reserve))
