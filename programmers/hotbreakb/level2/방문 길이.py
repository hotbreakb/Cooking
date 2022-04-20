#
#  방문 길이
#  https://programmers.co.kr/learn/courses/30/lessons/49994
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/17.
#
SIZE = 5


def solution(dirs):
    return len(set(getRoutes((0, 0), list(dirs))))


def getRoutes(start: tuple, dirs: list) -> list:
    before = start
    routes = []
    for dir in dirs:
        after = getCurrentPos(before, dir)
        if before == after:
            continue
        routes.append(tuple(sorted([before, after])))
        before = after

    return routes


def getCurrentPos(pos: list, dir: str) -> tuple:
    x, y = pos
    if dir == "L":
        if x - 1 >= -SIZE:
            x -= 1
    elif dir == "R":
        if x + 1 <= SIZE:
            x += 1
    elif dir == "U":
        if y + 1 <= SIZE:
            y += 1
    else:
        if y - 1 >= -SIZE:
            y -= 1

    return (x, y)


dirs = "LLLLLUUDDRRRRRRR"
print(solution(dirs))
