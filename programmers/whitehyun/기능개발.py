#
#  기능개발
#  https://programmers.co.kr/learn/courses/30/lessons/42586
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/12.
#


def solution(progresses, speeds):
    day = 1
    answer = []
    for i in range(len(speeds)):
        if progresses[i] + day * speeds[i] >= 100:
            answer[-1] += 1
        else:
            answer.append(1)
            while progresses[i] + day * speeds[i] < 100:
                day += 1
    return answer
