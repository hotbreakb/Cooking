#
#  점프와 순간 이동
#  https://programmers.co.kr/learn/courses/30/lessons/12980
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/17.
#

def solution(n):
    decrement = 0

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            decrement += 1

    return decrement+1


n = int(input().rstrip())
print(solution(n))
