#
#  예산
#  https://programmers.co.kr/learn/courses/30/lessons/12982
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/09.
#


def solution(d, budget):
    answer = 0
    departments = sorted(d)
    for department in departments:
        budget -= department
        if budget >= 0:
            answer += 1

    return answer


if __name__ == "__main__":
    d = [[1, 3, 2, 5, 4], [2, 2, 3, 3]]
    budget = [9, 10]
    for dd, bb in zip(d, budget):
        print(solution(dd, bb))
