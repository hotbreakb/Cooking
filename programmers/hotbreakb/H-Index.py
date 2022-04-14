#
#  H-Index
#  https://programmers.co.kr/learn/courses/30/lessons/42747
#  Version: Python 3.8.9
#
#  Created by hotbreakb on 2022/04/12.
#

def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True) + [0]
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return answer


citations = [3, 0, 6, 1, 5]
print(solution(citations))
