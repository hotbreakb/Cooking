#
#  숫자의 표현
#  https://programmers.co.kr/learn/courses/30/lessons/12924
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/14.
#

def solution(n):
    answer = 1

    for num in range(n-1, 0, -1):
        sum = num
        for left_num in range(num-1, 0, -1):
            sum += left_num
            if sum >= n:
                break
        if sum == n:
            answer += 1
    return answer


n = int(input().rstrip())
print(solution(n))
