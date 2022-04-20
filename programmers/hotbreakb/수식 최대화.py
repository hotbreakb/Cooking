#
#  수식 최대화
#  https://programmers.co.kr/learn/courses/30/lessons/67257
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/13.
#

from itertools import permutations
import re


def solution(expression):
    answer = 0
    expression = expression[1:-1]
    nums = re.findall("\d+", expression)
    calcs = re.findall("\D", expression)
    print(calcs)

    calc_option = ("*", "+", "-")
    calculationList = list(permutations(calc_option, 3))

    for calcList in calculationList:
        first, second, third = calcList
        sum = 0
        stack = []

        # 후위표기식을 써야 하나...

    print(calculationList)
    return answer


expression = input().rstrip()
print(solution(expression))
