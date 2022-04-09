#
#  완주하지 못한 선수
#  https://programmers.co.kr/learn/courses/30/lessons/42576
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/09.
#


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] == participant[i]:
            continue
        else:
            return participant[i]
    return participant[-1]
