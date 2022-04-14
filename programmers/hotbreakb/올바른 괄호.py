#
#  올바른 괄호
#  https://programmers.co.kr/learn/courses/30/lessons/12909
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/14.
#

def solution(s):
    stack = []

    for bracket in s:
        if bracket == "(":
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()

    if stack:
        return False
    return True
