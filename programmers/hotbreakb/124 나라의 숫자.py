#
#  124 나라의 숫자
#  https://programmers.co.kr/learn/courses/30/lessons/12899
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/10.
#

def solution(n):
    answer = ""

    while n > 0:
        n -= 1
        answer = "124"[n % 3]+answer
        n //= 3

    return answer


n = int(input().rstrip())
print(solution(n))
