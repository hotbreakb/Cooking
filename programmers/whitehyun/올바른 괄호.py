#
#  올바른 괄호
#  https://programmers.co.kr/learn/courses/30/lessons/12909
#  Version: Python 3.9.10
#
#  Created by WhiteHyun on 2022/04/16.
#


def solution(string: str) -> bool:
    stack = []
    stack.append(string[0])

    for bracket in string[1:]:
        if stack and stack[-1] == "(" and bracket == ")":
            stack.pop()
        else:
            stack.append(bracket)

    if stack:
        return False

    return True
