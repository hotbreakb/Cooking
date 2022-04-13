#
#  프린터
#  https://programmers.co.kr/learn/courses/30/lessons/42587
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/12.
#


from collections import deque


def solution(priorities, location):
    queue = deque(priorities)
    top_priority = max(priorities)
    wanted_paper = location
    answer = 0
    while True:
        while queue[0] != top_priority:
            queue.append(queue.popleft())
            wanted_paper = wanted_paper - 1 if wanted_paper > 0 else len(queue) - 1
        queue.popleft()
        answer += 1
        wanted_paper -= 1
        if wanted_paper == -1:
            break
        top_priority = max(queue)
    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))
