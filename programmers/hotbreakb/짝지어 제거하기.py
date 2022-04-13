#
#  짝지어 제거하기
#  https://programmers.co.kr/learn/courses/30/lessons/12973
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/13.
#

def solution(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
            continue
        stack.append()

    if not stack:
        return 1
    return 0
