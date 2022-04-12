#
#  두 정수 사이의 합
#  https://programmers.co.kr/learn/courses/30/lessons/12912
#  Version: Python 3.8.12
#
#  Created by WhiteHyun on 2022/04/10.
#


solution = lambda a, b: sum(range(a, b + 1)) if a < b else sum(range(b, a + 1))
