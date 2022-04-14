#
#  프린터
#  https://programmers.co.kr/learn/courses/30/lessons/42587
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/11.
#

from collections import deque


def solution(priorities, location):
    queue = deque((i, p) for i, p in enumerate(priorities))

    rank = sorted(priorities, reverse=True)
    rankIndex = 0
    count = 1

    while queue:
        if queue[0][1] != rank[rankIndex]:
            queue.append(queue.popleft())
            continue
        if queue[0][0] == location:
            return count
        else:
            queue.popleft()
            rankIndex += 1
            count += 1

    return count


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
