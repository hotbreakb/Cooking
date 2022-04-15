#
#  짝지어 제거하기
#  https://programmers.co.kr/learn/courses/30/lessons/12973
#  Version: Python 3.8.12
#
#  Created by WhiteHyun on 2022/04/15.
#


def solution(s):
    stack = [s[0]]  # 첫 번째 문자를 집어넣고 시작.

    for element in s[1:]:
        if not stack:  # 스택이 비었으면 값을 넣음
            stack.append(element)
        elif stack[-1] == element:  # 스택의 peak이 element와 같으면 값 제거
            stack.pop()
        else:  # 같지 않으면 그냥 원소를 넣음
            stack.append(element)

    if stack:
        return 0
    return 1


if __name__ == "__main__":
    print(solution("baabaa"))
    print(solution("aabaab"))
    print(solution("cdcd"))
