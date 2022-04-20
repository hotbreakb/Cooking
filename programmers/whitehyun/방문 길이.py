#
#  방문 길이
#  https://programmers.co.kr/learn/courses/30/lessons/49994
#  Version: Python 3.8.12
#
#  Created by WhiteHyun on 2022/04/19.
#


def solution(dirs):
    dir_dict = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    visited = set()
    count = 0
    x, y = 5, 5  # 초기 위치
    for dir in dirs:
        # dx, dy: 움직인 위치
        dx, dy = dir_dict[dir]
        dx += x
        dy += y
        # 위치를 벗어나면 다시 진행
        if dx < 0 or dx > 10 or dy < 0 or dy > 10:
            continue

        # 방문하지 않았다면
        if (x, y, dx, dy) not in visited:
            count += 1
            visited.add((x, y, dx, dy))
            visited.add((dx, dy, x, y))
        # 이미 방문한 곳인 경우 위치만 갱신하고 반복문 진행
        x, y = dx, dy

    return count
