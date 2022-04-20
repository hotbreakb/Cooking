#
#  n^2 배열 자르기
#  https://programmers.co.kr/learn/courses/30/lessons/87390
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/14.
#

def solution(n, left, right):
    answer = []

    for index in range(left, right+1):
        h = index//n
        w = index % n
        answer.append(max(h, w)+1)

    return answer


n = int(input().rstrip())
left = int(input().rstrip())
right = int(input().rstrip())
print(solution(n, left, right))
